/** Filter educational topics without changing their official source links. */
const root = document.querySelector('[data-ed-catalog]');
if (root) {
  const search = root.querySelector('[data-ed-search]');
  const buttons = Array.from(root.querySelectorAll('[data-ed-filter]'));
  const cards = Array.from(document.querySelectorAll('[data-ed-card]'));
  const count = document.querySelector('[data-ed-count]');
  const empty = document.querySelector('[data-ed-empty]');
  let category = 'todos';
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const update = () => {
    const query = normalize(search.value.trim());
    let visible = 0;
    for (const card of cards) {
      const match = (category === 'todos' || card.dataset.category === category) && normalize(card.dataset.search).includes(query);
      card.hidden = !match;
      if (match) visible += 1;
    }
    count.textContent = `${visible} ${visible === 1 ? 'área para explorar' : 'áreas para explorar'}`;
    empty.hidden = visible !== 0;
  };
  search.addEventListener('input', update);
  buttons.forEach(button => button.addEventListener('click', () => {
    category = button.dataset.edFilter;
    for (const item of buttons) {
      const selected = item === button;
      item.classList.toggle('is-active', selected);
      item.setAttribute('aria-pressed', String(selected));
    }
    update();
  }));
}
