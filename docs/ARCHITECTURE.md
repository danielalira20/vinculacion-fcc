# Arquitectura

## Flujo

Contenido JSON + plantillas Jinja2 → `scripts/build.py` → HTML, CSS, JavaScript e índice JSON de búsqueda en `dist/`.

El navegador recibe archivos estáticos. Python se usa únicamente para construirlos; no existe un backend en ejecución. Las rutas usan archivos `index.html` explícitos y enlaces relativos, por lo que el sitio funciona tanto en la raíz de un dominio como dentro de una subcarpeta.

La generación calcula una huella del contenido de todos los archivos CSS y JavaScript. Esa versión se añade a los enlaces de entrada del HTML y a las importaciones de hojas de estilo y módulos. Si cambia cualquier dependencia, los navegadores solicitan las nuevas versiones; se evita combinar HTML actualizado con estilos o módulos antiguos en caché. El código fuente mantiene rutas simples y las URLs versionadas solo aparecen en `dist/`.

## Responsabilidades

- `site.json`: navegación, textos editoriales, catálogo de Academias y certificaciones, servicios y contacto.
- `experiences.json`: composición editorial, identidad, accesos y contactos de las portadas. No sustituye el contenido original de `pages.json`.
- `pages.json`: contenido recuperado, ruta nueva, procedencia, recursos y notas de vigencia. El texto original permanece junto al contenido convertido.
- `employers.json`: contenido editorial de Bolsa de Trabajo y registros de Empresas y Vacantes.
- `processes.json`: cinco procesos nativos, requisitos, acciones y referencias a las imágenes originales sustituidas.
- `certifications.json`: presentación estructurada de IT Specialist, Adobe, Microsoft Office, oferta, precios históricos y recursos del proceso. Conserva textos, versiones e identificadores originales; no sustituye el registro de migración. `certification.html` y cuatro plantillas de página comparten la escala de la familia. `certifications.css` está limitado a `.cert-page`; `learning.js` mejora sus catálogos sin ocultar contenido cuando no hay JavaScript.
- `presentation.py`: adaptación de gráficos a marcadores de componentes y de emojis a SVG sin modificar los registros originales; los marcadores se renderizan con la plantilla común `process-flow.html`.
- `coordinations.json`: personas, contactos, fotografías recuperadas y videos del directorio de Academias.
- `embedded-resources.json`: nombres descriptivos de los materiales integrados.
- `asset-sources.json`: trazabilidad de las imágenes y PDF locales. Los nombres derivados del hash evitan colisiones entre archivos llamados `image.png`.
- `layouts/`: estructura, metadatos, hojas de estilo y punto de entrada de JavaScript.
- `components/`: elementos comunes sin duplicación entre páginas.
- `pages/`: composición propia de cada tipo de página.
- CSS: valores centrales, estructura, componentes y estilos particulares separados.
- `editorial.css`: composiciones expresivas de las portadas y perfiles; las plantillas `academy.html` y `about.html` conservan también el contenido completo recuperado.
- JavaScript: un módulo por responsabilidad. La búsqueda usa `textContent` para presentar resultados, sin interpretar HTML de las consultas.

Jinja2 usa escape automático y variables estrictas. El HTML recuperado se convierte durante una importación manual con una lista permitida de etiquetas; se retiran scripts, estilos, manejadores de eventos y elementos de formulario del WordPress anterior. Durante la generación, `scripts/embeds.py` restaura los visores de YouTube, Canva, Microsoft Forms y el PDF local desde una lista permitida de dominios y rutas. El PDF utiliza 18 imágenes locales renderizadas a partir del original, dentro de una región desplazable con ampliación por página y descarga del documento; su inventario está en `PDF_PREVIEWS` de `scripts/embeds.py`. Cada visor de terceros tiene título accesible, carga diferida y un enlace alternativo específico. Los videos no se reproducen automáticamente. Los enlaces repetidos de una misma presentación se unifican. Los videos retirados o privados detectados se presentan como tarjetas de disponibilidad, sin un reproductor roto. La procedencia permanece en los archivos de contenido y documentación, fuera de la interfaz pública.

## Actualizaciones

En la portada de Academias, `academy-video.html` y `academy-video.js` presentan los videos de `coordinations.json`, normalizados con la misma lista permitida de `embeds.py`. La miniatura se solicita a YouTube; el iframe solo se crea tras la acción de reproducir. Esta acción inicia el video solicitado, mientras la carga inicial permanece silenciosa. Al abrir otra tarjeta, volver a la miniatura o filtrar una tarjeta activa, el iframe se retira para detener el audio. El control de cierre recibe el foco sin cambiar la posición de lectura. Sin JavaScript la miniatura conserva su enlace a YouTube, y los enlaces a la academia siguen disponibles. Las tarjetas del Inicio conservan su composición original.

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

Los pasos usan elementos `details` nativos abiertos inicialmente. `process.js` añade únicamente el control conjunto para abrir/cerrar los detalles; el contenido y las acciones no dependen de JavaScript. La reconstrucción visual mantiene requisitos y contactos publicados, sin simular registro, validación ni finalización del trámite.
