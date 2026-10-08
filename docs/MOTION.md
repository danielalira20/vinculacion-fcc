# Movimiento discreto · 7 de octubre de 2026

Ampliación de la dirección FCC aprobada: conservar las superficies, fotos, glass y composición existentes. Referencias fijadas en HOME-NETWORK-REDESIGN.md y CERTIFICATIONS-REDESIGN.md; guía de oficio `refero-design/references/motion.md` para tiempos, continuidad y respuesta. Refero en vivo no disponible por suscripción; no se atribuyen nuevas referencias a una búsqueda en vivo.

| Decisión | Fuente / función | Límite |
| --- | --- | --- |
| Logo seleccionado con relieve y ficha con entrada breve | Usuario, composición Skillfire ya aprobada, guía de feedback | Selección manual, 3 px, sin bucle ni avance automático |
| Acercamiento de fotografía y flecha al enfocar tarjetas | Usuario, fotos originales, guía de microinteracciones | Escala 1.025, controles y texto estables; teclado y puntero |
| Apertura suave de navbar | Guía de continuidad, menú nativo existente | 6 px, 200 ms, sin retrasar enlaces ni cierre |
| Tiempos compartidos | Guía de movimiento | 140 ms feedback, 200 ms cambios de estado; propiedades explícitas |

Implementación nativa CSS, sin librerías adicionales. Todas las nuevas reglas de movimiento se limitan a `prefers-reduced-motion: no-preference`. Las interacciones permanecen inmediatas y accesibles cuando el usuario reduce el movimiento. El contenido no depende de la animación para mostrarse.

## Validación

- Generación de 48 páginas y comprobación de 2353 referencias locales aprobadas.
- Chrome: fotografía de IT responde al foco con escala 1.025 y transición de 200 ms; desplegable usa entrada de 200 ms; Escape cierra inmediatamente y devuelve foco al resumen.
- Convenios: clic en Oracle y Enter en Volkswagen, una sola ficha visible, selección y relieve de 3 px correctos.
- Menú y submenú móvil a 390 px funcionan; sin desbordamiento a 390 y 320 px. Vista de escritorio restaurada.
- Revisión de CSS: todas las animaciones nuevas están dentro de la consulta de movimiento permitido; la regla global de movimiento reducido anula animaciones y transiciones. No se cambió la preferencia del sistema para la prueba.
- Captura real: `outputs/academy-review/animaciones-navbar.png`.
