# Nueva sección: Cultura Digital · ECM0121

## Qué cambia
- Se eliminan visualmente las seis ofertas originales; se presenta una sola certificación.
- Se muestran competencias, ruta de certificación, PDF informativo y registro a Microsoft Forms.
- El QR se generó a partir de la URL **larga** compartida por Yara, de forma que botón y QR apuntan al mismo enlace.
- No se inventan precios, fechas, duración ni modalidad: no aparecen en el brochure.

## Ver la demostración
Abre `vista-previa-cultura-digital.html` en tu navegador (sin instalar nada). Conserva `assets/` en la misma carpeta.

## Integración en vinculacion-fcc
No editamos el repositorio real porque sus archivos de código no se han adjuntado en esta conversación.

En el repositorio original se trabajaba en:
- `src/templates/pages/continuing-education.html`
- `src/assets/css/continuing-education.css` o el archivo de CSS equivalente
- `src/assets/js/continuing-education.js` o equivalente
- `src/data/continuing-education.json` o la ruta de datos del proyecto

1. En el template de Educación Continua, sustituye la sección de las seis tarjetas y sus filtros por el contenido de `seccion-cultura-digital.html`.
2. Carga la hoja `cultura-digital.css` y ubícala donde se copien los estilos al sitio publicado.
3. Copia la carpeta `assets/` a una ubicación servida y ajusta las referencias relativas si es necesario.
4. Retira la lógica JS que depende de seis categorías/filtros y actualiza la fuente de datos: no deben seguir ofertándose otras opciones en la página ni en enlaces relacionados.
5. Ejecuta `python scripts/build.py` (o el comando de build indicado por el repo) y revisa la ruta generada `dist/educacion-continua/index.html`.

**No editar directamente `dist/`**, ya que se regenera al compilar.

## Enlace de registro
https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=OjGYGihHnE6az7bSE1NX-201xb0ugutLt-0fzh3tsapUMzZFMFhVWkFaS0cxSEUyRkFEVVdXQ05NTS4u
