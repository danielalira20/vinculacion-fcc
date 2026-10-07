"""Render supported media from migrated URLs without depending on WordPress."""
import html
import re
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit

UNAVAILABLE_VIDEOS = {
    "7sViLbTvDKk": "El video de presentación ya no está disponible en YouTube.",
    "Ar2L2i2A0aY": "El video de presentación está privado en YouTube.",
}
PDF_PREVIEWS = {"@/assets/media/a68c6efe6ff18ca9.pdf": ("sipago-page", 18)}


def embed_spec(href):
    href = html.unescape(href)
    parsed = urlsplit(href)
    query = parse_qs(parsed.query)
    if parsed.scheme == "https" and parsed.hostname in {"www.youtube.com", "www.youtube-nocookie.com"}:
        match = re.fullmatch(r"/embed/([A-Za-z0-9_-]{11})", parsed.path)
        if match:
            video = match.group(1)
            params = {"hl": "es", "playsinline": "1"}
            for name in ("start", "list"):
                value = query.get(name, [""])[0]
                if value and re.fullmatch(r"[A-Za-z0-9_-]+", value):
                    params[name] = value
            return {"key": video, "kind": "video", "src": f"https://www.youtube.com/embed/{video}?{urlencode(params)}", "link": f"https://www.youtube.com/watch?v={video}", "action": "Ver en YouTube"}
    if parsed.scheme == "https" and parsed.hostname == "www.canva.com":
        match = re.fullmatch(r"/design/([A-Za-z0-9_-]+)/([A-Za-z0-9_-]+)/view", parsed.path)
        if match:
            return {"key": match.group(1), "kind": "presentation", "src": f"https://www.canva.com{parsed.path}?embed", "link": f"https://www.canva.com{parsed.path}", "action": "Abrir presentación en Canva"}
    if parsed.scheme == "https" and parsed.hostname in {"forms.office.com", "forms.cloud.microsoft"} and parsed.path.lower() == "/pages/responsepage.aspx":
        form_id = query.get("id", [""])[0]
        if re.fullmatch(r"[A-Za-z0-9_-]+", form_id):
            base = f"https://{parsed.hostname}/Pages/ResponsePage.aspx"
            return {"key": form_id, "kind": "form", "src": base + "?" + urlencode({"id": form_id, "embed": "true"}), "link": base + "?" + urlencode({"id": form_id}), "action": "Abrir formulario en una ventana"}
    if re.fullmatch(r"@/assets/media/[a-f0-9]{16}\.pdf", href):
        return {"key": href, "kind": "pdf", "src": href, "link": href, "action": "Abrir documento PDF"}
    return None


def render_embed(href, title):
    spec = embed_spec(href)
    if not spec:
        raise ValueError(f"Unsupported embedded resource: {href}")
    if spec["key"] in UNAVAILABLE_VIDEOS:
        return (f'<div class="resource-embed embed-unavailable"><div class="embed-heading"><strong>{html.escape(title)}</strong></div>'
                f'<div class="media-unavailable"><span aria-hidden="true">{(Path(__file__).resolve().parents[1] / "src/assets/icons/play.svg").read_text()}</span><p>{html.escape(UNAVAILABLE_VIDEOS[spec["key"]])}</p>'
                '<a href="mailto:vinculacion.fcc@correo.buap.mx">Consultar el material con Vinculación</a></div></div>')
    if spec["key"] in PDF_PREVIEWS:
        prefix, count = PDF_PREVIEWS[spec["key"]]
        pages = "".join(f'<figure><figcaption>Página {n} de {count} · Pulsa para ampliar</figcaption><a href="@/assets/media/{prefix}-{n:02d}.jpg" target="_blank" rel="noopener" aria-label="Ampliar página {n}"><img src="@/assets/media/{prefix}-{n:02d}.jpg" alt="{html.escape(title, quote=True)} · Página {n} de {count}" loading="lazy" width="910" height="1287"></a></figure>' for n in range(1, count + 1))
        return (f'<div class="resource-embed embed-pdf"><div class="embed-heading"><strong>{html.escape(title)}</strong></div>'
                f'<div class="pdf-pages" role="region" tabindex="0" aria-label="{html.escape(title, quote=True)} · {count} páginas">{pages}</div>'
                f'<div class="embed-caption"><a href="{spec["link"]}" target="_blank" rel="noopener">Abrir o descargar el PDF completo</a></div></div>')
    attributes = ' loading="lazy" referrerpolicy="strict-origin-when-cross-origin"'
    if spec["kind"] in {"video", "presentation"}:
        attributes += ' allow="fullscreen; picture-in-picture; encrypted-media" allowfullscreen'
    escape = html.escape
    return (f'<div class="resource-embed embed-{spec["kind"]}">'
            f'<div class="embed-heading"><strong>{escape(title)}</strong></div>'
            f'<div class="embed-viewport"><iframe src="{escape(spec["src"], quote=True)}" title="{escape(title, quote=True)}"{attributes}></iframe></div>'
            f'<div class="embed-caption"><a href="{escape(spec["link"], quote=True)}" target="_blank" rel="noopener">{escape(spec["action"])}</a></div></div>')


def prepare_page(page, titles, page_titles):
    """Restore embeds in their original position and remove duplicate resource links."""
    result = dict(page)
    seen = set()

    def title_for(spec):
        default = {"video": "Video", "presentation": "Presentación", "form": "Formulario", "pdf": "Documento PDF"}[spec["kind"]]
        return titles.get(spec["key"], f"{default} · {page['title']}")

    def replace_anchor(match):
        href, content = html.unescape(match.group(1)), match.group(2)
        spec = embed_spec(href)
        plain = html.unescape(re.sub(r"<[^>]+>", "", content)).strip()
        if spec and spec["kind"] != "pdf" and not re.search(r"<img\b", content):
            if spec["key"] in seen:
                return ""
            seen.add(spec["key"])
            return render_embed(href, title_for(spec))
        if plain in {"Abrir recurso externo", "Consultar recurso", "Ver recurso"}:
            if href.startswith("@/"):
                label = page_titles.get(href[2:], "Consultar información")
            elif href.startswith("mailto:"):
                label = href.removeprefix("mailto:")
            else:
                label = "Consultar " + (urlsplit(href).hostname or "información")
            return f'<a href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        return match.group(0)

    result["body"] = re.sub(r'<a href="([^"]+)">(.*?)</a>', replace_anchor, page["body"], flags=re.S)
    resources, extras = [], []
    for resource in page["resources"]:
        href = resource["href"]
        # An invalid legacy email URL is replaced with the published address.
        if href == "https://vinculacion.cs.buap.mx/bolsadetrabajo.fcc@correo.buap.mx.html":
            href = "mailto:bolsadetrabajo.fcc@correo.buap.mx"
        spec = embed_spec(href)
        if spec:
            if spec["key"] not in seen:
                seen.add(spec["key"])
                extras.append(render_embed(href, title_for(spec)))
            continue
        label = resource["label"]
        if label in {"Ver recurso", "Consultar recurso", "Abrir recurso externo"}:
            label = page_titles.get(href[2:], "Consultar información") if href.startswith("@/") else href.removeprefix("mailto:") if href.startswith("mailto:") else "Consultar " + (urlsplit(href).hostname or "información")
        resources.append({"href": href, "label": label})
    result["body"] += "".join(extras)
    # Preserve the original record on disk; the public copy names its own portal.
    for field in ("body", "original_text"):
        result[field] = result[field].replace("Portal oficial vinculacion.cs.buap.mx", "Portal de Vinculación FCC")
    result["resources"] = resources
    return result
