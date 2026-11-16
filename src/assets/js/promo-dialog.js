// Home announcement: opens once per browser session and never blocks the page without JavaScript.
const OPEN_DELAY = 700;

function seen(key) {
  try {
    return sessionStorage.getItem(key) === '1';
  } catch {
    return false;
  }
}

function remember(key) {
  try {
    sessionStorage.setItem(key, '1');
  } catch {
    // Storage can be blocked (private mode); the dialog simply may appear again.
  }
}

// One tab per offer. The user changes slides; nothing advances on its own.
function initializeTabs(dialog) {
  const tabs = [...dialog.querySelectorAll('[data-promo-tabs] [role="tab"]')];
  const slides = [...dialog.querySelectorAll('[data-promo-slide]')];
  if (tabs.length < 2) return;
  let current = 0;

  const select = (index, { focus = false } = {}) => {
    current = (index + tabs.length) % tabs.length;
    tabs.forEach((tab, position) => {
      const active = position === current;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      slides[position].toggleAttribute('data-inactive', !active);
      slides[position].inert = !active;
    });
    if (focus) tabs[current].focus();
  };

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => select(index));
    tab.addEventListener('keydown', (event) => {
      const moves = { ArrowRight: 1, ArrowLeft: -1 };
      if (event.key in moves) {
        event.preventDefault();
        select(current + moves[event.key], { focus: true });
      } else if (event.key === 'Home' || event.key === 'End') {
        event.preventDefault();
        select(event.key === 'Home' ? 0 : tabs.length - 1, { focus: true });
      }
    });
  });

  // Horizontal swipe on touch screens moves to the neighbouring offer.
  let start = null;
  dialog.addEventListener('pointerdown', (event) => {
    if (event.pointerType === 'mouse' || event.target.closest('a, button')) return;
    start = { x: event.clientX, y: event.clientY };
  });
  dialog.addEventListener('pointerup', (event) => {
    if (!start) return;
    const dx = event.clientX - start.x;
    const dy = event.clientY - start.y;
    start = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) select(current + (dx < 0 ? 1 : -1));
  });
  dialog.addEventListener('pointercancel', () => { start = null; });
}

export function initializePromoDialog() {
  const dialog = document.querySelector('[data-promo-dialog]');
  if (!dialog?.showModal) return;
  const key = dialog.dataset.promoKey;
  const forced = new URLSearchParams(location.search).has('aviso');
  if (seen(key) && !forced) return;

  initializeTabs(dialog);
  const close = () => dialog.close();
  dialog.querySelectorAll('[data-promo-close]').forEach((button) => button.addEventListener('click', close));
  dialog.querySelectorAll('[data-promo-go]').forEach((link) => link.addEventListener('click', () => remember(key)));
  dialog.addEventListener('close', () => {
    remember(key);
    document.documentElement.classList.remove('promo-open');
  });
  // Clicking the dimmed backdrop (outside the card) also dismisses.
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) close();
  });
  dialog.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') return;
    const controls = [...dialog.querySelectorAll('button, a[href]')]
      .filter((control) => !control.disabled && !control.closest('[data-inactive]') && control.getClientRects().length);
    const first = controls[0];
    const last = controls.at(-1);
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  window.setTimeout(() => {
    if (document.querySelector('dialog[open]')) return; // Never stack over another open dialog.
    dialog.showModal();
    document.documentElement.classList.add('promo-open');
    dialog.querySelector('[data-promo-slide]:not([data-inactive]) [data-promo-go]')?.focus();
  }, forced ? 0 : OPEN_DELAY);
}
