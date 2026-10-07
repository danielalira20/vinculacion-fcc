// Only a deliberate click creates a player. Removing it also stops its audio.
export function initializeAcademyVideos() {
  let activeVideo = null;
  for (const video of document.querySelectorAll('[data-inline-video]')) {
    const fallback = video.querySelector('[data-video-launch]');
    const screen = video.querySelector('[data-video-screen]');
    const controls = video.querySelector('[data-video-controls]');
    const close = video.querySelector('[data-video-close]');
    const status = video.querySelector('[data-video-status]');
    const launch = document.createElement('button');
    launch.type = 'button';
    launch.className = fallback.className;
    launch.setAttribute('aria-label', fallback.getAttribute('aria-label'));
    launch.setAttribute('aria-controls', screen.id);
    launch.append(...fallback.childNodes);
    fallback.replaceWith(launch);

    const stop = (restoreFocus = false) => {
      screen.querySelector('iframe')?.remove();
      launch.hidden = false;
      controls.hidden = true;
      video.classList.remove('is-playing');
      status.textContent = '';
      if (activeVideo?.element === video) activeVideo = null;
      if (restoreFocus) launch.focus({ preventScroll: true });
    };

    launch.addEventListener('click', () => {
      activeVideo?.stop();
      const src = new URL(video.dataset.videoSrc);
      if (src.origin !== 'https://www.youtube.com'
          || !/^\/embed\/[A-Za-z0-9_-]{11}$/.test(src.pathname)) return;
      // Autoplay is scoped to this user-requested action; initial page load is silent.
      src.searchParams.set('autoplay', '1');
      const player = document.createElement('iframe');
      player.src = src.href;
      player.title = video.dataset.videoTitle;
      player.loading = 'eager';
      player.referrerPolicy = 'strict-origin-when-cross-origin';
      player.allow = 'autoplay; fullscreen; picture-in-picture; encrypted-media';
      player.allowFullscreen = true;
      launch.hidden = true;
      controls.hidden = false;
      video.classList.add('is-playing');
      screen.append(player);
      activeVideo = { element: video, stop };
      status.textContent = `${video.dataset.videoTitle}. Reproductor abierto en esta tarjeta.`;
      close.focus({ preventScroll: true });
    });
    close.addEventListener('click', () => stop(true));
    video.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && video.classList.contains('is-playing')) {
        event.preventDefault();
        stop(true);
      }
    });
    video.closest('[data-searchable]')?.addEventListener('catalog:hide', () => stop());
  }
}
