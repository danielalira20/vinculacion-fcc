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

export function initializePromoDialog() {
  const dialog = document.querySelector('[data-promo-dialog]');
  if (!dialog?.showModal) return;
  const key = dialog.dataset.promoKey;
  const forced = new URLSearchParams(location.search).has('aviso');
  if (seen(key) && !forced) return;

  const close = () => dialog.close();
  dialog.querySelectorAll('[data-promo-close]').forEach((button) => button.addEventListener('click', close));
  dialog.querySelector('[data-promo-go]')?.addEventListener('click', () => remember(key));
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
      .filter((control) => !control.disabled && control.getClientRects().length);
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
    dialog.querySelector('[data-promo-go]')?.focus();
  }, forced ? 0 : OPEN_DELAY);
}
