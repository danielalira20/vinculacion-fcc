# Arquitectura

## Flujo

Contenido JSON + plantillas Jinja2 → `scripts/build.py` → HTML, CSS, JavaScript e índice JSON de búsqueda en `dist/`.

El navegador recibe archivos estáticos. Python se usa únicamente para construirlos; no existe un backend en ejecución. Las rutas usan archivos `index.html` explícitos y enlaces relativos, por lo que el sitio funciona tanto en la raíz de un dominio como dentro de una subcarpeta.

## Responsabilidades

- `site.json`: navegación, textos editoriales, catálogo de Academias y certificaciones, servicios y contacto.
- `experiences.json`: composición editorial, identidad, accesos y contactos de las portadas. No sustituye el contenido original de `pages.json`.
- `pages.json`: contenido recuperado, ruta nueva, procedencia, recursos y notas de vigencia. El texto original permanece junto al contenido convertido.
- `asset-sources.json`: trazabilidad de las imágenes y PDF locales. Los nombres derivados del hash evitan colisiones entre archivos llamados `image.png`.
- `layouts/`: estructura, metadatos, hojas de estilo y punto de entrada de JavaScript.
- `components/`: elementos comunes sin duplicación entre páginas.
- `pages/`: composición propia de cada tipo de página.
- CSS: valores centrales, estructura, componentes y estilos particulares separados.
- `editorial.css`: composiciones expresivas de las portadas y perfiles; las plantillas `academy.html` y `about.html` conservan también el contenido completo recuperado.
- JavaScript: un módulo por responsabilidad. La búsqueda usa `textContent` para presentar resultados, sin interpretar HTML de las consultas.

Jinja2 usa escape automático y variables estrictas. El HTML recuperado se convierte durante una importación manual con una lista permitida de etiquetas; se retiran scripts, estilos, manejadores de eventos y elementos de formulario del WordPress anterior. Los iframes pasan a enlaces explícitos, evitando cargar proveedores externos al visitar una página.

## Actualizaciones

1. Editar contenido o componentes de `src/`.
2. Generar el sitio.
3. Ejecutar `scripts/check.py`.
4. Revisar en navegador las páginas afectadas en escritorio y móvil.
5. Registrar la modificación en Git.

`dist/` es un resultado regenerable y queda fuera del historial Git. El ZIP de entrega contiene una copia generada para revisar la página sin instalar Jinja2.

## Ampliaciones

Moodle: primero definir si solo se enlazarán cursos o si se necesitan cuentas compartidas, matrículas, progreso o calificaciones. En estos últimos casos hay que diseñar una integración autorizada con la instancia institucional y un backend que proteja las credenciales; nunca incluir tokens en JavaScript del navegador.

Edición de contenido: si el departamento requiere un panel, decidir quién edita, qué permisos tiene y cómo aprueba cambios. La arquitectura actual asume actualización mediante archivos y generación del sitio. No se implementa un panel ficticio.

Publicación: alojamiento estático, dominio oficial y redirecciones por confirmar. La configuración de indexación y el aviso de privacidad deben revisarse antes de activar la versión pública.
