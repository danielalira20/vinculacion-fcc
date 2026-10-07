# Dirección visual · Vinculación FCC

## Intención

Una web cálida, contemporánea y cercana: tonos nude, espacio suficiente, fotografías, tipografía con presencia y detalles pastel. La identidad institucional se mantiene mediante el logotipo de Vinculación, el nombre de la Facultad y sus enlaces oficiales. No se impone el azul como fondo dominante.

## Referencias seleccionadas por la usuaria

Numeración según las trece imágenes compartidas en la conversación:

| Referencia | Decisión aplicada |
| --- | --- |
| 1 · Oxford | Fotografía protagonista, navegación ligera y composición editorial |
| 2 · Orizon | Composiciones contenidas, tarjetas superpuestas y una placa de glass sobre imagen |
| 3 · Vespa | Título e imagen en una portada continua, módulos que se encajan y accesos integrados |
| 4 · Travorra | Curvas amplias en fotografías, serif editorial y accesos destacados |
| 8 · Q2 planning | Marfil, arena, calidez y contraste con elementos oscuros |
| 9 · Custom Syllabus | Lavanda, rosa y salvia; bordes suaves y uso localizado de transparencia |
| 10 · Hippo Campus | Tarjetas de catálogo con jerarquía y estructura constantes |
| 11 · JAAC | Organización por servicios, presentación, recursos y contacto |
| 12 · Industrial | Una tarjeta con glass sobre fotografía |
| 13 · UCLA | Información de trámites conservada para futuras guías de pasos |

Las capturas inspiran decisiones, no se publican como imágenes del sitio ni se copian sus marcas, textos o funciones ficticias.

## Paleta

El archivo central es `src/assets/css/tokens.css`.

| Función | Valor |
| --- | --- |
| Fondo marfil | `#F7F4EF` |
| Superficie clara | `#FFFDFA` |
| Texto carbón cálido | `#292724` |
| Texto secundario | `#68635D` |
| Arena | `#E8DED2` |
| Salvia | `#DFE7DD` |
| Durazno | `#F0DECE` |
| Rosa empolvado | `#EAD7D3` |
| Lavanda | `#DEDBEA` |
| Foco de teclado | `#17354A` |

Los pasteles distinguen áreas y fondos decorativos; no sustituyen nombres ni estados textuales. Los botones principales mantienen carbón y texto blanco en todas las secciones. Evitar texto blanco sobre pastel.

## Tipografía y composición

- Manrope variable, alojada localmente, para navegación, texto y títulos. Licencia OFL incluida.
- Georgia en cursiva para una frase editorial breve dentro de títulos de portada.
- Contenedor máximo de 1240 px; cuatro tarjetas en escritorio, dos en tablet y una en móvil estrecho.
- Radios de 12, 24 y 36 px según escala; botones redondeados.
- Texto general de 17 px; descripciones de portada de 17–18 px, botones de 15 px y etiquetas de al menos 12 px.
- La frase de portada «Un vínculo entre tu formación…» usa 15 px en escritorio y 14 px en móvil.
- Inicio, las cinco secciones principales, Nosotros y las cuatro Academias tienen composiciones propias: campos de color, curvas, órbitas, mosaicos y tarjetas superpuestas.
- Información importante sobre superficies sólidas y con espacio para leer. Los documentos y contenidos históricos permanecen completos.

## Glass y movimiento

Glass limitado al encabezado y las placas sobre las fotografías o composiciones de las Academias. `backdrop-filter` tiene una alternativa de fondo opaco. No se aplica blur a párrafos, precios, requisitos ni procedimientos.

Transiciones de 180–280 ms en interacción; aparición única de 500 ms con desplazamiento de 14 px en unas pocas secciones. El contenido sigue visible sin JavaScript. `prefers-reduced-motion` elimina movimiento; no hay animaciones continuas, reproducción automática, scroll forzado ni cursor personalizado.

## Comunidad y redes

Facebook aparece como una sección visual de comunidad en Inicio, Academias, Egresados y Nosotros, y como una tarjeta propia en Oracle y Cisco. Se usan los destinos publicados por el sitio original. Son accesos a perfiles oficiales, no un feed incrustado ni publicaciones inventadas. AWS y EC-Council muestran sus contactos institucionales sin asignarles cuentas sociales no verificadas.

`experiences.json` centraliza los textos, temas y accesos de estas portadas; `editorial.css` añade sus composiciones sobre la estructura compartida. Las fotografías son recursos recuperados, no las capturas de inspiración.

## Próxima revisión con Refero

Comparar una referencia principal de color/tipografía, una de catálogo y una de glass. Documentar la adaptación aquí antes de modificar los valores comunes. Cualquier DESIGN.md externo se usa como material de referencia, no reemplaza estas decisiones ni las instrucciones de la usuaria. Comprobar legibilidad, versión móvil y consistencia de botones tras cada cambio.

## Coordinaciones y materiales

Portada arena/salvia con círculos decorativos y cuatro piezas pastel inclinadas con los logotipos recuperados. Directorio en tarjetas amplias con fotografías existentes, símbolos para las coordinaciones sin retrato, ubicación y correo legible. La galería conserva las mismas curvas y superficies cálidas. Los visores usan un marco sólido para proteger la legibilidad del contenido del proveedor; no se aplica glass sobre videos, documentos o formularios.

## Bolsa de Trabajo y registro de oportunidades

La Bolsa de Trabajo utiliza una red visual nativa que conecta Talento FCC con empleo, prácticas y servicio social. Vacantes y Empresas usan una pieza editorial en forma de tarjeta inclinada, con pequeñas superficies glass superpuestas. Las ilustraciones se dibujan con HTML, CSS e iconos locales, para que texto y formas se adapten al tamaño de pantalla. Los formularios conservan superficies sólidas y legibles.

Los procesos se convierten en tarjetas conectadas y numeradas. Cada tarjeta permite consultar detalles, requisitos y acciones correspondientes. El glass se reserva a acentos sobre fondos cálidos; la animación aparece en hover y revelado, respetando la preferencia de movimiento reducido.

Regla de la usuaria: PROHIBIDO EMOJIS en la interfaz. Usar iconos SVG locales. Los símbolos heredados se sustituyen durante la generación; las copias históricas permanecen como respaldo.
