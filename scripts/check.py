"""Check generated pages, local destinations, accessibility basics and asset imports."""
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from embeds import embed_spec
from presentation import EMOJI

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references, self.ids, self.errors = [], [], []
        self.h1_count = 0
        self.has_main = False
        self.lang = None
        self.embeds = Counter()

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == "html":
            self.lang = attributes.get("lang")
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.has_main = True
        if attributes.get("id"):
            self.ids.append(attributes["id"])
        if tag == "img" and "alt" not in attributes:
            self.errors.append("Image without alt attribute")
        if "pdf-pages" in attributes.get("class", "").split():
            self.embeds["pdf"] += 1
        for name in attributes:
            if name.startswith("on"):
                self.errors.append("Inline event handler in generated content")
        if tag == "iframe":
            src = attributes.get("src", "")
            parsed = urlsplit(src)
            spec = embed_spec(src)
            if not spec and not (not parsed.scheme and not parsed.netloc and parsed.path.endswith(".pdf")):
                self.errors.append("Unsupported embedded resource")
            if not attributes.get("title") or attributes.get("loading") != "lazy":
                self.errors.append("Embedded resource without accessible title or lazy loading")
            if attributes.get("referrerpolicy") != "strict-origin-when-cross-origin":
                self.errors.append("Embedded resource without provider-compatible referrer policy")
            self.embeds[spec["kind"] if spec else "pdf"] += 1
        for name in ("href", "src"):
            if attributes.get(name):
                self.references.append(attributes[name])


def check():
    if not DIST.is_dir():
        raise SystemExit("Run scripts/build.py before scripts/check.py")
    documents, errors = {}, []
    for path in DIST.rglob("*.html"):
        document = Document()
        html = path.read_text(encoding="utf-8")
        document.feed(html)
        if EMOJI.search(html):
            document.errors.append("Emoji exposed in the public interface")
        if any(label in html for label in ("Fuente de esta información", "Fuentes de información", "Consultar publicación original", "Abrir recurso externo", "Ver recurso externo", "vinculacion.cs.buap.mx")):
            document.errors.append("Legacy provenance or external-resource placeholder exposed in the interface")
        documents[path.resolve()] = document
        label = str(path.relative_to(DIST))
        errors.extend(f"{label}: {error}" for error in document.errors)
        if document.h1_count != 1 or not document.has_main or document.lang != "es-MX":
            errors.append(f"{label}: page landmarks, language or primary heading missing")
        if any(count > 1 for count in Counter(document.ids).values()):
            errors.append(f"{label}: duplicate HTML IDs")
    reference_count = 0
    for path, document in documents.items():
        for reference in document.references:
            parsed = urlsplit(reference)
            if parsed.hostname == "vinculacion.cs.buap.mx":
                errors.append(f"{path.name}: destination still depends on retired website")
            if parsed.scheme:
                if parsed.scheme not in {"https", "http", "mailto", "tel"}:
                    errors.append(f"{path.name}: unsupported URL scheme: {parsed.scheme}")
                continue
            if parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            reference_count += 1
            if not target.is_relative_to(DIST.resolve()) or not target.is_file():
                errors.append(f"{path.relative_to(DIST.resolve())}: missing destination {reference}")
            elif parsed.fragment and target in documents and unquote(parsed.fragment) not in documents[target].ids:
                errors.append(f"{path.name}: missing fragment {reference}")
    for path in (DIST / "assets").rglob("*"):
        if path.suffix not in {".css", ".js"}:
            continue
        text = path.read_text()
        pattern = r"(?:url\(|from\s+)[\"']?([^\"'\s)]+)"
        for reference in re.findall(pattern, text):
            if reference.startswith(("https:", "data:", "#")):
                continue
            if not (path.parent / reference).is_file():
                errors.append(f"{path.name}: missing stylesheet/module asset {reference}")
    pages = json.loads((ROOT / "src/content/pages.json").read_text())
    processes = json.loads((ROOT / "src/content/processes.json").read_text())
    for path, document in documents.items():
        for reference in document.references:
            if any(urlsplit(reference).path.endswith(flow["asset"]) for flow in processes.values()):
                errors.append(f"{path.name}: process still rendered as a raster image")
    for page in pages:
        if (DIST / page["path"]).resolve() not in documents:
            errors.append(f"Missing recovered page {page['id']}")
    search = json.loads((DIST / "assets/search-index.json").read_text())
    if not any("liberaci" in p["title"].lower() for p in search):
        errors.append("Graduation release process missing from search index")
    if errors:
        raise SystemExit("\n".join(errors))
    embeds = sum((document.embeds for document in documents.values()), Counter())
    print(f"PASS: {len(documents)} pages, {reference_count} local references, {len(pages)} recovered records, embeds {dict(embeds)}, CSS/JS imports and HTML basics.")


if __name__ == "__main__":
    check()
