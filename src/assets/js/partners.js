/** Enhance the original logo directory; all organization cards exist without JS. */
export function initializePartners() {
  document.querySelectorAll('[data-partner-network]').forEach(network => {
    const links = [...network.querySelectorAll('.partner-logo')];
    const panels = [...network.querySelectorAll('.partner-panel')];
    const select = hash => {
      const selected = panels.find(panel => `#${panel.id}` === hash);
      if (!selected) return false;
      panels.forEach(panel => { panel.hidden = panel !== selected; });
      links.forEach(link => {
        if (link.hash === hash) link.setAttribute('aria-current', 'true');
        else link.removeAttribute('aria-current');
      });
      return true;
    };
    network.classList.add('partner-ready');
    if (!select(window.location.hash)) select('#empresa-cisco');
    links.forEach(link => link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
      if (!select(link.hash)) return;
      event.preventDefault();
      window.history.replaceState(null, '', link.hash);
    }));
    window.addEventListener('hashchange', () => select(window.location.hash));
  });
}
