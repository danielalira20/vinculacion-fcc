"""Import a reviewed public backup, preserving provenance and rewriting local links.

This is a manual migration command. The regular build never fetches the network.
"""
import argparse
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
HOST = "vinculacion.cs.buap.mx"
ROUTES = {
    "inicio": "archivo/inicio/index.html",
    "967": "nosotros/index.html", "303": "certificaciones/oferta/index.html",
    "291": "certificaciones/proceso/index.html", "891": "certificaciones/precios/index.html",
    "88": "academias/coordinaciones/index.html", "100": "academias/cisco/index.html",
    "1852": "academias/aws/index.html", "98": "academias/oracle/index.html",
    "96": "academias/ec-council/index.html", "1015": "empresas/bolsa-de-trabajo/index.html",
    "865": "empresas/registro/index.html", "877": "empresas/vacantes/index.html",
    "127": "egresados/seguimiento/index.html", "151": "egresados/liberacion/index.html",
    "150": "egresados/registro/index.html", "152": "recursos/informacion/index.html",
    "177": "academias/presentacion/index.html", "53": "certificaciones/centro/index.html",
    "51": "egresados/comunidad/index.html", "131": "nosotros/labor/index.html",
    "129": "nosotros/coordinaciones/index.html", "1945": "recursos/inscripcion-aws/index.html",
    "1404": "academias/oracle/recursos/index.html", "745": "certificaciones/it-specialist/index.html",
    "772": "certificaciones/microsoft-office/index.html", "778": "certificaciones/adobe/index.html",
    "805": "certificaciones/autodesk/index.html", "2141": "archivo/cache/index.html",
    "86": "recursos/por-que-certificarme/index.html", "84": "recursos/que-buscan-las-empresas/index.html",
    "792": "academias/cisco/ruta/index.html", "991": "academias/cisco/cursos/index.html",
    "1924": "academias/aws/oferta/index.html",
}
HISTORICAL = {
    "contenido-891": "Los precios publicados corresponden a marzo de 2025. Consulta con Vinculación los importes actuales antes de realizar un pago.",
    "contenido-991": "Esta convocatoria corresponde a Primavera 2023. Consulta con la Academia Cisco las próximas fechas de inscripción.",
    "contenido-1404": "El cartel de esta publicación corresponde al registro de mayo y junio de 2025. Consulta la convocatoria actual con Oracle Academy.",
    "contenido-1924": "Esta oferta finalizó el 28 de febrero de 2026. Consulta con AWS Academy las próximas convocatorias.",
    "contenido-1945": "Esta guía conserva las fechas y condiciones publicadas en el sitio anterior. Confirma la convocatoria y los requisitos de tu periodo con AWS Academy.",
}
SAFE_TAGS = {"p", "h2", "h3", "h4", "h5", "h6", "strong", "b", "em", "i", "ul", "ol", "li", "a", "br", "figure", "figcaption", "img", "table", "thead", "tbody", "tr", "th", "td", "blockquote", "hr"}


