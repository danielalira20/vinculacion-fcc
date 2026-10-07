# Dirección visual · Vinculación FCC

## Intención

Una web cálida, contemporánea y cercana: tonos nude, espacio suficiente, fotografías, tipografía con presencia y detalles pastel. La identidad institucional se mantiene mediante el logotipo de Vinculación, el nombre de la Facultad y sus enlaces oficiales. No se impone el azul como fondo dominante.

## Referencias seleccionadas por la usuaria

Numeración según las trece imágenes compartidas en la conversación:

| Referencia | Decisión aplicada |
| --- | --- |
| 1 · Oxford | Fotografía protagonista, navegación ligera y composición editorial |
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
- Información importante sobre superficies sólidas y con espacio para leer.

## Glass y movimiento

Glass limitado al encabezado y la tarjeta sobre la fotografía de portada. `backdrop-filter` tiene una alternativa de fondo opaco. No se aplica blur a párrafos, precios, requisitos ni procedimientos.

Transiciones de 180–280 ms en interacción; aparición única de 500 ms con desplazamiento de 14 px en unas pocas secciones. El contenido sigue visible sin JavaScript. `prefers-reduced-motion` elimina movimiento; no hay animaciones continuas, reproducción automática, scroll forzado ni cursor personalizado.

## Próxima revisión con Refero

Comparar una referencia principal de color/tipografía, una de catálogo y una de glass. Documentar la adaptación aquí antes de modificar los valores comunes. Cualquier DESIGN.md externo se usa como material de referencia, no reemplaza estas decisiones ni las instrucciones de la usuaria. Comprobar legibilidad, versión móvil y consistencia de botones tras cada cambio.
