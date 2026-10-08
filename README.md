# Vinculación FCC · BUAP

Sitio del Departamento de Vinculación en revisión. HTML semántico, CSS nativo, JavaScript en módulos y Python con Jinja2 para generar páginas estáticas. No requiere WordPress, Node ni un servidor Python en producción.

## Repositorio y Visual Studio Code

Repositorio privado: [danielalira20/vinculacion-fcc](https://github.com/danielalira20/vinculacion-fcc). La rama principal es `main` y conserva el historial de cambios por funcionalidad.

En Visual Studio Code, usa **Archivo → Abrir carpeta** y selecciona `vinculacion-fcc`, la carpeta que contiene este README junto con `src/` y `scripts/`. Abre la carpeta completa para trabajar con el proyecto.

Para descargarlo en otro equipo con acceso al repositorio:

```sh
git clone https://github.com/danielalira20/vinculacion-fcc.git
cd vinculacion-fcc
code .
```

Después sigue los pasos de preparación de Python indicados abajo. `dist/` y `.venv/` se generan localmente y quedan excluidos de Git.

Al guardar un cambio, elige un mensaje convencional que describa su propósito, por ejemplo `feat(academias): añadir un catálogo de cursos`, `fix(navegacion): corregir el menú móvil` o `docs: actualizar la guía de instalación`. En **Control de código fuente**, revisa los archivos, crea el commit y sincroniza para subirlo a GitHub. Subir cambios al repositorio no publica el sitio.

## Abrir la versión generada

La carpeta `dist/` contiene el sitio listo para servir. Desde la carpeta del proyecto:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abre `http://127.0.0.1:8000`. Para usar búsqueda y módulos de JavaScript, abre el sitio mediante este servidor local, no con doble clic sobre el HTML.

## Preparar y generar el proyecto

Requiere Python 3.11 o posterior.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
python scripts/test_embeds.py
```

Cada generación reemplaza `dist/`. Edita `src/`, nunca `dist/`. La generación es local: no solicita información a servicios externos.

## Organización

```text
src/
  content/                 Información, navegación y procedencia
    site.json              Textos del inicio, tarjetas y servicios
    experiences.json       Portadas, identidades y accesos de las Academias
    employers.json         Bolsa de Trabajo y registros de Empresas/Vacantes
    processes.json         Procesos nativos y sus requisitos
    learning.json          Cursos, beneficios y programas transcritos a HTML
    cisco.json             Cinco rutas y grupos CCNA con sus horarios publicados
    coordinations.json     Directorio y presentaciones de las Academias
    embedded-resources.json Nombres de videos y materiales integrados
    pages.json             41 registros recuperados del sitio anterior
    media.json             Fotografías y logotipo del sitio original
    asset-sources.json     Relación entre recursos locales y sus fuentes
  templates/
    layouts/base.html      Estructura común
    components/            Encabezado, pie y tarjetas
    pages/                 Inicio, servicios, artículos y búsqueda
  assets/
    css/                   Valores visuales, estructura, componentes y páginas
    js/                    Navegación, filtros, búsqueda y movimiento
    icons/                 Iconos SVG propios
    fonts/                 Manrope y licencia OFL
    media/                 102 recursos recuperados y 18 vistas de la guía PDF
scripts/
  build.py                 Generación de HTML y del índice de búsqueda
  presentation.py         Procesos e iconos del contenido público
  embeds.py                Visores y normalización de recursos recuperados
  test_embeds.py           Pruebas de la migración multimedia
  check.py                 Comprobación de enlaces, archivos y estructura
  import_content.py        Importación manual del respaldo revisado
docs/
  DESIGN.md                Decisiones visuales y referencias
  ARCHITECTURE.md          Arquitectura y mantenimiento
  MIGRATION.md             Cobertura y asuntos pendientes
  ACADEMY-REDESIGN.md       Referencias de Refero y revisión de las Academias
```

## Qué incluye

- Portada, Academias, Certificaciones, Empresas, Egresados, Nosotros y Recursos.
- Menú móvil, filtros de Academias y búsqueda local que reconoce consultas sin acentos.
- Tarjetas de Academias con miniaturas y reproducción en la misma página; enlaces opcionales a la academia y a YouTube. Solo se carga un reproductor al pulsar y se detiene al ocultar su tarjeta.
- Bolsa de Trabajo y Vacantes con portadas propias, glass moderado y formularios integrados.
- Cinco flujos en HTML seleccionable con detalles desplegables; iconos SVG sin emojis en la interfaz.
- Coordinaciones con portada, directorio de contacto y galería de videos.
- Videos, presentaciones de Canva, siete formularios y guía PDF integrados en sus páginas.
- Catálogos filtrables: ocho cursos de Oracle y nueve de AWS; beneficios por audiencia, selector de programas EC-Council y mapa de formación en HTML.
- Cisco: cinco rutas con 29 cursos seleccionables, conexiones y glosario; tres grupos CCNA con fechas, horarios e instructores de Primavera 2023. Google permite una vista previa del formulario histórico, con acceso opcional al registro del proveedor.
- Guía de inscripción AWS compacta, lista de preparación y preguntas desplegables.
- Interfaz sin enlaces de procedencia ni dependencias del dominio que se retirará.
- Texto accesible de cuatro materiales gráficos revisados durante el respaldo.
- Notas de vigencia para precios y convocatorias históricas.
- Portadas con campos de color nude y pastel, formas curvas, fotografías y tarjetas superpuestas; textos más grandes y glass localizado.
- Sección de comunidad con accesos destacados a Facebook de Vinculación, Oracle y Cisco.
- Movimiento suave con respeto a la preferencia de reducir animaciones.

## Estado de la entrega

Es una versión de revisión, no una publicación oficial. La generación incluye `noindex` y `robots.txt` para evitar indexación accidental. Antes de publicar hay que validar responsables, contactos, precios, convocatorias, textos de carteles y materiales faltantes con el departamento; revisar el aviso de privacidad institucional aplicable; y definir dominio, alojamiento y redirecciones. La tabla `redirect-map.json` se genera como referencia, pero no configura el servidor por sí sola.

Los formularios integrados se sirven desde sus proveedores actuales y también ofrecen un enlace opcional para abrirlos aparte. El sitio no captura ni almacena datos personales. Moodle está pendiente de requisitos; todavía no hay cuentas, seguimiento de progreso ni sincronización con esa plataforma.

El proyecto se guarda en un repositorio privado de GitHub; el sitio todavía no está publicado. La investigación visual usa las referencias del usuario y Podia, Heptabase y Syllabus en la biblioteca pública de Refero Styles; ver `docs/ACADEMY-REDESIGN.md`. El acceso a investigación en vivo de Refero requiere una suscripción y no estuvo disponible durante esta revisión.

## Reimportar un respaldo

Solo cuando se quiera sustituir el contenido importado, instala las dependencias de migración y proporciona la carpeta del respaldo:

```sh
python -m pip install -r requirements-dev.txt
python scripts/import_content.py /ruta/al/respaldo-vinculacion-fcc
python scripts/build.py
python scripts/check.py
python scripts/test_embeds.py
```

Este paso sustituye `pages.json`, `media.json` y el mapa de recursos. Revisa los cambios antes de confirmar la nueva versión. El respaldo completo anterior se conserva separado de este proyecto.
