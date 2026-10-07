"""Public presentation adaptations; the recovered source records stay intact."""
import html
import re
from functools import lru_cache
from pathlib import Path

EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u200D]")
ICON_FOR_EMOJI = {"\u2705": "check", "\u2753": "info", "\U0001f447": "arrow", "\U0001f4c5": "clock", "\U0001f4ca": "network", "\U0001f4cb": "document", "\U0001f4cc": "map", "\U0001f50d": "search"}


@lru_cache
def inline_icon(name):
    icon = (Path(__file__).resolve().parents[1] / "src/assets/icons" / f"{name}.svg").read_text()
    return icon.replace("<svg ", '<svg class="content-icon" ', 1).strip()


def clean_text(text):
    return EMOJI.sub("", text)


def prepare_presentation(page, processes):
    result = dict(page)
    # An SVG replaces the symbol in rich content; plain metadata remains plain text.
    result["body"] = EMOJI.sub(lambda match: inline_icon(ICON_FOR_EMOJI[match[0]]) if match[0] in ICON_FOR_EMOJI else "", result["body"])
    for field in ("title", "summary", "original_text", "notice"):
        result[field] = clean_text(result[field])
    result["resources"] = [{**item, "label": clean_text(item["label"])} for item in result["resources"]]
    result["images"] = [{**item, "text": clean_text(item["text"])} for item in result["images"]]
    result["has_process_flow"] = False

    def replace_figure(match):
        for key, flow in processes.items():
            if f'@/{flow["asset"]}' in match[0]:
                result["has_process_flow"] = True
                return f'<!-- process-flow:{key} -->'
        # Old image-shaped buttons become readable native resource links.
        if page["path"] == "certificaciones/proceso/index.html":
            buttons = {"assets/media/c1f652ce9e2f842b.png": ("https://sipago.buap.mx/", "Acceder a SiPAGO BUAP"), "assets/media/7549461de90f7a0f.png": ("@/assets/media/a68c6efe6ff18ca9.pdf", "Abrir la guía de pagos referenciados"), "assets/media/43c0f58ea946ef29.png": ("@/certificaciones/precios/index.html", "Consultar precios por certificación"), "assets/media/23115487729660b7.png": ("@/certificaciones/oferta/index.html", "Explorar la oferta de certificaciones")}
            for asset, (href, title) in buttons.items():
                if f'@/{asset}' in match[0]:
                    return f'<a class="inline-resource" href="{html.escape(href, quote=True)}">{html.escape(title)}{inline_icon("arrow")}</a>'
        return match[0]

    result["body"] = re.sub(r"<figure\b[^>]*>.*?</figure>", replace_figure, result["body"], flags=re.S)
    if result["has_process_flow"] and 'class="resource-embed embed-form"' in result["body"]:
        result["body"] = result["body"].replace('class="resource-embed embed-form"', 'class="resource-embed embed-form" id="formulario"', 1)
    return result
