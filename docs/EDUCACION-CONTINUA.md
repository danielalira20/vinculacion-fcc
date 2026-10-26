# Educación Continua · Página nativa (sin Canva)

## Archivos

- `src/templates/pages/continuing-education.html`: vista semántica Jinja/HTML integrada con encabezado y pie del sitio.
- `src/content/continuing-education.json`: textos, filtros, tarjetas del catálogo y preguntas frecuentes; aquí se actualiza el contenido sin editar HTML.
- `src/assets/css/continuing-education.css`: estilos adaptables y aislados por clases `ed-`.
- `src/assets/js/continuing-education.js`: búsqueda y filtros progresivos de tarjetas.
- `src/content/site.json`: menú «Nosotros > Educación continua · Eduit» convertido de vínculo Canva a enlace local.
- `scripts/build.py`: genera `dist/educacion-continua/index.html` e indexa la página en la búsqueda local.

## Generar y ver

En la raíz del proyecto, ejecuta:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abre `http://127.0.0.1:8000/educacion-continua/`.

No edites `dist/`: se elimina y vuelve a generar en cada compilación. Si ya lo tienes configurado, solo necesitas reconstruir el sitio.

## Revisión editorial pendiente

La página enlazada en Canva no pudo inspeccionarse como contenido textual ni descargarse en este entorno, por lo que esta implementación es una **primera versión propia**, consistente con el diseño del sitio, **no una reproducción exacta de las diapositivas de Canva**. Hay que comparar contra capturas o exportación de Canva para trasladar todos sus textos e imágenes de forma fiel.

Los nombres de las seis áreas se basan en un muestreo del catálogo público Eduit (octubre de 2026). No están confirmados como convocatoria activa de la FCC, ni se ofrecen inscripciones, tarifas, pagos o disponibilidad a través de esta nueva página. El correo y nombre de coordinación provienen del directorio del proyecto y de la web FCC; confirmar actualizaciones antes de publicar.

URLs consultadas:
- `https://www.grupoeduit.com/certificaciones/3/1`
- `https://www.grupoeduit.com/certificaciones/3/2`
- `https://www.grupoeduit.com/certificaciones/7/1`
- `https://www.cs.buap.mx/Coordinadores.php`

Para actualizar el catálogo, cambia los registros `programs` en el JSON. Los valores de `category` deben coincidir con un `key` de `categories`, los nombres de iconos deben existir en `src/assets/icons/` y los temas deben existir en los estilos compartidos.

## Registro, QR y aviso de privacidad

- La URL del formulario, la imagen del QR y el aviso de privacidad están en `registration` dentro de `src/content/continuing-education.json`. No pegues la URL directamente en la plantilla.
- El botón y el QR del formulario siempre se publican, acompañados de una línea de privacidad: si `privacy_notice_url` tiene un enlace https, enlaza al aviso; si está vacío, indica que se solicite el aviso por correo a la coordinación. Pendiente: obtener y pegar la URL del aviso.
- `scripts/build.py` detiene la compilación si `form_url` no es un Microsoft Forms (`forms.cloud.microsoft` o `forms.office.com`) o si el aviso no usa https.
- `scripts/test_continuing_education.py` decodifica el QR y comprueba que apunte exactamente a `form_url`. Si cambias el formulario, regenera la imagen del QR o la prueba fallará.
- Pendiente institucional: confirmar que el formulario pertenece a una cuenta `@correo.buap.mx`.
