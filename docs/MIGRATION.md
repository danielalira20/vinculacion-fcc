# Migración del contenido

Origen: `https://vinculacion.cs.buap.mx/index.html`. Respaldo revisado el 6 de octubre de 2026.

Esta entrega importa los 41 registros agrupados del respaldo: 33 páginas/entradas, inicio y siete listados. Genera 48 páginas HTML al añadir las portadas de servicios y búsqueda. Incluye 102 recursos locales de contenido, fotografías, logotipo y PDF; no incluye los scripts, temas ni plugins del WordPress anterior.

El texto original de cada registro permanece en `src/content/pages.json`. El respaldo completo de 419 archivos originales continúa conservado en la carpeta separada `respaldo-vinculacion-fcc`; esta nueva web no reemplaza ese respaldo.

## Adaptación

- Las secciones principales tienen portadas propias y rutas legibles.
- El texto de las páginas interiores se conserva en HTML simplificado y sin estilos del tema anterior.
- Las imágenes recuperadas se sirven localmente. La interfaz utiliza las fotografías y el logotipo del sitio original, no las capturas de Pinterest.
- Cuatro transcripciones revisadas contra imagen se muestran como texto adicional en compra de certificaciones, precios, registro de empresas y liberación.
- Los demás carteles conservan sus originales. El OCR automático permanece como dato de referencia y todavía necesita revisión humana antes de convertirlo en texto oficial.
- Los formularios y servicios externos mantienen sus enlaces. No se crean formularios nuevos ni se hacen envíos de prueba.
- Los listados históricos y la entrada residual `cache` se mantienen en el archivo de Recursos, no en el menú principal.
- Los códigos del plugin de libros se retiran de la presentación; los documentos correspondientes siguen pendientes.
- Los avisos de fechas vencidas aparecen en Cisco, Oracle y AWS; los precios de marzo de 2025 tienen un aviso específico.

## Pendientes materiales

1. Libros de Oracle (IDs 1839, 1831, 1829, 1836, 1834) y oferta AWS (ID 1926): pedir archivos originales al departamento.
2. Fotografía `FCC-2025-64`: la dirección publicada no entrega una imagen válida.
3. Seis imágenes externas no incluidas en el respaldo: logotipos pequeños y material de Certiport, imagen de un artículo y decoración de una ruta Cisco. Sus referencias se registran en `migration-warnings.json`; no se sustituyen con imágenes inventadas.
4. Revisar todos los carteles con OCR pendiente, vigencia de contactos y costos, los formularios completos y el acceso restringido del formulario Cisco.
5. Confirmar el correo de compra: un cartel escribe `vinculación` con acento y el sitio usa `vinculacion`. El contacto común conserva la dirección sin acento publicada en textos y formularios; la transcripción mantiene la diferencia documentada.
6. Validar el texto de Academias: una publicación menciona tres pero enumera cuatro. La nueva portada muestra las cuatro academias presentes; el texto original permanece para revisión.
7. Revisión editorial de residuos del tema, enlaces institucionales, avisos legales y rutas históricas antes de publicar.

Los hallazgos completos, las transcripciones verificadas y el esquema visible de formularios se incluyen en `docs/`. Esta es una primera versión funcional y visual; no se afirma que todos los documentos pendientes ya estén recuperados ni que las convocatorias sean vigentes.
