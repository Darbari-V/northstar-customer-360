#!/usr/bin/env python3
"""Render complete Northstar documents without editing their Markdown sources.

Install requirements-site.txt, then run this script from any directory.
Use --check in CI to verify coverage, links and generated-file freshness.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from pathlib import Path, PurePosixPath
from string import Template
from urllib.parse import unquote, urlsplit, urlunsplit

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/Darbari-V/northstar-customer-360/blob/main/'
GUIDES = json.loads((ROOT / 'web/reading-guides.json').read_text(encoding='utf-8'))
PAGES = GUIDES['pages']
OVERVIEWS = json.loads((ROOT / 'web/original-web-overviews.json').read_text(encoding='utf-8'))
PAGE_BY_SOURCE = {page['source']: page['output'] for page in PAGES}


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)


def normalized(value: str) -> str:
    return re.sub(r'\s+', '', value)


def parse(value: str) -> BeautifulSoup:
    return BeautifulSoup(value, 'html.parser')


def markdown_document(source: str):
    renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'sane_lists'],
                                 extension_configs={'toc': {'toc_depth': '2-3'}})
    document = parse(renderer.convert(source))
    headings = document.find_all('h1')
    if len(headings) != 1:
        raise ValueError('Every artefact must have exactly one top-level title')
    title = headings[0].get_text()
    headings[0].extract()
    return title, document, renderer.toc


def rewrite_links(document, source_path: str):
    for link in document.find_all('a', href=True):
        uri = urlsplit(link['href'])
        if not uri.scheme and not uri.netloc and uri.path:
            parts = []
            for part in (PurePosixPath(source_path).parent / unquote(uri.path)).parts:
                if part == '..':
                    if not parts:
                        raise ValueError('Link escapes repository: ' + link['href'])
                    parts.pop()
                elif part != '.':
                    parts.append(part)
            resolved = '/'.join(parts)
            if resolved in PAGE_BY_SOURCE:
                link['href'] = urlunsplit(('', '', PAGE_BY_SOURCE[resolved], uri.query, uri.fragment))
            elif resolved == 'README.md':
                link['href'] = GITHUB + resolved
            elif (ROOT / resolved).is_file():
                link['href'] = urlunsplit(('', '', resolved, uri.query, uri.fragment))
            else:
                raise ValueError('Missing source link: ' + resolved)
        if link['href'].startswith(('https://', 'http://')):
            link['target'] = '_blank'
            link['rel'] = ['noopener', 'noreferrer']


SQL_LINES = {
    'SELECT Customers.customer_id, Customers.name': 'Return the customer identifier and customer name.',
    'FROM Customers': 'Start with the Customers table.',
    'WHERE phone IS NULL': 'Keep records where no phone value is stored. NULL means the value is missing in this fixture.',
    'SELECT Enquiries.enquiry_id': 'Return the enquiry identifier, so each result can be traced to a record.',
    'FROM Enquiries': 'Start with the Enquiries table.',
    'LEFT JOIN Customers': 'Keep every enquiry while looking for a matching customer record.',
    'ON Enquiries.customer_id = Customers.customer_id': 'Look for a match by comparing the customer identifiers stored in the two tables.',
    'WHERE Customers.customer_id IS NULL': 'Keep rows where the join found no matching customer. This can happen for an absent identifier or a recorded but unmatched identifier.',
    'AND Enquiries.customer_id IS NOT NULL': 'Also require the enquiry to contain an identifier. This separates an unmatched recorded ID from an empty ID.',
    'SELECT enquiry_id': 'Return the enquiry identifier.',
    'WHERE customer_id IS NULL': 'Keep enquiries that have no stored customer identifier.',
    'SELECT Enquiries.enquiry_id, Customers.name': 'Return each matching enquiry identifier together with the customer name.',
    'INNER JOIN Customers': 'Keep only enquiries that match a customer record. Unmatched enquiries are excluded.',
    'ORDER BY Enquiries.enquiry_id': 'Sort the results by enquiry identifier.',
    'SELECT WebsiteSubmissions.submission_id': 'Return the identifier of each website submission found by the check.',
    'FROM WebsiteSubmissions': 'Start with the website submissions for the illustrative reporting period.',
    'LEFT JOIN SalesEnquiryRegister': 'Keep every website submission while looking for its corresponding entry in the Sales register.',
    'ON WebsiteSubmissions.submission_id = SalesEnquiryRegister.submission_id': 'Match the two sources using the same submission identifier.',
    'WHERE SalesEnquiryRegister.submission_id IS NULL': 'Keep website submissions for which the join found no Sales register entry.',
    'ORDER BY WebsiteSubmissions.submission_id': 'Sort the results by website submission identifier.',
    'SELECT phone, COUNT(*) AS number_of_customers': 'Return each phone value and the number of customer records using it. The count column is named number_of_customers.',
    'WHERE phone IS NOT NULL': 'Leave out missing phone values before looking for repeated recorded values.',
    'GROUP BY phone': 'Put customer records with the same phone value into a group.',
    'HAVING COUNT(*) > 1': 'Keep groups containing more than one record. A shared phone value is a review signal, not proof of a duplicate customer.'
}


def add_sql_walkthroughs(document):
    for code in list(document.select('pre > code.language-sql')):
        lines = [line for line in code.get_text().splitlines() if line.strip()]
        explanation = document.new_tag('details', attrs={'class': 'sql-walkthrough', 'data-reader-added': 'sql-help'})
        label = document.new_tag('summary')
        label.string = 'Read this query line by line'
        explanation.append(label)
        ordered = document.new_tag('ol', attrs={'class': 'sql-line-list'})
        for line in lines:
            key = line.strip().rstrip(';')
            if key not in SQL_LINES:
                raise ValueError('Add a plain-English explanation for SQL line: ' + line)
            item = document.new_tag('li')
            statement = document.new_tag('code')
            statement.string = line
            meaning = document.new_tag('p')
            meaning.string = SQL_LINES[key]
            item.extend([statement, meaning])
            ordered.append(item)
        explanation.append(ordered)
        code.parent.insert_after(explanation)


def add_reader_guides(document, page):
    headings = document.find_all('h2')
    if len(headings) != len(page['sections']):
        raise ValueError(f"Section guide count differs for {page['source']}: {len(headings)} headings")
    for heading, text in zip(headings, page['sections']):
        note = document.new_tag('aside', attrs={'class': 'reader-note', 'data-reader-added': 'section-guide', 'aria-label': 'In plain English'})
        label = document.new_tag('span', attrs={'class': 'reader-note-label'})
        label.string = 'In plain English'
        paragraph = document.new_tag('p')
        paragraph.string = text
        note.extend([label, paragraph])
        heading.insert_after(note)
    for table in list(document.find_all('table')):
        wrap = document.new_tag('div', attrs={'class': 'table-wrap', 'role': 'region', 'tabindex': '0', 'aria-label': 'Scrollable document table'})
        table.wrap(wrap)
        hint = document.new_tag('p', attrs={'class': 'table-hint', 'data-reader-added': 'table-help'})
        hint.string = 'On a small screen, swipe across this table to read every column.'
        wrap.insert_before(hint)
    for pre in document.find_all('pre'):
        pre['tabindex'] = '0'
        pre['aria-label'] = 'Scrollable original code or model'
    add_sql_walkthroughs(document)


def legacy_overview(page):
    saved = parse(OVERVIEWS[page['output']])
    main = saved.find('main')
    if not main:
        raise ValueError('Original overview has no main content: ' + page['output'])
    for heading in main.find_all(re.compile(r'^h[1-5]$')):
        heading.name = 'h' + str(int(heading.name[1]) + 1)
    for element in main.find_all(id=True):
        element['id'] = 'overview-' + element['id']
    return main.decode_contents()


def source_metrics(document):
    return {
        'sections': len(document.find_all('h2')),
        'subsections': len(document.find_all('h3')),
        'tables': len(document.find_all('table')),
        'table_cells': len(document.find_all(['td', 'th'])),
        'code_blocks': len(document.select('pre > code')),
    }


def verify_document(output: str, page, original_document, title):
    result = parse(output)
    article = result.select_one('article.document-content')
    if not article:
        raise ValueError('Full document absent: ' + page['output'])
    copy = parse(str(article))
    for extra in copy.select('[data-reader-added]'):
        extra.decompose()
    if normalized(copy.get_text()) != normalized(original_document.get_text()):
        raise ValueError('Document text was omitted or changed: ' + page['source'])
    if source_metrics(copy) != source_metrics(original_document):
        raise ValueError('Document structure differs: ' + page['source'])
    original_codes = [code.get_text() for code in original_document.select('pre > code')]
    actual_codes = [code.get_text() for code in copy.select('pre > code')]
    if original_codes != actual_codes:
        raise ValueError('Original code changed: ' + page['source'])
    original_cells = [normalized(cell.get_text()) for cell in original_document.find_all(['th', 'td'])]
    actual_cells = [normalized(cell.get_text()) for cell in copy.find_all(['th', 'td'])]
    if original_cells != actual_cells:
        raise ValueError('Original table cells changed: ' + page['source'])
    if result.find('h1').get_text() != title or len(result.find_all('h1')) != 1:
        raise ValueError('Document title differs or is duplicated')
    original_main = parse(OVERVIEWS[page['output']]).find('main')
    saved_overview = result.select_one('.original-overview')
    if normalized(original_main.get_text()) != normalized(saved_overview.get_text()):
        raise ValueError('Earlier web overview omitted or changed: ' + page['output'])
    ids = [element['id'] for element in result.find_all(id=True)]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate anchor IDs: ' + page['output'])
    section_ids = {heading['id'] for heading in article.find_all(['h2', 'h3'])}
    contents_ids = {link['href'][1:] for link in result.select('.reader-contents a[href^="#"]')}
    if section_ids != contents_ids:
        raise ValueError('Contents does not cover every section and subsection: ' + page['output'])
    return source_metrics(original_document)


def render_page(page, index):
    source_bytes = (ROOT / page['source']).read_bytes()
    title, original, contents = markdown_document(source_bytes.decode('utf-8'))
    document = parse(str(original))
    rewrite_links(document, page['source'])
    add_reader_guides(document, page)
    project_nav = '<a href="index.html">Overview</a>'
    for item in PAGES:
        current = ' aria-current="page"' if item is page else ''
        project_nav += f'<a href="{esc(item["output"])}"{current}>{esc(item["short"])}</a>'
    project_nav += '<a href="https://darbari-v.github.io/#projects">← Portfolio</a>'
    journey = ''.join(f'<a href="{esc(item["output"])}"' + (' aria-current="step"' if item is page else '') + f'><span class="reader-step-number">{i + 1:02d}</span><span>{esc(item["step"])}</span></a>' for i, item in enumerate(PAGES))
    adjacent = ''
    if index:
        previous = PAGES[index - 1]
        adjacent += f'<a href="{esc(previous["output"])}">← Previous: {esc(previous["step"])}</a>'
    if index + 1 < len(PAGES):
        following = PAGES[index + 1]
        adjacent += f'<a href="{esc(following["output"])}">Next: {esc(following["step"])} →</a>'
        next_title = following['step']
    else:
        adjacent += '<a href="index.html#roadmap">View the development roadmap →</a>'
        next_title = 'What remains to be built and verified'
    sql = ''
    if page['output'] == '05-customer-data.html':
        sql_bytes = (ROOT / 'data/05-synthetic-data-and-checks.sql').read_bytes()
        sql = '<details class="reader-fixture"><summary>Complete reproducible SQL file — setup, sample records and all seven queries</summary><p>This practice script recreates four synthetic diagnostic tables, adds the invented records and runs the seven investigations. The original script is reproduced in full below.</p><p><a href="data/05-synthetic-data-and-checks.sql" download>Download the SQL practice file</a></p><pre tabindex="0" aria-label="Complete original SQL practice file"><code data-source="data/05-synthetic-data-and-checks.sql">' + esc(sql_bytes.decode('utf-8')) + '</code></pre></details>'
    template = Template((ROOT / 'web/artefact-page.template.html').read_text(encoding='utf-8'))
    output = template.substitute(
        description=esc(page['lead']), browser_title=esc(page['short']), title=esc(title),
        step_number=index + 1, step_count=len(PAGES), status=esc(page['status']),
        lead=esc(page['lead']), story=esc(page['story']), connection=esc(page['connection']),
        project_navigation=project_nav, journey_navigation=journey,
        glossary=''.join(f'<dt>{esc(term)}</dt><dd>{esc(definition)}</dd>' for term, definition in GUIDES['glossary']),
        contents=contents, source=esc(page['source']), source_hash=hashlib.sha256(source_bytes).hexdigest(),
        document=str(document), reproducible_sql=sql, next_title=esc(next_title),
        next_explanation=esc(page['next']), previous_next=adjacent,
        source_url=esc(GITHUB + page['source']), original_overview=legacy_overview(page),
    )
    metrics = verify_document(output, page, original, title)
    if sql:
        actual_sql = parse(output).select_one('.reader-fixture code').get_text()
        if actual_sql != sql_bytes.decode('utf-8'):
            raise ValueError('The full SQL fixture was changed during rendering')
    return output, metrics


def verify_links(outputs):
    parsed = {name: parse(content) for name, content in outputs.items()}
    parsed['index.html'] = parse((ROOT / 'index.html').read_text(encoding='utf-8'))
    for filename, soup in parsed.items():
        for element in soup.find_all(['a', 'img', 'script', 'link']):
            uri = element.get('href') or element.get('src')
            if not uri:
                continue
            link = urlsplit(uri)
            if link.scheme or link.netloc or link.path.startswith('/'):
                continue
            path = unquote(link.path) or filename
            if path not in parsed and not (ROOT / path).is_file():
                raise ValueError(f'Missing link in {filename}: {uri}')
            if link.fragment and path in parsed:
                if not parsed[path].find(id=unquote(link.fragment)):
                    raise ValueError(f'Missing fragment in {filename}: {uri}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate generated content without writing files')
    args = parser.parse_args()
    outputs = {}
    totals = {'sections': 0, 'subsections': 0, 'tables': 0, 'table_cells': 0, 'code_blocks': 0}
    for index, page in enumerate(PAGES):
        output, metrics = render_page(page, index)
        outputs[page['output']] = output
        for key, count in metrics.items():
            totals[key] += count
        print(f"Verified {page['output']}: {metrics}")
    verify_links(outputs)
    stale = []
    for filename, output in outputs.items():
        path = ROOT / filename
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8') != output:
                stale.append(filename)
        else:
            path.write_text(output, encoding='utf-8')
    if stale:
        raise SystemExit('Regenerate these pages: ' + ', '.join(stale))
    print(f"PASS: {len(outputs)} complete artefacts; {totals}; original overview text retained; links and contents verified.")


if __name__ == '__main__':
    main()
