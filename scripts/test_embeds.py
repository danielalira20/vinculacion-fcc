"""Regression checks for the media migration and its URL allowlist."""
import unittest
from embeds import embed_spec, prepare_page, render_embed


class EmbedTests(unittest.TestCase):
    def test_youtube_keeps_start_but_drops_autoplay(self):
        spec = embed_spec("https://www.youtube.com/embed/JP1C-dxaRq4?start=3&autoplay=1")
        self.assertIn("start=3", spec["src"])
        self.assertNotIn("autoplay", spec["src"])

    def test_unapproved_urls_are_not_embedded(self):
        for href in ("javascript:alert(1)", "http://www.youtube.com/embed/JP1C-dxaRq4", "https://www.youtube.com.evil.test/embed/JP1C-dxaRq4", "@/../../secret.pdf", "https://forms.office.com/Pages/ResponsePage.aspx?id=%22%3E"):
            with self.subTest(href=href):
                self.assertIsNone(embed_spec(href))

    def test_canva_duplicate_links_become_one_viewer(self):
        href = "https://www.canva.com/design/DAF66t1rdWo/iATjcEcqsyYL6Ay-lpOFxA/view"
        page = {"title": "Academia", "body": f'<a href="{href}?embed">Abrir recurso externo</a><a href="{href}">Ver recurso</a>', "resources": [{"href": href, "label": "Ver recurso"}], "original_text": "Conservado"}
        view = prepare_page(page, {}, {})
        self.assertEqual(view["body"].count("<iframe"), 1)
        self.assertEqual(view["resources"], [])
        self.assertIn("Abrir recurso externo", page["body"])
        self.assertEqual(page["original_text"], "Conservado")

    def test_titles_are_escaped_and_frames_named(self):
        markup = render_embed("https://www.youtube.com/embed/JP1C-dxaRq4", '<script>"Título"</script>')
        self.assertNotIn("<script>", markup)
        self.assertIn('title="&lt;script&gt;', markup)
        self.assertIn('loading="lazy"', markup)
        self.assertIn('referrerpolicy="strict-origin-when-cross-origin"', markup)

    def test_forms_and_local_pdf(self):
        form = embed_spec("https://forms.office.com/Pages/ResponsePage.aspx?id=abc_DEF-123&embed=false")
        self.assertIn("embed=true", form["src"])
        self.assertNotIn("embed=", form["link"])
        self.assertEqual(embed_spec("@/assets/media/a68c6efe6ff18ca9.pdf")["kind"], "pdf")
        pdf = render_embed("@/assets/media/a68c6efe6ff18ca9.pdf", "SiPAGO")
        self.assertEqual(pdf.count("<img"), 18)
        self.assertIn("sipago-page-18.jpg", pdf)
        self.assertIn('href="@/assets/media/a68c6efe6ff18ca9.pdf"', pdf)

    def test_microsoft_forms_current_host_is_allowed_without_lookalikes(self):
        spec = embed_spec("https://forms.cloud.microsoft/pages/responsepage.aspx?id=abc_DEF-123&route=shorturl")
        self.assertEqual(spec["kind"], "form")
        self.assertIn("https://forms.cloud.microsoft/", spec["src"])
        self.assertIn("embed=true", spec["src"])
        self.assertNotIn("route=", spec["src"])
        self.assertIsNone(embed_spec("https://forms.cloud.microsoft.evil.test/pages/responsepage.aspx?id=abc"))

    def test_retired_videos_have_no_broken_player(self):
        markup = render_embed("https://www.youtube.com/embed/Ar2L2i2A0aY", "Autodesk")
        self.assertNotIn("<iframe", markup)
        self.assertIn("está privado", markup)

    def test_google_form_uses_only_the_published_form_path(self):
        spec = embed_spec("https://docs.google.com/forms/d/e/abc_DEF-123/viewform?usp=sharing")
        self.assertEqual(spec["src"], "https://docs.google.com/forms/d/e/abc_DEF-123/viewform?embedded=true")
        self.assertNotIn("usp", spec["link"])
        for href in ("https://docs.google.com.evil.test/forms/d/e/abc/viewform", "https://docs.google.com/document/d/abc/edit", "http://docs.google.com/forms/d/e/abc/viewform", "https://docs.google.com/forms/d/e/%22/viewform"):
            self.assertIsNone(embed_spec(href))


if __name__ == "__main__":
    unittest.main()
