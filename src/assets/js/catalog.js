export function normalizeText(value) {
  return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('es');
}

export function initializeCatalog() {
  const catalog = document.querySelector('[data-catalog]');
  if (!catalog) return;
  const search = catalog.querySelector('[data-catalog-search]');
  const buttons = [...catalog.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('[data-searchable]')];
  const count = document.querySelector('[data-catalog-count]');
  const empty = document.querySelector('[data-catalog-empty]');
  let category = 'all';

  const update = () => {
    const words = normalizeText(search.value.trim()).split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const text = normalizeText(card.dataset.search);
      const match = (category === 'all' || card.dataset.category === category)
        && words.every((word) => text.includes(word));
      card.hidden = !match;
      if (match) visible += 1;
    }
    count.textContent = `${visible} ${visible === 1 ? 'academia' : 'academias'}`;
    empty.hidden = visible !== 0;
  };

  search.addEventListener('input', update);
  for (const button of buttons) {
    button.addEventListener('click', () => {
      category = button.dataset.filter;
      for (const item of buttons) {
        const selected = item === button;
        item.classList.toggle('is-active', selected);
        item.setAttribute('aria-pressed', String(selected));
      }
      update();
    });
  }
}
