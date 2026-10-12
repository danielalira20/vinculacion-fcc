# Correcciones de la revisión de Diego

Revisión del 11 de octubre de 2026, hora de Ciudad de México. Se revisaron el texto y las catorce capturas de `Fcc.docx`, el proyecto abierto en Visual Studio Code, el respaldo del sitio anterior y los recursos públicos de sus proveedores.

Los problemas del sitio se corrigieron en `src/` y se regeneró `dist/`. Oracle y Cisco necesitan que sus coordinaciones confirmen un registro vigente. Los enlaces institucionales conservan sus direcciones oficiales: durante esta revisión no resolvieron desde la Mac, aunque la herramienta remota encontró las páginas de FCC y Diplomado. Su disponibilidad requiere revisión de la red o del servicio institucional.

## Observaciones y resultados

| Punto revisado | Causa comprobada | Cambio o estado |
| --- | --- | --- |
| Correo del inicio | `mailto` depende de una aplicación de correo configurada; un enlace válido puede parecer inactivo | Opciones de Gmail, Outlook, copiar dirección y aplicación de correo, disponibles en todas las páginas |
| Oracle Solicitar información | Enlace `mailto` al correo de la Academia | Abre las opciones con `coord_oracleacademia.fcc@correo.buap.mx` |
| Oracle formulario de registro | Microsoft Forms muestra que no se tiene permiso para verlo o responder | El formulario restringido deja de ofrecerse como registro; se solicita a la coordinación el acceso y el enlace del periodo |
| AWS Solicitar información | Enlace `mailto` al correo de la Academia | Opciones de correo con `academia.aws@correo.buap.mx` |
| Cisco próxima convocatoria y formulario de 2023 | El botón es de correo; los grupos y el formulario recuperados son históricos | Consulta con asunto específico; se retira el formulario 2023 de la interfaz, se mantienen los cursos identificados como históricos y los avisos de Cisco en Facebook |
| IT Inteligencia Artificial | El enlace reportado abrió un PDF; el catálogo oficial publica ahora otra dirección | Se usa la dirección del catálogo oficial, que abre `ITS OD 307 Artificial Intel 0426 (NEW).pdf` |
| IT Cybersecurity | Filecamp responde HTTP 200 pero muestra Archivo no encontrado | Destino oficial `fc/ITS/cybersecurity`, comprobado con el PDF `ITS OD 105 Cybersecurity 0525.pdf` |
| Otros temarios IT | Varios enlaces heredados dependían de direcciones de archivos compartidos | Se actualizan desde el catálogo oficial de Certiport; los quince temarios mostraron un archivo PDF en Chrome |
| MOS objetivos de cinco aplicaciones | Los cinco destinos de Certiport redirigen a la misma portada MOS | Doce destinos oficiales de Microsoft Learn, separados por aplicación, nivel y versión; Outlook muestra la versión 2019 que se pudo verificar |
| Correo de IT y MOS | Mismo comportamiento de `mailto` | Opciones de contacto con Vinculación en ambas páginas |
| Bolsa de Trabajo Consultar oportunidades y Conocer opciones | Los cuatro botones consultan por correo; no son una lista de vacantes | Opciones de contacto con Bolsa de Trabajo. Las tres tarjetas preparan asuntos distintos para empleo, prácticas y servicio social |
| Bolsa de Trabajo correo de coordinación | Enlace `mailto` al correo de Bolsa de Trabajo | Opciones de contacto con `bolsadetrabajo.fcc@correo.buap.mx` |
| Registro egresados Escríbenos | Enlace de correo del panel de ayuda | Opciones de contacto con Vinculación |
| Seguimiento correo | Enlace de correo del bloque de orientación | Opciones de contacto con Vinculación |
| FCC y Diplomado | Los dominios no resolvieron desde esta Mac; las direcciones oficiales aparecen en fuentes institucionales y la herramienta remota | Se conservan los enlaces oficiales. No se afirma una caída general ni se reemplazan por destinos de otra institución |
| AWS curso adicional encontrado al comparar | El formulario Otoño 2026 contiene diez opciones; el cartel histórico tenía nueve | Se incorpora Data Center Technician, se muestra Otoño 2026 como periodo del formulario y las condiciones del cartel anterior quedan separadas |

## Referencias y contraste

