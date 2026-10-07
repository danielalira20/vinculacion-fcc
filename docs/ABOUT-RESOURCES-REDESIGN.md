# Labor, equipo y biblioteca

## Referencias y decisiones previas a implementación

Se mantiene el reference lock de ACADEMY-REDESIGN.md: Podia como dirección dominante (territorios cálidos, esquinas orgánicas, Manrope/Georgia); Heptabase únicamente para densidad y navegación de biblioteca; Syllabus únicamente para conexiones nativas. Las imágenes proporcionadas por la usuaria aportan composición dividida (Vespa), fotografía institucional (Oxford) y la idea de tarjetas recorribles (carrusel de destinos). No se mezcla su paleta azul ni su ornamentación turística.

Refero MCP respondió NO_SUBSCRIPTION a las tres consultas de estilos de esta sesión. No se atribuyen nuevas referencias a resultados inaccesibles. Se usan las referencias ya revisadas y los principios de craft del skill.

- Labor: fotografía original en composición dividida y diagrama HTML de comunidad, Vinculación y sectores. Dos párrafos originales visibles; sin cifras ni alianzas inventadas.
- Coordinaciones: directorio compacto con dos tarjetas en la primera fila y tres en la segunda; retratos pequeños, nombres y cargos visibles. Contactos desplegables nativos con un panel abierto a la vez. Cinco integrantes originales y tres contactos adicionales del directorio; iniciales para Educación Continua, que no tiene retrato publicado.
- Recursos: portada compacta y tres guías destacadas; catálogo completo de destinos existentes con búsqueda sin sensibilidad a acentos y filtros de sección. Archivo separado y accesible, sin enlaces al sitio que será retirado.
- Glass reservado a detalles sobre fotos, contenedores sólidos para texto largo. Formas y líneas explican conexiones; iconos SVG, sin emojis. Todos los materiales quedan accesibles sin JavaScript. Movimiento reducido respetado.

## Verificación

- Construcción: 48 páginas; comprobador de enlaces, HTML, importaciones y ausencia de emojis y destinos del sitio retirado aprobado. Nueve pruebas de medios aprobadas.
- Conservación: párrafos originales de Labor y Coordinaciones, cinco nombres/cargos originales, cuatro retratos originales. Todos los correos añadidos coinciden con el directorio de Nosotros. Catálogo con 32 destinos y nueve entradas históricas, mismos destinos que antes.
- Chrome de escritorio: revisión visual de las tres composiciones; fotografía y retratos cargados. Directorio: contactos abiertos por clic y Enter, cierre del panel anterior al abrir otro, información conservada y cinco coordinaciones visibles juntas en escritorio.
- Búsqueda: Oracle devuelve dos resultados; cadena inexistente devuelve cero y muestra recuperación; limpiar restaura 32; Academias devuelve diez; «inscripcion» encuentra «inscripción».
- Revisión a 390 y 320 px: sin desbordamiento horizontal global, tarjetas de una columna y correos ajustados. El directorio pasa a una columna; correos largos se ajustan incluso a 320 px. Tamaño de navegador restaurado tras la prueba.
- Datos de equipo y biblioteca separados en archivos JSON; estilos acotados a estas tres páginas. Sin cambios de paleta o navegación global.


## Revisión del directorio tras comentarios de la usuaria

La captura señala que una tarjeta individual y su retrato dominan la pantalla. Se fija una composición compacta sin carrusel: dos tarjetas de cabecera y tres debajo en escritorio, con retratos pequeños, nombres legibles y contacto desplegable nativo. Se conserva la dirección Podia ya investigada; las referencias de tarjetas compactas de cursos y mosaico educativo aportadas por la usuaria orientan la densidad. La información permanece completa, sin ocultar nombres o funciones ni inventar fotografías. Encabezado más corto, glass en el panel de contacto y movimiento solo al interactuar. Se elimina el módulo y el CSS del carrusel.

Verificación de la revisión: construcción y enlaces aprobados; cinco nombres/cargos y todos los correos conservados, apertura/cierre nativos comprobados en Chrome, vistas de 390 y 320 px sin desbordamiento, captura `outputs/academy-review/coordinaciones-compactas.png`.
