import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

// Import the browser ES module without changing the project's runtime requirements.
const source = readFileSync(new URL('../src/assets/js/email.js', import.meta.url), 'utf8');
const {emailDestinations} = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const original = 'mailto:coord_oracleacademia.fcc@correo.buap.mx?subject=Acceso%20Oracle%20%26%20cursos&body=Hola%0AQuiero%20informaci%C3%B3n&cc=academias.fcc%40correo.buap.mx';
const result = emailDestinations(original);
assert.equal(result.recipient, 'coord_oracleacademia.fcc@correo.buap.mx');
for (const provider of ['gmail', 'outlook']) {
  const url = new URL(result[provider]);
  assert.equal(url.searchParams.get('to'), result.recipient);
  assert.equal(url.searchParams.get(provider === 'gmail' ? 'su' : 'subject'), 'Acceso Oracle & cursos');
  assert.equal(url.searchParams.get('body'), 'Hola\nQuiero información');
  assert.equal(url.searchParams.get('cc'), 'academias.fcc@correo.buap.mx');
}
const named = emailDestinations('mailto:buap.cisco@correo.buap.mx', 'Próxima convocatoria');
assert.equal(new URL(named.gmail).searchParams.get('su'), 'Próxima convocatoria');
assert.equal(new URL(named.outlook).searchParams.get('subject'), 'Próxima convocatoria');
assert.throws(() => emailDestinations('javascript:alert(1)'), TypeError);
assert.throws(() => emailDestinations('mailto:%zz@correo.buap.mx'), URIError);
const special = new URL(emailDestinations('mailto:vinculacion.fcc@correo.buap.mx?subject=%3Cscript%3E%26%3F').gmail);
assert.equal(special.searchParams.get('su'), '<script>&?');
assert.equal(special.searchParams.size || [...special.searchParams].length, 5);
console.log('PASS: email destinations preserve recipient, subject, body and cc; reject invalid schemes and encoding.');