- Sitio anterior: `https://vinculacion.cs.buap.mx/`. Chrome mostró `DNS_PROBE_FINISHED_NXDOMAIN` desde esta Mac. La herramienta remota redirigió su `index.html` a una página institucional 404. Por ello, la comparación completa del contenido recuperado se hace contra el respaldo conservado del 6 de octubre, no se presenta como una nueva captura completa del sitio vivo.
- [FCC](https://www.cs.buap.mx/) y [Diplomado](https://diplomado.cs.buap.mx/) siguen siendo las direcciones institucionales encontradas. El acceso remoto y el resultado DNS local difirieron durante la revisión.
- [Catálogo oficial IT Specialist de Certiport](https://certiport.pearsonvue.com/Certifications/ITSpecialist/Certification/Certify): los destinos se toman de los enlaces de objetivos publicados en sus apartados. Cada destino final fue abierto en Chrome para verificar que entrega un PDF, no solo una respuesta HTTP 200.
- [Objetivos Excel Associate 2019](https://learn.microsoft.com/es-es/credentials/certifications/mos-excel-2019/) y las once páginas equivalentes de Excel Expert, Word, Outlook, PowerPoint y Access en Microsoft Learn. Las doce direcciones están registradas en `src/content/certifications.json` y fueron comprobadas mediante la herramienta de consulta web.
- Formulario AWS publicado: `https://forms.office.com/r/iEY2jMfJ4g`. Se verificaron su título Otoño 2026 y sus diez opciones en lectura. El formulario no muestra fechas de cierre ni confirma los costos del cartel histórico; esas condiciones requieren confirmación de la Academia.
- Formulario Oracle publicado: `https://forms.office.com/r/cHBckaBpNM`. Se comprobó la restricción en la página de Microsoft Forms; la web nueva no puede cambiar permisos del proveedor.

## Cobertura del respaldo

Se comprobó que los 41 registros recuperados siguen teniendo una ruta generada entre las 48 páginas del sitio. Todos los destinos de correo del contenido original siguen presentes en la interfaz: catorce direcciones distintas. `pages.json` conserva el contenido importado y las URL originales; los destinos sustituidos de IT y MOS se guardan además como `original_href`.

Este control de rutas, contactos y recursos no equivale a una revisión editorial palabra por palabra de una nueva versión del sitio institucional. Los pendientes materiales ya documentados continúan en `MIGRATION.md`: seis libros del plugin anterior sin archivos originales, material multimedia retirado o privado identificado en la migración, siete referencias de imágenes no recuperadas, y vigencia de carteles, precios y responsables. Necesitan archivos o confirmación del departamento.

## Decisiones de interfaz

Se mantiene el objetivo visual existente de `DESIGN.md` y las referencias de `ACADEMY-REDESIGN.md`: superficies marfil, Manrope, bordes cálidos y acciones carbón. Esta revisión corrige interacciones del producto existente.

| Decisión | Evidencia | Aplicación |
| --- | --- | --- |
| Elegir un método de correo sin depender de la aplicación instalada | Capturas de Diego y enlaces `mailto` válidos | Diálogo con opciones explícitas; destinatarios y asuntos preservados; `mailto` sigue funcionando sin JavaScript |
| Superficie sólida para leer opciones | Sistema visual aprobado, superficies de lectura en `DESIGN.md` | Panel marfil, texto carbón, acción secundaria con borde; glass solo en el fondo |
| Objetivos por versión con acceso compacto | Las doce páginas oficiales de Microsoft Learn | Desplegables nativos agrupados; abrir una tarjeta no estira sus vecinas |
| Separar registros históricos de consultas nuevas | Capturas, periodo 2023 de Cisco, restricción Oracle y título AWS Otoño 2026 | Sin fechas nuevas inventadas; los originales permanecen en los datos de revisión |

## Verificación

- Generación y comprobador de 48 páginas, enlaces locales, fragmentos, importaciones y accesibilidad básica.
- Nueve pruebas existentes de normalización de recursos y seis pruebas nuevas de regresión de esta revisión.
- Pruebas de destinos de correo: destinatarios, asuntos, acentos, saltos de línea, parámetros, codificación y rechazo de esquemas distintos a `mailto`.
- En Chrome: ocho accesos señalados por Diego, las tres consultas de Bolsa de Trabajo, copiar dirección, Tab, Shift+Tab, Escape y devolución de foco.
- En Chrome: quince temarios IT con PDF visible; selectores MOS específicos y una sola versión de aplicación desplegada a la vez.
- Páginas Oracle, AWS, Cisco y MOS a 320 píxeles sin desbordamiento horizontal. Diálogo de correo revisado a 320 y 390 píxeles; vista normal restablecida al terminar.

Comandos para repetir las comprobaciones locales:

```sh
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
.venv/bin/python scripts/test_embeds.py
.venv/bin/python scripts/test_review_regressions.py
node scripts/test_email.mjs
```

Node solo se usa para la prueba opcional del módulo de correo; no es necesario para generar o servir el sitio.
