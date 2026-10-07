export function initializeNavigation() {
  const header = document.querySelector('.site-header');
  const toggle = header?.querySelector('.menu-toggle');
  const navigation = header?.querySelector('.site-nav');
  if (!toggle || !navigation) return;

  const dropdowns = [...navigation.querySelectorAll('.nav-dropdown')];
  const desktop = window.matchMedia('(min-width: 1021px)');
  const closeDropdowns = (except) => dropdowns.forEach((menu) => {
    if (menu !== except) menu.open = false;
  });
  header.classList.add('nav-enhanced');
  const setOpen = (open) => {
    header.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    if (!open) closeDropdowns();
  };
  // Native details keep the complete navigation usable without JavaScript.
  dropdowns.forEach((menu) => menu.addEventListener('toggle', () => {
    if (menu.open) closeDropdowns(menu);
  }));
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  header.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    const openDropdown = dropdowns.find((menu) => menu.open);
    if (openDropdown) {
      openDropdown.open = false;
      openDropdown.querySelector('summary').focus();
    } else if (toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!header.contains(event.target)) setOpen(false);
  });
  header.addEventListener('focusout', (event) => {
    // A null destination can occur during pointer focus transfer to summary.
    // Close only when focus actually moves outside the header.
    if (event.relatedTarget && !header.contains(event.relatedTarget)) setOpen(false);
  });
  desktop.addEventListener('change', () => setOpen(false));
}
