# Comprobaciones de la primera versión

## Generación y archivos

- 48 páginas HTML generadas a partir de 41 registros recuperados y las páginas nuevas de presentación y búsqueda.
- Comprobación de 1300 destinos locales entre páginas, imágenes, estilos, scripts y fragmentos de navegación.
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
