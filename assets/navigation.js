// Keep fragment navigation clear of the responsive sticky header.
(() => {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const updateHeaderOffset = () => {
    const offset = Math.ceil(header.getBoundingClientRect().height) + 16;
    document.documentElement.style.setProperty('--header-offset', `${offset}px`);
  };

  updateHeaderOffset();
  if ('ResizeObserver' in window) {
    new ResizeObserver(updateHeaderOffset).observe(header);
  } else {
    window.addEventListener('resize', updateHeaderOffset);
  }

  // Account for the measured header on direct links into a section.
  window.addEventListener('load', () => {
    updateHeaderOffset();
    if (!window.location.hash) return;
    let target;
    try {
      target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    } catch {
      return;
    }
    if (target) target.scrollIntoView({ block: 'start', behavior: 'instant' });
  }, { once: true });
})();
