"""Public Facebook timelines, limited to the pages recovered from the FCC site."""
from urllib.parse import parse_qs, urlencode, urlsplit

PUBLIC_PAGES = {
    "VinculandoteFcc", "BUAPFCCAcademiadeOracle",
    "Academia-CISCO-BUAP-107611248503423",
}


def public_page(href):
    parsed = urlsplit(href)
    if (parsed.scheme == "https" and parsed.netloc == "www.facebook.com"
            and parsed.path.strip("/") in PUBLIC_PAGES
            and not parsed.query and not parsed.fragment):
        return "https://www.facebook.com/" + parsed.path.strip("/")
    return None


def facebook_timeline_src(href, width=500):
    page = public_page(href)
    if not page:
        raise ValueError("Facebook timeline must use a recovered institutional page")
    params = {"href": page, "tabs": "timeline", "width": max(180, min(500, int(width))),
              "height": 500, "small_header": "true", "adapt_container_width": "true",
              "hide_cover": "false", "show_facepile": "false", "locale": "es_LA"}
    return "https://www.facebook.com/plugins/page.php?" + urlencode(params)


def facebook_frame_spec(href):
    parsed = urlsplit(href)
    if (parsed.scheme != "https" or parsed.netloc != "www.facebook.com"
            or parsed.path != "/plugins/page.php"):
        return None
    page = public_page(parse_qs(parsed.query).get("href", [""])[0])
    if not page:
        return None
    return {"kind": "facebook", "key": page, "src": facebook_timeline_src(page),
            "link": page, "action": "Ver publicaciones en Facebook"}
