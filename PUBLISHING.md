# Publishing complete Northstar artefacts

The files in `docs/` are the master documents. The six existing public artefact URLs now display their full contents. Original document text, tables and code are checked during rendering; reader explanations are separate additions.

## Update a document

1. Edit and review the relevant Markdown document in `docs/`.
2. If its major sections or SQL statements change, update the corresponding explanations in `web/reading-guides.json` or `scripts/build_artefacts.py`.
3. Install the pinned rendering dependencies and regenerate the pages:

```sh
python -m pip install -r requirements-site.txt
python scripts/build_artefacts.py
python scripts/build_artefacts.py --check
```

4. Review the generated page on desktop and a narrow screen, then commit the source change together with the generated HTML. GitHub Pages continues publishing the repository's existing root files.

The verification workflow checks that the generated pages are current. It has read-only repository access; it does not write commits or change the hosting configuration.

## Shared structure

- `web/artefact-page.template.html`: the page structure and navigation.
- `web/reading-guides.json`: reading order, stage introductions, section explanations and glossary.
- `assets/reader.css`: the full-document reading layout.
- `scripts/build_artefacts.py`: Markdown rendering, link conversion, SQL explanations and preservation checks.

The generator does not write to `docs/`, `data/`, `README.md`, the overview page, or the original shared assets. Markdown links between artefacts are translated into the corresponding public HTML links without changing the source documents.

## Preserved web overviews

`web/original-web-overviews.json` retains the six previous HTML pages as exact strings, captured before this presentation update. Their main content is also available in the optional earlier-overview section on each new artefact page. The full document is the primary reading path. The earlier overview is a historical presentation and is not a second master document.

## Add a future artefact

Add its reviewed Markdown file and an entry to `web/reading-guides.json`, with an output URL, reading-order label and one explanation for each level-two section. Regenerate all pages so their navigation remains consistent. Do not mark a proposed design, synthetic example or planned test as a completed implementation.

## Preservation checks

Every build checks the complete rendered document text, section counts, table-cell text and order, exact code-block contents, full contents navigation, original-overview text, local links and anchor targets. Artefact 005 also checks the exact embedded SQL practice file. These checks use the current source documents; they do not freeze the project against future deliberate, reviewed changes.
