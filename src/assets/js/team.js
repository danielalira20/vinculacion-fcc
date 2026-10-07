/* Manual, native scrolling: every card remains accessible without JavaScript. */
export function initializeTeam() {
  document.querySelectorAll('[data-team-carousel]').forEach(carousel => {
    const track = carousel.querySelector('[data-team-track]');
    const cards = [...track.querySelectorAll('[data-team-card]')];
    const previous = carousel.querySelector('[data-team-prev]');
    const next = carousel.querySelector('[data-team-next]');
    const position = carousel.querySelector('[data-team-position]');
    const jumps = [...carousel.querySelectorAll('[data-team-index]')];
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let active = 0;
    let frame = 0;
    const offsets = () => cards.map(card => card.offsetLeft - cards[0].offsetLeft);
    const sync = () => {
      frame = 0;
      const starts = offsets();
      active = starts.reduce((closest, start, index) => Math.abs(start - track.scrollLeft) < Math.abs(starts[closest] - track.scrollLeft) ? index : closest, 0);
      previous.disabled = active === 0;
      next.disabled = active === cards.length - 1;
      position.textContent = `${String(active + 1).padStart(2, '0')} / ${String(cards.length).padStart(2, '0')}`;
      jumps.forEach((button, index) => button.setAttribute('aria-pressed', String(index === active)));
    };
    const go = index => {
      const target = Math.max(0, Math.min(cards.length - 1, index));
      track.scrollTo({ left: offsets()[target], behavior: reducedMotion.matches ? 'instant' : 'smooth' });
    };
    previous.addEventListener('click', () => go(active - 1));
    next.addEventListener('click', () => go(active + 1));
    jumps.forEach(button => button.addEventListener('click', () => go(Number(button.dataset.teamIndex))));
    track.addEventListener('keydown', event => {
      // Preserve arrow-key behavior inside links and other controls.
      if (event.target !== track) return;
      const target = { ArrowRight: active + 1, ArrowLeft: active - 1, Home: 0, End: cards.length - 1 }[event.key];
      if (target === undefined) return;
      event.preventDefault();
      go(target);
    });
    track.addEventListener('scroll', () => { if (!frame) frame = requestAnimationFrame(sync); }, { passive: true });
    new ResizeObserver(sync).observe(track);
    carousel.querySelector('[data-team-controls]').hidden = false;
    carousel.querySelector('[data-team-jumps]').hidden = false;
    sync();
  });
}