def source_id(url):
    parsed = urlsplit(unquote(url))
    m = re.search(r"(?:p|page_id)=(\d+)", parsed.path + "?" + parsed.query)
    return m.group(1) if m else None


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def migrate(backup):
    pages = load_json(backup / "contenido-estructurado.json")
    manifest = load_json(backup / "inventario.json")
    records = {r["url"]: r for r in manifest["records"]}
    url_routes = {}
    for page in pages:
        key = page["id"].removeprefix("contenido-")
        page["path"] = ROUTES.get(key, f"archivo/{page['id']}/index.html")
        for url in [page["source_url"], *page["aliases"]]:
            url_routes[url] = page["path"]
    assets = ROOT / "src/assets/media"
    assets.mkdir(parents=True, exist_ok=True)
    asset_map, warnings = {}, []

    def copy_asset(url):
        if url in asset_map:
            return asset_map[url]
        record = records.get(url)
        if not record or not record.get("content_type", "").startswith(("image/", "application/pdf")):
            return None
        source = backup / record["local"]
        if not source.is_file():
            return None
        suffix = source.suffix.lower()
        name = hashlib.sha256(source.read_bytes()).hexdigest()[:16] + suffix
        shutil.copy2(source, assets / name)
        asset_map[url] = f"assets/media/{name}"
        return asset_map[url]

    def resolve(url, base):
        url = urljoin(base, html.unescape(url.strip()))
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https", "mailto", "tel"}:
            return None
        if parsed.hostname == HOST:
            if url in url_routes:
                return "@/" + url_routes[url]
            key = source_id(url)
            if key in ROUTES:
                return "@/" + ROUTES[key]
            if unquote(parsed.path).rstrip("/") in {"", "/index.html"}:
                return "@/index.html"
            local = copy_asset(url)
            if local:
                return "@/" + local
        return url

    output = []
    for page in pages:
        soup = BeautifulSoup((backup / page["html_original"]).read_text(errors="replace"), "html.parser")
        container = soup.select_one(".entry-content") or soup.select_one("#primary")
        if page["id"] == "inicio" or not container:
            body = "".join(f"<p>{html.escape(p.strip())}</p>" for p in page["text"].split("\n\n") if p.strip())
        else:
            fragment = BeautifulSoup(str(container), "html.parser")
            for unwanted in list(fragment.select("script, style, noscript, form, input, button, svg, .post-navigation, .comments-area, .sharedaddy, .nav-links")):
                unwanted.decompose()
            for comment in fragment.find_all(string=lambda text: isinstance(text, Comment)):
                comment.extract()
            # Iframes become explicit links: no tracking or external form requests on page load.
            for frame in list(fragment.find_all("iframe")):
                link = fragment.new_tag("a", href=urljoin(page["source_url"], frame.get("src", "")))
                link.string = "Abrir formulario" if "forms." in link["href"] else "Abrir recurso externo"
                frame.replace_with(link)
            for tag in list(fragment.find_all(True)):
                if tag.name not in SAFE_TAGS:
                    tag.unwrap()
                    continue
                attrs = dict(tag.attrs)
                tag.attrs = {}
                if tag.name == "a":
                    href = resolve(attrs.get("href", ""), page["source_url"])
                    if href:
                        tag["href"] = href
                        if not tag.get_text(strip=True) and not tag.find("img"):
                            tag.string = "Consultar recurso"
                    else:
                        tag.unwrap()
                elif tag.name == "img":
                    src = urljoin(page["source_url"], attrs.get("src", ""))
                    local = copy_asset(src)
                    if local:
                        tag["src"] = "@/" + local
                        tag["alt"] = attrs.get("alt", "") or f"Material publicado: {page['title'].split(' – ')[0]}"
                        tag["loading"] = "lazy"
                        tag["decoding"] = "async"
                    else:
                        warnings.append({"page": page["id"], "unavailable_image": src})
                        tag.decompose()
                elif tag.name in {"td", "th"}:
                    for attr in ("colspan", "rowspan"):
                        value = str(attrs.get(attr, ""))
                        if value.isdigit() and int(value) < 100:
                            tag[attr] = value
                    if tag.name == "th":
                        tag["scope"] = "col"
            # Old book plugin shortcodes have no downloadable source in the backup.
            for text in list(fragment.find_all(string=re.compile(r"\[/?3d-flip-book"))):
                replacement = re.sub(r"\[/?3d-flip-book[^\]]*\]", "", str(text)).strip()
                text.replace_with(replacement)
            body = str(fragment)
        images = []
        for image in page.get("images", []):
            local = copy_asset(image["url"])
            if local:
                images.append({**image, "asset": local})
        resources, seen = [], set()
        for ref in page["references"]:
            if ref["tag"] not in {"a", "iframe"}:
                continue
            href = resolve(ref["url"], page["source_url"])
            if href and href not in seen and href != "@/" + page["path"]:
                seen.add(href)
                label = ref.get("label", "").strip()
                if not label:
                    label = "Abrir formulario" if "forms." in href else "Ver recurso"
                    if "youtube" in href:
                        label = "Ver video"
                    if "canva" in href:
                        label = "Ver presentación"
                resources.append({"href": href, "label": label})
        title = page["title"].replace("\xa0", " ").split(" – Vinculación FCC")[0].strip()
        pending_books = page["id"] in {"contenido-1404", "contenido-1924"}
        output.append({
            "id": page["id"], "title": title, "path": page["path"],
            "section": page["path"].split("/")[0], "source_url": page["source_url"],
            "original_text": page["text"], "body": body,
            "images": images, "resources": resources,
            "notice": HISTORICAL.get(page["id"], ""), "pending_books": pending_books,
            "summary": re.sub(r"\s+", " ", page["text"])[:170].strip(),
        })
    # UI photographs and logos are original assets from the public site, never Pinterest screenshots.
    featured = {
        "hero": "https://vinculacion.cs.buap.mx/wp-content/uploads/2022/06/Egresados-revista-edu-1024x682.jpg",
        "community": "https://vinculacion.cs.buap.mx/wp-content/uploads/2022/06/oracle2-2016.jpg",
        "workshop": "https://vinculacion.cs.buap.mx/wp-content/uploads/2022/06/UnityMasAlla-2-400x420.jpg",
        "logo": "https://vinculacion.cs.buap.mx/wp-content/uploads/2023/08/logoBlanco-transparente-300x300.png",
    }
    featured = {name: copy_asset(url) for name, url in featured.items()}
    for url, record in records.items():
        if record.get("content_type", "").startswith("application/pdf"):
            copy_asset(url)
    content = ROOT / "src/content"
    content.mkdir(parents=True, exist_ok=True)
    (content / "pages.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    (content / "media.json").write_text(json.dumps(featured, ensure_ascii=False, indent=2), encoding="utf-8")
    (content / "asset-sources.json").write_text(json.dumps(asset_map, ensure_ascii=False, indent=2), encoding="utf-8")
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    for name in ("hallazgos.json", "transcripciones-verificadas.json", "formularios-revisados.md", "elementos-globales.json"):
        shutil.copy2(backup / name, docs / name)
    (docs / "migration-warnings.json").write_text(json.dumps(warnings, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Imported {len(output)} content records and {len(asset_map)} assets; {len(warnings)} unavailable image references recorded.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("backup", type=Path)
    migrate(parser.parse_args().backup.resolve())
