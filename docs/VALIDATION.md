# Comprobaciones de la versión actual

## Generación y archivos

- 48 páginas HTML generadas a partir de 41 registros recuperados y las páginas nuevas de presentación y búsqueda.
- Comprobación de 1312 destinos locales entre páginas, imágenes, estilos, scripts y fragmentos de navegación.
- Verificación de importaciones CSS y JavaScript, identificadores HTML únicos, un título principal por página, idioma español y región principal de contenido.
- Sin manejadores de eventos inline, scripts del WordPress anterior ni iframes de terceros en el contenido importado.
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
