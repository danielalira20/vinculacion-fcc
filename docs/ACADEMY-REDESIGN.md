# Academias: referencias y decisiones

Revisión del 7 de octubre de 2026. Se conserva `pages.json` como registro de migración; la presentación estructurada está en `learning.json`. No se usa contenido inventado para sustituir flipbooks perdidos.

## Dirección fijada antes de implementar

Referencia dominante: [Podia en Refero Styles](https://styles.refero.design/style/342f1c3b-a123-49b6-a980-3491bc7793db): superficies cálidas, regiones de color con función, formas orgánicas y jerarquía de radios. Se conserva la paleta FCC (cream, rose, peach, lavender), Manrope y botones carbón. Los colores identifican academias/áreas; no se reutilizan como estados de éxito/error. Glass limitado a controles superpuestos, no a textos largos.

Patrón secundario: [Heptabase](https://styles.refero.design/style/7368cfab-6313-4e50-97e5-c3318c52e7fe), solo organización de biblioteca, controles segmentados y densidad interna. No se importa su azul ni sus grandes separaciones de marketing. [Syllabus](https://styles.refero.design/style/b78edcaa-6754-41d7-ac00-0119b41ad88a), solo mapas esquemáticos y jerarquía de información. No se importa su geometría rígida ni su verde.

Referencias del usuario: primera composición universitaria, hero dividido de Vespa y paneles sobre imágenes de sus referencias 2/4; mantener identidad FCC ya aprobada. Prioridad explícita: aprovechar espacio y convertir imágenes de contenido en HTML. Las reglas de espaciado y superficies de las referencias son adaptadas a esta prioridad. Investigación mediante la biblioteca pública Styles; no hay herramientas MCP de Refero disponibles en esta sesión.

## Decisiones

- Perfiles: el logo aparece en una placa compacta en la cabecera, nunca repetido a tamaño de cartel. Información y contacto en regiones anchas y cortas, sin columnas largas vacías.
- Oracle: biblioteca de ocho cursos transcritos del cartel `be4a26217a1d640a.png`, filtros por área, convocatoria de 2025 identificada como histórica. Los cinco flipbooks no recuperados no se simulan.
- AWS oferta: nueve cursos de `a23012c9e4ee4fa3.png`; sustituir el aviso de deslizar por búsqueda y filtros funcionales. Oferta terminada en febrero de 2026, conservar periodo, gratuidad y duración aproximada.
- AWS perfil: beneficios de `7f4d1b6dc533f05c.png` en panel por audiencia; insignia del programa pequeña. Video original integrado. No garantizar empleo por la frase promocional del cartel.
- Inscripción: proceso HTML de cuatro etapas sin duplicar el diagrama y la lista original; fechas históricas, requisitos, preguntas y preparación conservados.
- EC-Council: selector de tres programas y presentaciones Canva integradas; mapa de seis niveles de `05b61d5a075fdf71.png` convertido a HTML. El mapa es del catálogo general, no prueba de oferta local ni de prerrequisitos obligatorios.
- Formularios: revisar URLs originales; Oracle devuelve falta de permiso público. Mostrar el estado y contacto, no una inscripción ficticia. Conservar acceso opcional al proveedor.
- Accesibilidad: contenido completo sin JS, filtros y paneles como mejora progresiva, teclado, foco visible, texto >=16 px para lectura, movimiento reducido, ninguna decoración intercepta controles.

## Verificación requerida

Construcción y comprobaciones existentes, conservación de texto/recursos originales, validación de navegación y filtros en Chrome, inspección visual de las seis páginas y vista móvil. Carteles originales siguen como enlaces de consulta opcional, no como contenido central.

## Verificación realizada

- Construcción: 48 páginas. Validador de enlaces, importaciones y HTML aprobado. Siete comprobaciones de medios aprobadas, incluida la nueva dirección oficial `forms.cloud.microsoft` y el rechazo de dominios parecidos.
- Chrome: seis páginas inspeccionadas a 390 px y 320 px, sin desbordamiento horizontal. Catálogos: Oracle Java devuelve 3/8; AWS Datos e IA devuelve 4/9; búsqueda Generative devuelve 1/9; búsqueda sin resultados muestra ayuda; Todos restaura el catálogo.
- Programas EC-Council: cambio por clic y flecha derecha, presentación Canva correspondiente visible; expansión de Especialización muestra su contenido.
- Guía: lista de preparación operativa y proceso de cuatro pasos como HTML (solo el logo permanece como imagen), detalles individuales y control de grupo nativos.
- Microsoft Forms: el vínculo de AWS ha sido reutilizado por el propietario y ahora muestra Otoño 2026 y un registro por curso. Formulario integrado confirmado dentro de la página, sin enviar datos. La oferta transcrita sigue identificada como la publicación que finalizó en febrero de 2026. Oracle devuelve falta de permiso público; conservar el enlace y contacto sin prometer acceso.
- Registro original `pages.json`: sin modificaciones; activos originales conservados.

## Ampliación Cisco · referencia fijada antes de implementar

Se reutiliza la dirección Podia/Heptabase ya aprobada para que las tres páginas Cisco pertenezcan a Academias. Sage y arena como territorios; las cinco áreas se distinguen con los pasteles existentes. Logo pequeño, glass en la placa de datos, video original dentro del perfil y dibujos de nodos con SVG/CSS.

- Ruta: transcribir los 29 cursos de `d6492d35df2262dd.png` a cinco paneles con ramas, relaciones explícitas y glosario. Las agrupaciones son editoriales; no inventar un orden obligatorio. Mantener el mapa completo como consulta opcional para sus conexiones entre áreas y distintivos. No enlazar las antiguas páginas de `ciscointeractivepathways.com`: el dominio ahora muestra un anuncio de venta, comprobado en Chrome.
- Cursos con instructor: tres grupos, dos cursos, docentes, días, horas y fechas de Primavera 2023. Importe del cartel $1,800 identificado como histórico, sin inferir moneda ni vigencia. Cartel y formulario opcionales. Google muestra solo una vista previa al integrar el formulario, y pide cuenta para completar el registro con archivos; indicarlo sin simular un registro nuevo.
- Perfil: mismo hero compacto del resto de academias, dos modos de aprendizaje y acceso directo a las cinco rutas. Conservar YouTube, Facebook y los identificadores sociales del gráfico original. Sin carteles gigantes ni infografías como contenido central.

### Verificación Cisco

- 29 cursos transcritos; los 3 grupos conservan docentes, fechas y horarios del cartel. Registro original `pages.json` sin cambios. Mapa y cartel completos conservados como consulta opcional local.
- Chrome: cinco áreas operativas, cambio mediante flechas y acceso directo IT desde el perfil. Glosario desplegable confirmado.
- Filtros: SRWE devuelve 2 grupos; búsqueda Marco devuelve 1; búsqueda sin coincidencias muestra ayuda. Video original de Cisco presenta el reproductor de YouTube dentro de la página. Google muestra la vista previa histórica dentro del panel, sin enviar datos.
- Inspección visual de las tres páginas en computadora y a 390/320 px; desbordamiento de la portada a 320 px corregido en el grid. Conectores pasan a orientación vertical en celular.
- 48 páginas generadas; enlaces locales, importaciones y ausencia de emojis/procedencia antigua comprobados. Ocho pruebas de medios aprobadas, incluida la ruta exacta de Google Forms y rechazo de dominios parecidos.

## Navegación y comunidad · referencia fijada antes de implementar

Se conserva la dirección aprobada Podia/Heptabase y el encabezado glass existente. El respaldo `elementos-globales.json` fija las subsecciones originales: academias individuales, oferta/proceso/precios de certificaciones, empresas/vacantes, seguimiento/liberación/registro y áreas asociadas. Paneles de navegación con iconos del sistema, descripción corta, accesos de sección y agrupación en dos columnas; sin cambiar tipografía o introducir otra paleta. Despliegue nativo con `details`, control por clic/teclado y un panel por vez. En móvil, paneles dentro del menú con altura limitada y desplazamiento.

Facebook solo en Inicio y perfiles Cisco/Oracle, donde ya existe espacio de comunidad y hay una página publicada en el respaldo. Se utiliza el Page Plugin oficial con pestaña timeline, idioma español, sin facepile y carga diferida; no se copian ni simulan anuncios. Superficie cálida exterior y marco de lectura blanco: el contenido del proveedor conserva su presentación. Enlace opcional siempre disponible. Ancho de 180–500 px y actualización al cambiar el contenedor, conforme a la documentación oficial: https://developers.facebook.com/documentation/plugins/page-plugin. No hace falta SDK, credenciales ni un backend para estos paneles públicos. Refero MCP no está disponible; la investigación reutiliza las referencias fijadas de la biblioteca y los patrones ya aprobados, contrastados con el respaldo y la documentación del proveedor.

### Verificación navegación y Facebook

- Chrome: timeline real cargada en Inicio, Cisco y Oracle; los demás espacios de comunidad conservan acceso al perfil sin agregar otro iframe. El contenido externo conserva su formato y puede contener los emojis de sus autores; la interfaz FCC utiliza SVG y el validador comprueba ausencia de emojis en nuestro HTML.
- Navegación: los cinco submenús muestran destinos recuperados. Apertura mediante clic y Enter, navegación con Tab, un desplegable por vez, cierre por Escape/clic fuera y regreso del foco. En móvil, Escape cierra primero la subsección y después el menú general. Enlace Cisco comprobado desde el desplegable de Oracle.
- Inspección en computadora, 900 px, 390 px y 320 px sin desplazamiento horizontal. Frame a 320 px ajustado a 238 px, dentro de los límites del proveedor. Botón de menú compacto para que la cabecera permanezca en una fila. Se corrigió el cierre prematuro por transferencia de foco al summary antes de entregar.
- Capturas de revisión: `outputs/academy-review/navigation-community.png` y `facebook-community.png` en el directorio de trabajo.
- Comprobaciones finales aprobadas: 48 páginas, 2,314 referencias locales, exactamente 3 timelines de Facebook y 9 pruebas de medios.

## Videos en Inicio · ajuste sobre el componente aprobado

La captura del usuario muestra el grid de Inicio con iconos. Se conserva esa composición de cuatro tarjetas y se reutiliza la miniatura, controles glass y reproductor de la página Academias. Los cuatro videos son los originales ya recuperados; clic reproduce dentro de la tarjeta, un solo reproductor activo, cierre devuelve foco y acceso opcional a YouTube. El tamaño del componente se adapta al grid de Inicio, sin cambiar los tokens ni rediseñar el resto de la portada.
- Verificado en Chrome: cuatro miniaturas en Inicio; Cisco reproduce en la misma URL, cambiar a AWS deja un solo reproductor y volver a miniatura detiene el video y devuelve foco. Vista de 320 px sin desbordamiento, Oracle abre dentro de su tarjeta. Captura `outputs/academy-review/home-videos.png`. Construcción de 48 páginas y 9 pruebas de medios aprobadas.
