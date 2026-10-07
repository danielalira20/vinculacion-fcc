export function initializeMotion() {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (preference.matches || !('IntersectionObserver' in window)) return;
  const targets = [...document.querySelectorAll('[data-reveal]')];
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-visible');
        observer.unobserve(entry.target);
      }
    }
  }, { threshold: 0.05 });

  for (const target of targets) {
    // Elements already visible are never hidden while the module initializes.
    if (target.getBoundingClientRect().top < window.innerHeight) continue;
    target.classList.add('reveal-ready');
    observer.observe(target);
  }
  preference.addEventListener('change', (event) => {
    if (event.matches) {
      observer.disconnect();
      for (const target of targets) target.classList.remove('reveal-ready');
    }
  });
}
