import { normalizeText } from './catalog.js';

export function initializeSearch() {
  const container = document.querySelector('[data-site-search]');
  if (!container) return;
  const form = container.querySelector('form');
  const input = form.querySelector('input');
  const status = container.querySelector('[data-search-status]');
  const results = container.querySelector('[data-search-results]');
  const root = new URL(document.body.dataset.root, document.baseURI);
  let indexPromise;
  let requestVersion = 0;

  const loadIndex = () => {
    indexPromise ??= fetch(new URL('assets/search-index.json', root))
      .then((response) => {
        if (!response.ok) throw new Error('Search index unavailable');
        return response.json();
      })
      .catch((error) => { indexPromise = undefined; throw error; });
    return indexPromise;
  };

  const search = async (query) => {
    const version = ++requestVersion;
    results.replaceChildren();
    const words = normalizeText(query).split(/\s+/).filter(Boolean);
    if (!words.length) {
      status.textContent = 'Escribe una palabra para comenzar.';
      return;
    }
    status.textContent = 'Buscando…';
    try {
      const index = await loadIndex();
      if (version !== requestVersion) return;
      const matches = index.filter((page) => {
        const text = normalizeText(`${page.title} ${page.text}`);
        return words.every((word) => text.includes(word));
      }).sort((a, b) => {
        const score = (page) => words.filter((word) => normalizeText(page.title).includes(word)).length;
        return score(b) - score(a);
      });
      status.textContent = `${matches.length} ${matches.length === 1 ? 'resultado' : 'resultados'} para “${query}”`;
      for (const page of matches) {
        const article = document.createElement('article');
        article.className = 'search-result';
        const category = document.createElement('small');
        category.textContent = page.section;
        const heading = document.createElement('h2');
        const link = document.createElement('a');
        link.href = new URL(page.path, root).href;
        link.textContent = page.title;
        heading.append(link);
        const summary = document.createElement('p');
        summary.textContent = page.summary;
        article.append(category, heading, summary);
        results.append(article);
      }
      if (!matches.length) status.textContent += '. Prueba con otra palabra.';
    } catch {
      if (version !== requestVersion) return;
      status.textContent = 'No pudimos cargar la búsqueda. Intenta de nuevo o consulta la sección Recursos.';
    }
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const query = input.value.trim();
    const current = new URL(location.href);
    current.searchParams.set('q', query);
    history.replaceState(null, '', current);
    search(query);
  });
  const initialQuery = new URLSearchParams(location.search).get('q');
  if (initialQuery) {
    input.value = initialQuery;
    search(initialQuery);
  }
}
