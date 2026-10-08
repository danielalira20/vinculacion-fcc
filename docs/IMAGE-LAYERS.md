# Imágenes y profundidad · 7 de octubre de 2026

Corrección directa sobre las capturas del usuario y la dirección FCC aprobada. Dominante: Podia / territorios FCC; referencias del usuario 2/3/4: imagen con placas glass. Conservar estructura, color, iconos y logo de Academias, introducir fotografía representativa bajo las formas. Glass pertenece a controles/placas, no al texto extenso. Sin letras gigantes de fondo.

| Decisión | Fuente y función | Aplicación |
| --- | --- | --- |
| Fondos temáticos en academias | Solicitud explícita de imagen representativa tenue; referencias fotográficas del usuario | Cisco: equipo de redes; AWS: servidores; EC-Council: trabajo de seguridad. Imágenes ilustrativas generadas, no fotos de instalaciones BUAP ni material oficial de marca |
| Capa de color suave | Usuario, superficies FCC | Fotografía visible, atenuada bajo icono central y placas glass; sin difuminar el cuerpo de lectura |
| Foto real de comunidad en empresa/vacante | Activo original FCC y petición de rehacer composición | Sustituye papel ficticio y tres etiquetas; nota glass compacta sobre fotografía original de participantes Oracle |
| Información de registro en regiones | Captura de texto excesivamente plano | Párrafos originales completos, introducción, cifra publicada, relación/comunidad y convenios; acción al formulario |

Herramienta de imágenes: integrada, sin CLI/API. Prompts y archivos definitivos se registrarán tras generación. No se presentan imágenes generadas como instalaciones reales ni como fotografías oficiales de las academias.

## Archivos y prompts finales

Generados con la herramienta integrada y copiados al proyecto sin modificar el bitmap. Archivos definitivos:

- Cisco: `/Users/danielalira/Documents/Codex/2026-10-06/ho/outputs/vinculacion-fcc/src/assets/media/academy-cisco-background.png`
- AWS: `/Users/danielalira/Documents/Codex/2026-10-06/ho/outputs/vinculacion-fcc/src/assets/media/academy-aws-background.png`
- EC-Council: `/Users/danielalira/Documents/Codex/2026-10-06/ho/outputs/vinculacion-fcc/src/assets/media/academy-security-background.png`

Prompt Cisco:

> Use case: photorealistic-natural. Asset type: thematic background for a university networking academy hero, illustrative generic scene rather than actual campus. Editorial photograph, close-up of an unbranded network switch and neatly connected ethernet cables in a clean learning lab, equipment recognizable and realistically built. Natural soft daylight, desaturated sage and warm gray, subtle depth of field. Square composition, equipment across lower and middle frame; no people needed. No text, logos, watermarks, UI, graphic overlays or borders. Create the photograph only; CSS will add a translucent layer.

Prompt AWS:

> Use case: photorealistic-natural. Asset type: illustrative cloud-computing academy background, generic scene rather than actual campus. Editorial architectural photograph of a modern data center aisle, softly illuminated server racks, realistic hardware, warm amber and muted slate light, restrained cinematic depth and clean bright atmosphere. Square composition with recognizable racks spanning frame. No text, logos, brand names, watermarks, people, holograms, cloud icons, graphic overlays or borders. Create the photograph only; CSS will add a translucent layer.

Prompt EC-Council:

> Use case: photorealistic-natural. Asset type: illustrative cybersecurity academy background, generic scene rather than actual campus. Editorial photograph over the shoulder of a professional in ordinary neutral clothing working on a laptop in a modern bright security lab. Laptop shows an abstract dark technical interface with subtle small lines, no legible words. Focus on hands, keyboard and screen; face not visible. Muted lavender gray with natural daylight, realistic textures and softly focused background. Square composition. No logos, text, watermarks, padlock icons, holograms, hooded hacker imagery, graphic overlays or borders. Create the photograph only; CSS will add a translucent layer.

Oracle conserva su foto real original. Empresas/vacantes reutilizan `assets/media/7118299c6cf4f0fd.jpg`, fotografía original del sitio de participantes Oracle; el alt conserva ese contexto. Los fondos nuevos son decoración temática, con alt vacío; no implican instalaciones reales ni actividad de marca.

## Verificación realizada

- 48 páginas y 2362 referencias locales aprobadas; todos los párrafos de empresas/registro y vacantes preservados literalmente, comparación con HTML generado.
- Chrome escritorio: Cisco, AWS, EC-Council y Empresas inspeccionados visualmente; fondos cargados, iconos y logos legibles, contraste de lectura intacto.
- Móvil: empresas y EC-Council inspeccionados a 390 px; cinco páginas modificadas sin desbordamiento horizontal a 320 px. Vista de escritorio restaurada.
- Botón Registrar mi empresa llega a `#formulario` y el iframe original permanece disponible. Sin enviar datos.
- Capturas reales: `outputs/academy-review/cisco-fondo-glass.png`, `empresas-portada-fotografia.png`, `empresas-informacion-regiones.png`.
