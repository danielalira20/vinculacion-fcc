/* All material is visible without JavaScript. Enhance only local exploration. */
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

export function initializeLearning() {
  document.querySelectorAll('[data-learning-catalog]').forEach(catalog => {
    const controls = catalog.querySelector('[data-catalog-controls]');
    const input = controls.querySelector('input');
    const filters = [...controls.querySelectorAll('[data-learning-filter]')];
    const courses = [...catalog.querySelectorAll('[data-learning-course]')];
    const count = catalog.querySelector('[data-learning-count]');
    const empty = catalog.querySelector('[data-learning-empty]');
    let selected = 'all';
    const update = () => {
      const query = normalize(input.value.trim());
      let visible = 0;
      courses.forEach(course => {
        const matches = (selected === 'all' || course.dataset.courseGroup === selected)
          && normalize(course.querySelector('h3').textContent).includes(query);
        course.hidden = !matches;
        if (matches) visible += 1;
      });
      count.textContent = `${visible} ${visible === 1 ? 'curso' : 'cursos'} de ${courses.length}`;
      empty.hidden = visible > 0;
    };
    filters.forEach(button => button.addEventListener('click', () => {
      selected = button.dataset.learningFilter;
      filters.forEach(filter => filter.setAttribute('aria-pressed', String(filter === button)));
      update();
    }));
    input.addEventListener('input', update);
    controls.hidden = false;
  });

  document.querySelectorAll('[data-learning-panels]').forEach(workbench => {
    const controls = workbench.querySelector('[data-panel-controls]');
    const buttons = [...controls.querySelectorAll('[data-panel-target]')];
    const panels = [...workbench.querySelectorAll('[data-learning-panel]')];
    controls.setAttribute('role', 'tablist');
    const activate = index => {
      buttons.forEach((button, position) => {
        const selected = index === position;
        button.setAttribute('aria-selected', String(selected));
        button.tabIndex = selected ? 0 : -1;
      });
      panels.forEach(panel => { panel.hidden = panel.id !== buttons[index].dataset.panelTarget; });
    };
    buttons.forEach((button, index) => {
      button.id = `${button.dataset.panelTarget}-tab`;
      button.setAttribute('role', 'tab');
      button.setAttribute('aria-controls', button.dataset.panelTarget);
      button.addEventListener('click', () => activate(index));
      button.addEventListener('keydown', event => {
        const direction = { ArrowRight: 1, ArrowLeft: -1, Home: -index, End: buttons.length - 1 - index }[event.key];
        if (direction === undefined) return;
        event.preventDefault();
        const next = (index + direction + buttons.length) % buttons.length;
        activate(next);
        buttons[next].focus();
      });
    });
    panels.forEach(panel => {
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', `${panel.id}-tab`);
      panel.tabIndex = 0;
    });
    activate(0);
    controls.hidden = false;
  });
}
