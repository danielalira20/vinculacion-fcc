# Comprobaciones de la versión actual

## Generación y archivos

- 48 páginas HTML generadas a partir de 41 registros recuperados y las páginas nuevas de presentación y búsqueda.
- Comprobación de 1337 destinos locales entre páginas, imágenes, estilos, scripts y fragmentos de navegación.
- Verificación de importaciones CSS y JavaScript, identificadores HTML únicos, un título principal por página, idioma español y región principal de contenido.
- Sin manejadores de eventos inline ni scripts del WordPress anterior. Visores limitados a YouTube, Canva, Microsoft Forms y un PDF local; títulos accesibles, carga diferida y política de referencia comprobados.
- Tipografía local cargada en el navegador.

## Pruebas de interacción en navegador

- Búsqueda de `ciberseguridad` en Academias: muestra EC-Council y cuenta de una Academia.
- Combinación de esa búsqueda con filtro Cisco: muestra cero resultados y el mensaje correspondiente.
- Búsqueda general de `liberacion`, sin acento: encuentra Proceso Liberación y sus enlaces locales.
- Vista a 390 × 844 px: portada y proceso de liberación sin desbordamiento horizontal.
- Menú móvil: abre los enlaces, actualiza su estado accesible y cierra con Escape, devolviendo el foco al botón.
- Portada y páginas representativas revisadas visualmente en escritorio y móvil.

Las capturas están en `docs/previews/`. No se han enviado formularios ni realizado pagos, y no se ha probado una integración con Moodle. Las comprobaciones de estructura son básicas; no representan una certificación integral de accesibilidad ni validan la vigencia del contenido institucional.

## Revisión tras el rediseño de portadas

- Inicio, cinco secciones principales, Nosotros y cuatro Academias sin desbordamientos horizontales a 390 px.
- Inicio comprobado también a 900 px; cabecera y portada se mantienen dentro del ancho disponible.
- Inicio, Oracle y proceso de liberación sin desbordamientos a 320 px.
- Oracle y Certificaciones revisadas visualmente en escritorio; Oracle e Inicio revisadas en móvil.
- Menú móvil abre y cierra con Escape; búsqueda de `ciberseguridad` en Academias sigue mostrando EC-Council y la cuenta de un resultado.
- Las portadas enlazan a recursos existentes y a los perfiles de Facebook conservados en el respaldo. No se incrusta un feed externo.
- El texto «Un vínculo entre tu formación…» se comprobó en navegador a 15 px en la vista de escritorio intermedia.
- Corregidos 12 enlaces de correo del contenido importado que apuntaban a páginas en lugar de abrir un correo; conservados el texto original y las direcciones publicadas.

## Coordinaciones y recursos integrados

- Las 48 páginas se comprueban para impedir enlaces al dominio retirado, bloques de fuentes y etiquetas genéricas de recurso externo. También se retira del texto público la dirección del portal anterior, conservando el original en JSON.
- 14 videos integrados, tres presentaciones Canva, cinco formularios y un PDF local. Dos videos originales no disponibles muestran tarjetas de consulta; el de Oracle se sustituye por el video oficial ya presente en otro registro recuperado.
- Seis pruebas de migración: dominios y rutas permitidos, escape de títulos, eliminación de reproducción automática, conservación del segundo inicial, deduplicación de Canva, formularios/PDF y tratamiento de videos privados.
- Todos los videos únicos revisados en navegador; tres presentaciones Canva y cinco formularios con contenido visible. No se han enviado datos ni completado pasos de registro.
- Coordinaciones y páginas de visores comprobadas a 320 px: sin desbordamiento horizontal; los reproductores conservan al menos 200 px de alto y se ajustan al ancho disponible.
- Guía SiPAGO: 18 páginas renderizadas localmente y revisadas visualmente. Visor con desplazamiento, foco de teclado, ampliación por página y enlace al PDF original; evita el panel vacío del visor PDF del navegador.
- Oracle reprodujo dentro de la página durante la prueba. La disponibilidad de proveedores externos puede cambiar.

## Bolsa de Trabajo, Vacantes y procesos nativos

- Bolsa de Trabajo, Registro de Vacantes y Registro de Empresas usan una composición editorial propia con geometría nativa, glass moderado y contactos reales. No se crean ofertas de empleo ficticias.
- Cinco flujos reconstruidos en HTML seleccionable: registro de empresas, registro de vacantes, compra de certificaciones, liberación y registro AWS. Cada paso usa un elemento `details` nativo; un botón permite desplegar o contraer todos los pasos. El formulario conserva su incrustación original.
- Ratón y teclado comprobados para el control conjunto y un paso individual. Los detalles quedan abiertos en el HTML inicial para que el contenido esté disponible sin JavaScript.
- Páginas afectadas comprobadas a 320 y 390 px, y Bolsa, Vacantes, Empresas y Compra a 900 px, sin desbordamiento horizontal. El formulario de Vacantes muestra sus campos dentro de la página; no se envían datos.
- La revisión automática de las 48 páginas rechaza emojis en el HTML público y cualquier referencia a las cinco imágenes de flujo reemplazadas. Los iconos son SVG locales.
- Los textos originales y las referencias de los 41 registros se compararon con la revisión anterior y permanecen intactos. Se revisó contra la imagen la transcripción del flujo de Vacantes.

## Videos en las tarjetas de Academias

- Las cuatro miniaturas corresponden a las presentaciones de Cisco, AWS, Oracle y EC-Council del directorio recuperado. Oracle mantiene la sustitución oficial documentada, porque el video original fue retirado.
- Las cuatro presentaciones cargaron sus reproductores dentro de la página en el navegador; Cisco y AWS mostraron reproducción en curso. La dirección de Academias se mantiene durante la reproducción.
- Al abrir AWS después de Cisco queda un solo iframe. Filtrar a Oracle elimina el reproductor de AWS. El cierre devuelve la miniatura y el foco; Enter abre el video y Escape lo cierra desde los controles de la tarjeta.
- Miniaturas reales cargadas para las cuatro academias. Enlaces separados a las páginas de cada academia y a YouTube; sin navegación obligatoria al reproducir.
- Galería revisada visualmente en escritorio y reproducción móvil a 390 px; sin desbordamiento a 320 y 390 px. Los reproductores mantienen el ancho de la tarjeta y al menos 200 px de alto.
- Capturas: `academias-videos-desktop.png` y `academias-video-mobile.png`. No se enviaron datos de formularios.
