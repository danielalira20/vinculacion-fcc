// The native mailto links remain usable when JavaScript is unavailable.
export function emailDestinations(href, fallbackSubject = '') {
  const uri = new URL(href);
  if (uri.protocol !== 'mailto:') throw new TypeError('Expected a mailto link');
  const recipient = decodeURIComponent(uri.pathname);
  const subject = uri.searchParams.get('subject') || fallbackSubject;
  const body = uri.searchParams.get('body') || '';
  const gmail = new URL('https://mail.google.com/mail/');
  const outlook = new URL('https://outlook.office.com/mail/deeplink/compose');
  gmail.search = new URLSearchParams({view: 'cm', fs: '1', to: recipient, su: subject, body});
  outlook.search = new URLSearchParams({to: recipient, subject, body});
  for (const field of ['cc', 'bcc']) {
    const value = uri.searchParams.get(field);
    if (value) {
      gmail.searchParams.set(field, value);
      outlook.searchParams.set(field, value);
    }
  }
  return {recipient, gmail: gmail.href, outlook: outlook.href};
}

export function initializeEmail() {
  const dialog = document.querySelector('#email-dialog');
  if (!dialog?.showModal) return;
  const address = dialog.querySelector('#email-address');
  const status = dialog.querySelector('[data-email-status]');
  const copy = dialog.querySelector('[data-email-copy]');
  let trigger;
  let copying = false;
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[href^="mailto:"]');
    if (!link || link.hasAttribute('data-email-native') || event.defaultPrevented ||
        event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    let destinations;
    try {
      const context = link.closest('article')?.querySelector('h3')?.textContent.trim();
      const pageTitle = document.title.split(' · Vinculación FCC')[0];
      destinations = emailDestinations(link.href, `Consulta · ${context || pageTitle}`);
    } catch {
      return; // Preserve native navigation for an unparseable address.
    }
    if (!dialog.open) dialog.showModal();
    event.preventDefault();
    trigger = link;
    address.value = destinations.recipient;
    dialog.querySelector('[data-email-gmail]').href = destinations.gmail;
    dialog.querySelector('[data-email-outlook]').href = destinations.outlook;
    dialog.querySelector('[data-email-native]').href = link.href;
    status.textContent = '';
    copy.textContent = 'Copiar dirección';
    dialog.querySelector('[data-email-close]').focus();
  });
  dialog.querySelector('[data-email-close]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => trigger?.focus());
  copy.addEventListener('click', async () => {
    if (copying) return;
    copying = true;
    const recipient = address.value;
    try {
      await navigator.clipboard.writeText(recipient);
      if (dialog.open && address.value === recipient) {
        copy.textContent = 'Dirección copiada';
        status.textContent = 'Ya puedes pegarla en tu correo.';
      }
    } catch {
      if (dialog.open && address.value === recipient) {
        address.focus();
        address.select();
        status.textContent = 'Seleccionamos la dirección. Cópiala con el menú de tu dispositivo.';
      }
    } finally {
      copying = false;
    }
  });
}
