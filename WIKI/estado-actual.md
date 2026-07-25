# Estado actual — dashboard

> El tablero único de qué está trabado, qué hay que decidir y qué vence. Reúne en un solo lugar lo que estaba regado por 6+ temas. **Actualizar en cada procesado de RAW.**

_Última actualización: 2026-07-23_

## ⏰ Fechas y deadlines
- **Miércoles próximo** — dar la **capacitación del [[evento-alumbra]]** (deck Canva, 10 slides, 30 min) para motivar al equipo a ir al evento anual de Fuxion en Perú.
- **28-ago-2026** — cierre del ciclo de 90 días. Meta doble: **rango Diamante** en [[fuxion-proa]] + **primeras ventas del ebook** ([[despertate-bien]]).

## 🔴 Bloqueantes activos (frenan resultado hoy)
- **✅ RESUELTO 25/07 — Tienda `despertatebien.com` volvió a funcionar.** Tras borrar el ALIAS a Netlify: apex resuelve a Shopify (23.227.38.65), Shopify emitió cert válido (`CN=despertatebien.com`, hasta oct-2026), HTTP 200. Ya no bloquea el lanzamiento. _(Detalle de la causa abajo, conservado como referencia.)_
- **~~🆕 25/07 — Tienda `despertatebien.com` caída~~ (resuelto, arriba). CAUSA RAÍZ que fue en la zona DNS (Hostinger):** el apex `@` tenía un **`ALIAS @ → sparkling-cascaron-a84ff7.netlify.app`** (un Netlify viejo, un creativo cinematográfico de captación que Mariano **ya no usa**) en conflicto con el `A @ → 23.227.38.65` (Shopify). El apex caía en ese Netlify sin cert → 403 + "conexión no privada" (los IPv6 `2600:1f18…` eran de Netlify/AWS). `www` sí tiene cert Shopify válido pero redirige al apex roto. **FIX (Opción A, decidida): borrar el `ALIAS @ → netlify`, dejar `A @ → 23.227.38.65`, agregar `AAAA @ → 2620:127:f00f:5::`.** Con eso el apex va a Shopify con SSL válido. Pendiente: que Mariano lo aplique y propague. NO usar "Restablecer registros DNS".
| Proyecto | Bloqueante | Estado / salida |
|---|---|---|
| [[despertate-bien]] | ~~Meta Ads pausados, ventas $0~~ | ✅✅ **25/07 CAMPAÑA LANZADA.** 3 creativos Veo 3 (C1 sueño, C2 energía, C3 café) corriendo en campaña de **Tráfico** ($3 USD/día, Argentina amplio, pixel conectado, destino despertatebien.com). El bloqueante de semanas quedó resuelto de punta a punta. **Próximo:** no tocar 48-72h; a los 2-3 días analizar cuál creativo gana (mejor CTR + menor costo) → escalar el ganador, pausar los otros. |
| [[nueva-frecuencia]] · [[planeta-limpio-corsair]] | Mismo problema Higgsfield ([[conexiones]] #1) | Se destraban con la misma solución del ebook |
| [[torque]] | **Pendiente sin resolver con Lucas** (estructura fiscal / CUIT) | Sin resolver — riesgo estructural |

## 🟡 Decisiones abiertas (esperan que decidas)
- **[[torque]]** — ¿cómo se resuelve lo de Lucas? (comisión / pendiente)
- **[[residencia-ancianos]]** — ¿comprás el terreno (lote 20×40m)? Sin decidir.
- **[[proa-crm]]** — ¿open-source + tier pago, o cerrado? ¿Se lanza contra Xenda?
- **Rango Fuxion** — ⚠️ contradicción a aclarar: ¿ya sos Diamante o vas hacia Diamante? (ver [[health check]])

## 📋 Pendientes por frente
- **[[fuxion-proa]]:** conversación directa con **Rosa y Adri** (foco declarado). Beta cerrada del CRM con ellas.
- **[[torque]]:** cerrar al **mecánico que se independiza** (cliente clave). Resolver lo de Lucas.
- **[[despertate-bien]]:** terminar generador de guiones → reactivar 1 campaña Meta con los 3 patrones AR.
- **Red (ver [[gente]]):** Juan Luis Reyna pidió ayuda con un tema fiscal personal (detalle en carpeta privada local `H:\CEREBRO-PRIVADO-LOCAL\`, fuera de la nube).

## 🟢 En pausa / despriorizado (no gastar energía ahora)
- [[planeta-limpio-corsair]] · ebook de supervivencia y negocio de madera ([[otros-proyectos]]).

## 📉 Falta medir (sin línea de base)
Metas sin baseline → hoy no son medibles. **Pendiente cargar:** facturación mensual de Torque, ventas/volumen Fuxion del mes, ingresos del ebook (se asume $0). Ver `OUTPUTS/health-check-2026-07-23.md`.

---
_Relacionado: [[index]] · [[perfil-mariano]] · [[conexiones]] · [[marco-ejecucion]]_
