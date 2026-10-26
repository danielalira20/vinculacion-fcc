"""Integrity checks for the Educación Continua registration (form link, QR and privacy notice)."""
import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit

import zxingcpp
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FORM_HOSTS = {"forms.office.com", "forms.cloud.microsoft"}


class ContinuingEducationRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        content = json.loads((ROOT / "src/content/continuing-education.json").read_text(encoding="utf-8"))
        cls.registration = content["registration"]

    def test_form_url_is_an_official_microsoft_form(self):
        form = urlsplit(self.registration["form_url"])
        self.assertEqual(form.scheme, "https")
        self.assertIn(form.hostname, FORM_HOSTS)
        self.assertRegex(form.path, r"(?i)^(/pages/responsepage\.aspx|/r/[a-z0-9]+)$")

    def test_qr_points_to_the_same_form(self):
        image = Image.open(ROOT / "src" / self.registration["qr_image"]).convert("L")
        decoded = [result.text for result in zxingcpp.read_barcodes(image)]
        self.assertEqual(len(decoded), 1, "La imagen debe contener exactamente un QR.")
        # Microsoft Forms adds ?origin=QRCode to its own QR codes to count scans; nothing else is allowed.
        expected = {self.registration["form_url"], self.registration["form_url"] + "?origin=QRCode"}
        self.assertIn(decoded[0], expected,
                      "El QR no coincide con form_url; regenera la imagen o corrige el JSON.")

    def test_template_has_no_hardcoded_form_links(self):
        template = (ROOT / "src/templates/pages/continuing-education.html").read_text(encoding="utf-8")
        for host in FORM_HOSTS:
            self.assertNotIn(host, template, "La URL del formulario debe venir de continuing-education.json")

    def test_privacy_notice_uses_https_when_present(self):
        privacy = self.registration["privacy_notice_url"]
        if privacy:
            self.assertEqual(urlsplit(privacy).scheme, "https")

    def test_published_page_shows_form_with_a_privacy_line(self):
        page = ROOT / "dist/educacion-continua/index.html"
        if not page.exists():
            self.skipTest("Ejecuta scripts/build.py antes de esta prueba.")
        html = page.read_text(encoding="utf-8")
        self.assertEqual(html.count(self.registration["form_url"].replace("&", "&amp;")), 2)
        self.assertIn("data-privacy-notice", html)
        privacy = self.registration["privacy_notice_url"]
        if privacy:
            self.assertIn(privacy.replace("&", "&amp;"), html)


if __name__ == "__main__":
    unittest.main()
