/* Native details work without JavaScript; the group control is an enhancement. */
export function initializeProcesses() {
  for (const flow of document.querySelectorAll('[data-process]')) {
    const toggle = flow.querySelector('[data-process-toggle]');
    const details = [...flow.querySelectorAll('.process-stop details')];
    if (!toggle || !details.length) continue;
    const update = () => {
      const allOpen = details.every(detail => detail.open);
      toggle.setAttribute('aria-expanded', String(allOpen));
      toggle.querySelector('span').textContent = allOpen ? 'Contraer detalles' : 'Desplegar detalles';
    };
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
      const open = !details.every(detail => detail.open);
      for (const detail of details) detail.open = open;
      update();
    });
    for (const detail of details) detail.addEventListener('toggle', update);
    update();
  }
}
