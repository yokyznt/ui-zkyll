---
name: ui-zkyll
description: Use when building, redesigning or improving any web UI. Pulls from 360 reference designs (navegación, texto, interruptores, cargas, cursor, fondos, scroll, galerías, transiciones, íconos, 3D, generativo, imagen y video, diagramas, portadas), adapts them to the project, and chains the web design skills of this package.
---

# UI Zkyll

Biblioteca de 360 diseños animados de referencia (HTML/CSS/JS sin framework) + el paquete de skills de diseño web. Al crear o mejorar una web: primero buscar referencia aquí, luego adaptar, luego revisar con las skills de calidad.

## Dónde está el código

Los 360 diseños vienen dentro de la skill, en `recursos/<categoría>/<slug>/moxen-<slug>/` (`index.html` demo, `<slug>.css`, `<slug>.js`, `README.md`). Se resuelve en este orden: `$ZKYLL_RECURSOS`, `recursos/` junto a esta skill, `D:\moxenecursos`. Si no existe ninguna: `python scripts/descargar.py` (cupón público de Moxen; acepta categorías como argumentos).

## Libertad creativa (modo por defecto)

El usuario no va a nombrar los diseños: elige tú. Para cada página nueva o rediseño:
1. Decide un concepto visual y una sola idea de movimiento que lo sostenga.
2. Escoge los diseños que lo sirvan en cada sección (portada, navegación, texto, fondo, scroll, galería, cursor, transiciones, cargas, íconos, 3D, generativo, imagen y video, diagramas, interruptores). Mezcla categorías, combina dos diseños en una sección si suma, y deja secciones quietas para dar aire.
3. Instálalos en el proyecto de una vez: `python scripts/usar.py <carpeta_del_proyecto> slug1 slug2 ...` copia cada uno a `<proyecto>/zkyll/<slug>/` (sin licencia), imprime sus `<link>`/`<script>` y deja `demo-main.html` con el marcado de la demo.
4. Integra: pega el marcado en la página, enlaza css/js, reemplaza textos, fotos y variables CSS por los del concepto, unifica tipografía y color entre diseños. No dejes un collage: todo debe verse de la misma mano.
5. Cuenta en el reporte final qué diseños usaste y dónde, en una línea cada uno.

## Flujo

1. Entender el pedido y la dirección visual (marca, tono, público). Si es algo nuevo y vago, cargar `brainstorming` o `design-taste-frontend` antes de elegir efectos.
2. Mapear cada parte de la página a una categoría:

| Parte de la web | Categoría (`catalogo/<c>.md`) |
|---|---|
| menús, tabs, breadcrumbs, barras | `navegacion` |
| títulos, párrafos, revelados, contadores | `texto` |
| toggles, switches, selectores | `interruptores` |
| spinners, skeletons, progreso | `cargas` |
| cursor personalizado, seguidores | `cursor` |
| fondos animados, mallas, partículas | `fondos` |
| scroll suave, parallax, pinned, progreso de scroll | `scroll` |
| carruseles, grids de imágenes, lightbox | `galerias` |
| cambios de página/estado/vista | `transiciones` |
| íconos animados, morphing | `iconos` |
| escenas y objetos 3D, tilt, WebGL | `tresd` |
| arte generativo, shaders, ruido | `generativo` |
| imagen, video, compare, zoom, reproductores | `media` |
| flujos, organigramas, líneas de tiempo, esquemas | `diagramas` |
| hero, carátulas, portadas, intros | `portadas` |

3. Buscar: `python scripts/buscar.py <palabra> [palabra]` (busca en nombre, frase y dependencias) o leer `catalogo/<categoría>.md`. Elegir 1–3 candidatos, no más: coherencia antes que cantidad.
4. Leer el `README.md`, el `.css` y el `.js` de cada candidato elegido (solo esos), o instalarlo con `usar.py` y leerlo ya copiado. Abrir `index.html` en el navegador si hay duda de cómo se ve.
5. Adaptar, no pegar:
   - Reemplazar colores, tipografías y medidas por los tokens del proyecto (los diseños declaran variables CSS al inicio).
   - Renombrar clases al esquema del proyecto; quitar lo que no se use; cambiar el texto de demostración y las fotos de `img/` (son de muestra).
   - Si el proyecto usa React/Vue/Tailwind, portar la lógica (el JS es vanilla) a un componente/hook, no incrustar el demo.
   - Dependencias (GSAP, three, etc.): usar las que ya tenga el proyecto; si el diseño dice `Ninguna`, mantenerlo así.
   - Si el proyecto no lleva comentarios en el código, quitar los del recurso.
6. Respetar siempre: `prefers-reduced-motion` (versión estática o más calma), foco visible y teclado, contraste, animar solo `transform`/`opacity`, 60 fps, que funcione en móvil (sin hover como única vía), y que no suba el peso ni el CLS/LCP.
7. Verificar en navegador real (`playwright-cli`): capturas a 1280 px y 390 px, consola sin errores, la animación realmente corre. No decir «listo» sin ver la captura.

## Mejorar una web existente

1. Recorrer la página sección por sección y anotar qué es plano o genérico (menú sin estado activo, spinner por defecto, títulos que aparecen de golpe, fondo vacío, cursor estándar, galería estática, cambio de página brusco, hero sin identidad).
2. Para cada punto, proponer un diseño de la categoría correspondiente y adaptarlo. Un solo gesto distintivo por sección; el resto sobrio (`subtractive-design`, `minimalist-ui`).
3. Si hay muchas mejoras, entregar primero 2–3 de mayor impacto (hero/portada, navegación, scroll) y luego el resto por rondas.

## Skills del paquete que se encadenan

| Necesidad | Skill |
|---|---|
| Dirección visual y anti-genérico | `design-taste-frontend`, `taste-skill`, `high-end-visual-design`, `frontend-design`, `antislop-ui`, `impeccable` |
| Movimiento | `gsap`, `60fps-animation`, `animate-ui`, `interaction-design`, `emil-design-eng`, `review-animations` |
| 3D / WebGL | `threejs`, `webgl-landing-steering` |
| Sistema visual | `better-colors`, `oklch-skill`, `better-typography`, `better-layout`, `tailwindcss`, `shadcn` |
| Revisión | `design-review`, `critique`, `audit`, `polish`, `better-interface`, `web-design-guidelines`, `refactoring-ui` |
| Accesibilidad y rendimiento | `better-accessibility`, `fixing-accessibility`, `core-web-vitals` |
| De imagen a código / clonar | `image-to-code`, `web-clone` |
| Frameworks | `next-best-practices`, `react-best-practices`, `vercel-react-best-practices` |
| Disciplina | `verification-before-completion`, `systematic-debugging`, `full-output-enforcement`, `unlazy` |

## Licencia de los diseños

Se pueden usar y modificar en proyectos propios y de clientes, incluso vendidos como producto terminado. No se pueden redistribuir como biblioteca, plantilla o recurso, ni publicar en otro repositorio. En GitHub solo van el catálogo y los scripts (el código de `recursos/` está en .gitignore); en la PC del usuario `recursos/` sí está instalado. Al entregar un proyecto, el código copiado con `usar.py` forma parte del producto terminado, lo cual la licencia permite. Las fotos de demostración son de Unsplash; reemplazarlas.
