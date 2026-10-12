"""Offline regression checks for issues reported in Diego's FCC review."""
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.hrefs, self.ids, self.iframes = [], [], []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('href'):
            self.hrefs.append(attrs['href'])
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'iframe':
            self.iframes.append(attrs.get('src', ''))


class ReviewRegressions(unittest.TestCase):
    def page(self, path):
        return (ROOT / 'dist' / path).read_text()

    def test_contacts_survive_migration_and_have_a_web_option(self):
        sources = json.loads((ROOT / 'src/content/pages.json').read_text())
        original = {unquote(urlsplit(href).path) for page in sources
                    for href in Links(page['body']).hrefs if href.startswith('mailto:')}
        public = set()
        for path in (ROOT / 'dist').rglob('*.html'):
            document = Links(path.read_text())
            self.assertEqual(document.ids.count('email-dialog'), 1, path)
            self.assertIn('email-address', document.ids, path)
            public.update(unquote(urlsplit(href).path) for href in document.hrefs
                          if href.startswith('mailto:'))
        self.assertFalse(original - public, original - public)

    def test_mos_links_are_specific_to_application_and_version(self):
        data = json.loads((ROOT / 'src/content/certifications.json').read_text())
        units = data['profiles']['microsoft-office']['units']
        all_links = []
        for unit in units:
            for objective in unit['objectives']:
                parsed = urlsplit(objective['href'])
                self.assertEqual(parsed.hostname, 'learn.microsoft.com')
                self.assertIn(f"mos-{unit['name'].lower()}-", parsed.path)
                all_links.append(objective['href'])
        self.assertEqual(len(all_links), 12)
        self.assertEqual(len(set(all_links)), 12)
        rendered = Links(self.page('certificaciones/microsoft-office/index.html'))
        self.assertTrue(set(all_links).issubset(rendered.hrefs))
        self.assertFalse(any('/MOS/Certify/' in href for href in rendered.hrefs))

    def test_it_does_not_send_visitors_to_missing_cybersecurity_file(self):
        rendered = Links(self.page('certificaciones/it-specialist/index.html'))
        self.assertFalse(any('WZamgoVwSSKHa5gU' in href for href in rendered.hrefs))
        self.assertIn('https://certiport.pearsonvue.com/fc/ITS/cybersecurity', rendered.hrefs)

    def test_restricted_oracle_form_is_not_offered_as_registration(self):
        rendered = Links(self.page('academias/oracle/recursos/index.html'))
        self.assertFalse(any('cHBckaBpNM' in href for href in rendered.hrefs))
        self.assertTrue(any(href.startswith('mailto:coord_oracleacademia.fcc@correo.buap.mx?subject=')
                            for href in rendered.hrefs))

    def test_cisco_2023_form_is_not_presented_as_current(self):
        html = self.page('academias/cisco/cursos/index.html')
        rendered = Links(html)
        self.assertFalse(any('1FAIpQLSe4AeUP4sx3ZE24VpzXhz2g4eZOiEKVLZz4VZy1ljKP_H3G1g' in href
                             for href in rendered.hrefs + rendered.iframes))
        self.assertIn('Primavera 2023', html)
        self.assertTrue(any(href.startswith('mailto:buap.cisco@correo.buap.mx?subject=')
                            for href in rendered.hrefs))

    def test_aws_matches_the_available_form_without_reusing_old_conditions(self):
        data = json.loads((ROOT / 'src/content/learning.json').read_text())
        catalog = data['catalogs']['academias/aws/oferta/index.html']
        self.assertEqual(catalog['period'], 'Otoño 2026')
        self.assertEqual(len(catalog['courses']), 10)
        self.assertIn('AWS Academy Data Center Technician', [c['name'] for c in catalog['courses']])
        self.assertEqual(catalog['archived_offer']['facts'][0], ['09', 'Cursos publicados'])
        self.assertIn('Data Center Technician', self.page('academias/aws/oferta/index.html'))


if __name__ == '__main__':
    unittest.main()
