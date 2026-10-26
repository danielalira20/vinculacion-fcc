"""Render a portable static website. No network requests, secrets or server required."""
import json
import hashlib
import os
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup
from embeds import embed_spec, prepare_page, render_embed
from presentation import prepare_presentation
from community import facebook_timeline_src

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
    learning_data = load("learning.json")
    cisco = load("cisco.json")
    media_titles = load("embedded-resources.json")
    processes, employers = load("processes.json"), load("employers.json")
    alumni = load("alumni.json")
    certifications = load("certifications.json")
    education = load("continuing-education.json")
    partners = load("partners.json")
    about_directory = load("about-directory.json")
    page_titles = {p["path"]: p["title"] for p in pages}
    pages = [prepare_presentation(prepare_page(page, media_titles, page_titles), processes) for page in pages]
    for page in pages:
        if page["path"] == "academias/coordinaciones/index.html":
            page["title"] = "Coordinaciones de Academias"
        elif page["path"] == "egresados/seguimiento/index.html":
            page["title"] = "Seguimiento a Egresados"
    coordinations = load("coordinations.json")
    department = load("department-team.json")
    library = load("resource-library.json")
    academy_previews = {}
    for academy in coordinations["academies"]:
        spec = embed_spec(academy["video"])
        if not spec or spec["kind"] != "video":
            raise ValueError(f"Unsupported academy video: {academy['path']}")
        academy_previews[academy["path"]] = {
            **spec, "title": media_titles[spec["key"]],
            "thumbnail": f"https://i.ytimg.com/vi/{spec['key']}/hqdefault.jpg",
        }
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SOURCE / "assets", DIST / "assets")
    # Version the entire CSS/JS dependency graph, including nested imports.
    # Otherwise browsers can combine fresh HTML with a cached entry point.
    code_assets = sorted(p for p in (SOURCE / "assets").rglob("*") if p.suffix in {".css", ".js"})
    fingerprint = hashlib.sha256()
    for asset in code_assets:
        fingerprint.update(asset.relative_to(SOURCE).as_posix().encode())
        fingerprint.update(asset.read_bytes())
    asset_version = fingerprint.hexdigest()[:12]
    for asset in code_assets:
        text = asset.read_text(encoding="utf-8")
        pattern = r"(@import\s+url\(['\"]?)(\./[^'\"\s)]+)(['\"]?\))" if asset.suffix == ".css" else r"(\bfrom\s+['\"])(\./[^'\"]+)(['\"])"
        text = re.sub(pattern, lambda m: f"{m[1]}{m[2]}?v={asset_version}{m[3]}", text)
        (DIST / asset.relative_to(SOURCE)).write_text(text, encoding="utf-8")
    env = Environment(loader=FileSystemLoader(SOURCE / "templates"), autoescape=select_autoescape(["html"]), undefined=StrictUndefined)
    env.globals["asset_version"] = asset_version
    env.globals["facebook_timeline_src"] = facebook_timeline_src
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
        html = env.get_template(template).render(site=site, pages=pages, media=media, experiences=experiences, coordinations=coordinations, department=department, academy_previews=academy_previews, processes=processes, certifications=certifications, partners=partners, about_directory=about_directory, url=url, local_body=local_body, current_path=path, **context)
        target = DIST / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    render("index.html", "pages/home.html", title="Vinculación FCC · BUAP", active="inicio", description=site["description"])
    for landing in site["landings"]:
        if landing["key"] == "recursos":
            render(landing["path"], "pages/resource-library.html", title=landing["title"], active=landing["key"], description=landing["description"], landing=landing, **library)
        else:
            render(landing["path"], "pages/landing.html", title=landing["title"], active=landing["key"], description=landing["description"], landing=landing)
    for page in pages:
        active = page["section"] if page["section"] != "archivo" else "recursos"
        experience = experiences["academies"].get(page["path"])
        employer = employers.get(page["path"])
        catalog = learning_data["catalogs"].get(page["path"])
        learning = learning_data["profiles"].get(page["path"])
        cisco_template = {"academias/cisco/ruta/index.html": "pages/cisco-route.html", "academias/cisco/cursos/index.html": "pages/cisco-courses.html"}.get(page["path"])
        template = cisco_template or ("pages/learning-catalog.html" if catalog else "pages/aws-guide.html" if page["path"] == "recursos/inscripcion-aws/index.html" else "pages/employer.html" if employer else "pages/coordinations.html" if page["path"] == "academias/coordinaciones/index.html" else "pages/academy.html" if experience else "pages/about.html" if page["path"] == "nosotros/index.html" else "pages/article.html")
        template = {"nosotros/labor/index.html": "pages/labor.html", "nosotros/coordinaciones/index.html": "pages/team.html", "egresados/seguimiento/index.html": "pages/alumni-followup.html"}.get(page["path"], template)
        cert_slug = page["path"].split("/")[1] if page["section"] == "certificaciones" else ""
        cert = certifications["profiles"].get(cert_slug)
        if cert:
            template = "pages/certification-profile.html"
        else:
            template = {"certificaciones/oferta/index.html": "pages/certification-offer.html", "certificaciones/precios/index.html": "pages/certification-prices.html", "certificaciones/proceso/index.html": "pages/certification-process.html"}.get(page["path"], template)
        render(page["path"], template, title=page["title"], active=active, description=page["summary"] or page["title"], page=page, experience=experience, employer=employer, catalog=catalog, learning=learning, cisco=cisco, alumni=alumni, cert=cert)
    education_contact = next(member for member in department["members"] if member["area"] == "Educación Continua")
    render("educacion-continua/index.html", "pages/continuing-education.html", title=education["title"], active="nosotros", description=education["intro"], education=education, education_contact=education_contact)
    render("buscar/index.html", "pages/search.html", title="Buscar", active="", description="Encuentra academias, certificaciones, trámites y recursos de Vinculación FCC.")
    search_index = [
        {"title": p["title"], "path": p["path"], "section": p["section"],
         "text": p["original_text"] + "\n" + "\n".join(course["name"] for course in learning_data["catalogs"].get(p["path"], {}).get("courses", [])) + "\n" + "\n".join(image["text"] for image in p["images"] if image["text_status"] == "revisado contra imagen"),
         "summary": p["summary"]}
        for p in pages if p["id"] != "contenido-2141"
    ]
    search_index += [{"title": l["title"], "path": l["path"], "section": l["key"], "text": l["description"], "summary": l["description"]} for l in site["landings"]]
    search_index.append({"title": education["title"], "path": "educacion-continua/index.html", "section": "nosotros", "text": education["intro"] + " " + " ".join(p["name"] + " " + p["description"] for p in education["programs"]), "summary": "Educación continua, áreas de certificación Eduit y contacto de la coordinación."})
    for record in search_index:
        if record["path"] == "academias/cisco/ruta/index.html":
            record["text"] += "\n" + "\n".join(course for route in cisco["routes"] for branch in route["branches"] for course in branch["courses"])
    (DIST / "assets/search-index.json").write_text(json.dumps(search_index, ensure_ascii=False), encoding="utf-8")
    (DIST / "robots.txt").write_text("# Preview: enable indexing only after editorial approval.\nUser-agent: *\nDisallow: /\n", encoding="utf-8")
    aliases = [{"source": p["source_url"], "target": p["path"]} for p in pages]
    (DIST / "redirect-map.json").write_text(json.dumps(aliases, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built {len(written)} HTML pages in {DIST}")


if __name__ == "__main__":
    build()
