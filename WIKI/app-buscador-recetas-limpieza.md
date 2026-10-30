# App Buscador de Recetas — bonus del ebook

_Última actualización: 2026-08-21_

> Idea de Mariano: convertir el ebook de "PDF que se lee una vez" en una herramienta de uso recurrente. El usuario escribe qué mancha tiene o qué quiere limpiar (ej. "mancha de grasa en el baño") y la app le devuelve la receta exacta del recetario. Posicionamiento: doble dolor — **ahorro** (dejar de comprar productos de limpieza) y **natural vs. químico**.

## Qué es
- Archivo único `H:\ebooks seba spiso\app-buscador-recetas.html` — HTML+JS estático, sin backend, sin costo recurrente, sin dependencias externas.
- Las 100 recetas de [[2026-08-19-recetario-100-recetas-limpieza-completo|el recetario completo]] están embebidas en el archivo.
- Búsqueda por texto libre con expansión de sinónimos (ej. "baño" también matchea sarro/inodoro/ducha/bidet/mampara; "grasa" matchea desengrasante/aceite) + filtro por las 10 categorías + 6 chips de búsquedas rápidas.
- Diseño mobile-first (el uso real va a ser desde el celular, después de la compra).

## Decisión de alcance (2026-08-21)
Se evaluaron dos versiones:
1. **Búsqueda simple (elegida)** — estática, gratis, sin riesgo de quedar a medio terminar.
2. **Chat con IA** — API de Claude, lenguaje natural libre, pero necesita backend/hosting y tiene costo por uso.

Se arrancó con la versión 1 para tener el bonus listo ya. La versión IA queda como posible upgrade de fase 2 si el producto empieza a vender.

## Pendiente
- [ ] Sumar esta app como bonus explícito en la página de venta ([[2026-08-15-pagina-venta-recetas-limpieza-casera]]).
- [ ] Definir cómo se entrega tras la compra (link directo, o subida a Netlify una vez creada la tienda Shopify nueva).
- [ ] Decidir si upgradeamos a versión con IA más adelante.

## Relacionado
- [[metodo-producto-ganador-spiso]] · [[2026-08-15-pagina-venta-recetas-limpieza-casera]] · [[2026-08-19-recetario-100-recetas-limpieza-completo]]
