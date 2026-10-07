export function initializeCommunity() {
  document.querySelectorAll('[data-facebook-frame]').forEach((frame) => {
    const container = frame.parentElement;
    let timer;
    const resize = () => {
      const width = Math.max(180, Math.min(500, Math.floor(container.getBoundingClientRect().width)));
      const source = new URL(frame.src);
      if (source.searchParams.get('width') === String(width)) return;
      source.searchParams.set('width', String(width));
      frame.src = source.href;
    };
    // The Page Plugin adapts on load, so reconfigure only when its width changes.
    resize();
    if ('ResizeObserver' in window) {
      const observer = new ResizeObserver(() => {
        clearTimeout(timer);
        timer = setTimeout(resize, 200);
      });
      observer.observe(container);
    } else {
      window.addEventListener('resize', resize);
    }
  });
}
