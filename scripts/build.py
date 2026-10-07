"""Render a portable static website. No network requests, secrets or server required."""
import json
import os
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup
from embeds import prepare_page, render_embed
from presentation import prepare_presentation

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"
DIST = ROOT / "dist"


def load(name):
    return json.loads((SOURCE / "content" / name).read_text(encoding="utf-8"))


def relative(target, current):
    return os.path.relpath(target, Path(current).parent).replace(os.sep, "/")


def build():
    site, pages, media = load("site.json"), load("pages.json"), load("media.json")
    experiences = load("experiences.json")
    media_titles = load("embedded-resources.json")
    processes, employers = load("processes.json"), load("employers.json")
    page_titles = {p["path"]: p["title"] for p in pages}
    pages = [prepare_presentation(prepare_page(page, media_titles, page_titles), processes) for page in pages]
    for page in pages:
        if page["path"] == "academias/coordinaciones/index.html":
            page["title"] = "Coordinaciones de Academias"
    coordinations = load("coordinations.json")
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SOURCE / "assets", DIST / "assets")
    env = Environment(loader=FileSystemLoader(SOURCE / "templates"), autoescape=select_autoescape(["html"]), undefined=StrictUndefined)
    env.globals["icon"] = lambda name: Markup((SOURCE / "assets/icons" / f"{name}.svg").read_text())
    env.globals["embedded_media"] = lambda href, title: Markup(render_embed(href, title))
    written = set()

    def render(path, template, **context):
        if path in written:
            raise ValueError(f"Duplicate output: {path}")
        written.add(path)
        url = lambda target: relative(target, path)
        flow_count = 0
        def local_body(body):
            def process(match):
                nonlocal flow_count
                flow_count += 1
                key = match.group(1)
                return env.get_template("components/process-flow.html").render(flow=processes[key], flow_id=f"{key}-{flow_count}", url=url)
            body = re.sub(r'<!-- process-flow:([a-z]+) -->', process, body)
            return Markup(re.sub(r'@/([^"\s<>]+)', lambda m: url(m.group(1)), body))
        html = env.get_template(template).render(site=site, pages=pages, media=media, experiences=experiences, coordinations=coordinations, processes=processes, url=url, local_body=local_body, current_path=path, **context)
        target = DIST / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    render("index.html", "pages/home.html", title="Vinculación FCC · BUAP", active="inicio", description=site["description"])
    for landing in site["landings"]:
        render(landing["path"], "pages/landing.html", title=landing["title"], active=landing["key"], description=landing["description"], landing=landing)
    for page in pages:
        active = page["section"] if page["section"] != "archivo" else "recursos"
        experience = experiences["academies"].get(page["path"])
        employer = employers.get(page["path"])
        template = "pages/employer.html" if employer else "pages/coordinations.html" if page["path"] == "academias/coordinaciones/index.html" else "pages/academy.html" if experience else "pages/about.html" if page["path"] == "nosotros/index.html" else "pages/article.html"
        render(page["path"], template, title=page["title"], active=active, description=page["summary"] or page["title"], page=page, experience=experience, employer=employer)
    render("buscar/index.html", "pages/search.html", title="Buscar", active="", description="Encuentra academias, certificaciones, trámites y recursos de Vinculación FCC.")
    search_index = [
        {"title": p["title"], "path": p["path"], "section": p["section"],
         "text": p["original_text"] + "\n" + "\n".join(image["text"] for image in p["images"] if image["text_status"] == "revisado contra imagen"),
         "summary": p["summary"]}
        for p in pages if p["id"] != "contenido-2141"
    ]
    search_index += [{"title": l["title"], "path": l["path"], "section": l["key"], "text": l["description"], "summary": l["description"]} for l in site["landings"]]
    (DIST / "assets/search-index.json").write_text(json.dumps(search_index, ensure_ascii=False), encoding="utf-8")
    (DIST / "robots.txt").write_text("# Preview: enable indexing only after editorial approval.\nUser-agent: *\nDisallow: /\n", encoding="utf-8")
    aliases = [{"source": p["source_url"], "target": p["path"]} for p in pages]
    (DIST / "redirect-map.json").write_text(json.dumps(aliases, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built {len(written)} HTML pages in {DIST}")


if __name__ == "__main__":
    build()
