# Vinculación FCC · BUAP

Primera versión local del nuevo sitio del Departamento de Vinculación. HTML semántico, CSS nativo, JavaScript en módulos y Python con Jinja2 para generar páginas estáticas. No requiere WordPress, Node ni un servidor Python en producción.

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
```

## Qué incluye

- Portada, Academias, Certificaciones, Empresas, Egresados, Nosotros y Recursos.
- Menú móvil, filtros de Academias y búsqueda local que reconoce consultas sin acentos.
- Bolsa de Trabajo y Vacantes con portadas propias, glass moderado y formularios integrados.
- Cinco flujos en HTML seleccionable con detalles desplegables; iconos SVG sin emojis en la interfaz.
- Coordinaciones con portada, directorio de contacto y galería de videos.
- Videos, presentaciones de Canva, cinco formularios y guía PDF integrados en sus páginas.
- Interfaz sin enlaces de procedencia ni dependencias del dominio que se retirará.
- Texto accesible de cuatro materiales gráficos revisados durante el respaldo.
- Notas de vigencia para precios y convocatorias históricas.
- Portadas con campos de color nude y pastel, formas curvas, fotografías y tarjetas superpuestas; textos más grandes y glass localizado.
- Sección de comunidad con accesos destacados a Facebook de Vinculación, Oracle y Cisco.
- Movimiento suave con respeto a la preferencia de reducir animaciones.

## Estado de la entrega

Es una versión de revisión, no una publicación oficial. La generación incluye `noindex` y `robots.txt` para evitar indexación accidental. Antes de publicar hay que validar responsables, contactos, precios, convocatorias, textos de carteles y materiales faltantes con el departamento; revisar el aviso de privacidad institucional aplicable; y definir dominio, alojamiento y redirecciones. La tabla `redirect-map.json` se genera como referencia, pero no configura el servidor por sí sola.

Los formularios se abren mediante enlaces a sus proveedores actuales. El sitio no captura ni almacena datos personales. Moodle está pendiente de requisitos; todavía no hay cuentas, seguimiento de progreso ni sincronización con esa plataforma.

El repositorio es local. No se ha creado un repositorio remoto ni publicado el sitio. Refero no está conectado: se usaron las referencias visuales compartidas en la conversación.

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
