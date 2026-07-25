# 📋 Changelog del Segundo Cerebro

Registro de qué se procesó y cuándo. Lo mantiene Claude.

---

## 2026-07-25 — Procesado: mentoría PROA con Dalmir
- **Fuente:** `RAW/GMT20260725-140710_Recording.cc.vtt` (mentoría por calificación, líder Dalmir desde Colombia).
- **`metodologia-proa.md`** ampliado con los frameworks de Dalmir: "actúa por lo que sabes, no por cómo te sientes"; acompañar en el bajón pidiendo permiso; "la office habla"; calificación = periodo + afiliación; autoempleado → dueño de negocio; vender sueños (no "ingreso extra"); **herramienta #1 "Imaginate"** (de Margarita Patiño); predicar con el ejemplo.
- **`gente.md`** + Dalmir, Willy y Belinda (Guatemala), Angie Gluxman, Macky Fernández, Margarita Patiño.

## 2026-07-25 — 🚀🎉 CAMPAÑA LANZADA (primer test de Despertate Bien en el aire)
- **PUBLICADA** la campaña "Despertate - Trafico Test - Jul25" (cuenta ...55252). 3 anuncios: C1 sueño, C2 energía, C3 café — cada uno con su video Veo 3 + su copy propio + URL `https://despertatebien.com/`. Tráfico, $3 USD/día, Argentina amplio, pixel 26395877520024900 conectado.
- Revisión final OK: los 3 con video y copy correctos, "un solo video" por anuncio (se limpió la imagen de IA que había colado la duplicación).
- **Hito:** el bloqueante de creativos que frenaba las ventas hace semanas se resolvió de punta a punta EN UN DÍA: generar creativos (Veo 3) → montar (CapCut Pro) → destrabar la tienda (DNS/SSL) → armar y lanzar la campaña.
- **Seguimiento:** no tocar 48-72h. A los 2-3 días (≈27-28/07) analizar CTR + costo por clic por creativo → escalar ganador, pausar perdedores.

## 2026-07-25 — Campaña Tráfico: 3 anuncios armados (C1 + 2 copias), falta subir c2/c3
- Mariano corrigió la URL de destino del C1 a `https://despertatebien.com/`.
- Claude duplicó el C1 x2 (Duplicar rápidamente, 2 copias) → 3 anuncios en el conjunto. Renombró la 1ra copia a **C2 - Energia**.
- Pendiente (lo hace Mariano, porque los videos >10MB no los sube Claude): en C2 y C3 → Editar contenido multimedia → subir `c2-energia-final-v1.mp4` / `c3-cafe-final-v1.mp4` + cambiar texto/título (copys en `OUTPUTS/2026-07-24-guia-campana-meta-despertate.md`). Renombrar la 2da copia a **C3 - Cafe**. Luego **Publicar** (Mariano) y no tocar 48-72h.
- Todo lo demás (pixel, público AR, $3/día, CTA "Ver más", URL) ya viene heredado del C1.

## 2026-07-25 — Campaña recreada limpia (Tráfico) tras lío de Advantage+
- La campaña Advantage+ Ventas original se enroscó: Meta le pegó un "mensaje de marketing" de WhatsApp automático ("Publicar anuncio y mensaje"). Se decidió **recrear como campaña manual de Tráfico** (limpia, sin Advantage+, sin mensajes).
- **Nueva campaña "Despertate - Trafico Test - Jul25"** (cuenta ...55252): manual de Tráfico, $3 USD/día, público Argentina amplio, destino Sitio web. Anuncio **C1** con video reusado de la biblioteca (`c1 916.mp4`), texto+título+CTA "Ver más", **pixel conectado** (ID 26395877520024900) → calienta aunque sea tráfico.
- ⚠️ **Pendiente:** el campo de URL de destino quedó con la URL del **funnel** (`funnel.despertatebien.com`) y es un campo controlado que revierte por automatización → Mariano debe cambiarlo a `https://despertatebien.com/` a mano. Falta también crear **C2 y C3** (duplicar C1 + cambiar video/copy). Después: revisar y publicar (lo hace Mariano).
- El link de destino confirmado por Mariano: la **home de la tienda** `https://despertatebien.com/`.
- Los borradores viejos (campaña Advantage+ enroscada) quedan sin publicar; se pueden borrar.

## 2026-07-25 — Campaña Meta armada (borrador) vía navegador
- Campaña creada en la cuenta correcta **"despertate super bien" (...55252)** — Claude la armó operando Ads Manager con la extensión Chrome (Opción B: Claude configura, Mariano publica).
- Config: objetivo **Ventas**, **US$ 3/día** (CBO; la cuenta está en USD, no pesos — ojo con esto), puja Volumen más alto. Conjunto: Argentina amplio, pixel `despertatebien.com`, evento **Ver contenido** (pixel frío → se calienta primero, después se pasa a Compra).
- 3 errores frenados a tiempo: cuenta equivocada (...881036), moneda USD vs pesos, y **C1 exportado apaisado 1920x1080** (los otros 2 OK 1080x1920).
- Videos finales en `H:\CREATIVOS DESPERTATE\2-finales-meta`: c2-energia-final-v1, c3-cafe-final-v1 (OK). **Falta re-exportar C1 vertical.**
- Pendiente: C1 vertical → subir 3 videos + copy a los 3 anuncios → Mariano revisa y publica. Copy en `OUTPUTS/2026-07-24-guia-campana-meta-despertate.md`.

## 2026-07-24 — 🎉 HITO: 3 creativos de video generados (bloqueante destrabado)
- Los **3 creativos de Despertate Bien generados en Veo 3** (Google Flow): c1 sueño (cama→reloj→café), c2 energía (agua→comida→amanecer), c3 café (café→escritorio→estiramiento). Todos 10s, 9:16, **sin texto alucinado y sin caras** — resuelto el problema de Higgsfield que frenaba las ventas hace semanas.
- Guardados en `H:\CREATIVOS DESPERTATE\1-crudos-veo\`. Prompts pulidos (v2) en el plan de lanzamiento.
- Falta: montar overlays en CapCut → armar campaña de test en Meta → lanzar.
- Nota de tooling: instalado `imageio`/`imageio-ffmpeg` para revisar los videos frame por frame.

## 2026-07-24 — Research creativos IA + norte de $100k + parking-lot
- **Research procesado** (`recursos-creativos-ia.md`, tema 22): shortlist para el cuello de botella de creativos → video on-target de Leonardo Arias (`30ILN6S13LQ`, Veo 3, sin cara), imágenes con Nano Banana + Cosmos AI, y apps de pago (100 Ads de Claudio Conde, AI Builders). Recomendación: probar lo gratis antes de comprar.
- **Objetivo macro grabado** en `perfil-mariano.md`: **USD 100.000/mes residuales + ayudar a otros**.
- **Nuevo `parking-lot.md`** (tema 23): estacionamiento de ideas no-activas. Primera entrada: "copiar apps de creativos para venderlas" → estacionada para no desenfocar (decisión de Mariano).

## 2026-07-24 — Procesado: video método Cosmos AI (infoproductos)
- **Fuente:** YouTube de Leonardo Arias, "eBook con IA en 24h + Hotmart". Método capturado desde descripción+capítulos (vía navegador).
- **Nuevo tema `workflow-cosmos.md`** (tema 21): qué es Cosmos AI (agentes que orquestan Claude), el método de 5 pasos, y **lectura estratégica**: a Mariano le sirve la validación de nicho y el copy, NO crear ebook de cero en Hotmart (ya tiene Despertate Bien en Shopify). El video NO cubre su cuello de botella real (creativos de video) → traer el video "anuncios con IA" del mismo autor.
- ✅ Cuarto tipo de fuente al circuito (video de YouTube) procesado.

## 2026-07-24 — Aclaración de estrategia + reencuadre del deck Alumbra
- **Resuelto el ⚠️ Torque/dependencia:** Mariano aclaró que Torque es **alternativa de ingresos rápidos** (conocimiento + contactos proveedores), NO el foco. Foco = ebooks ([[despertate-bien]]) + [[fuxion-proa]] cuanto antes. Actualizados `perfil-mariano.md` y `torque.md`.
- **Deck Alumbra mejorado** con un reencuadre potente de la sesión del 04/06: "la energía de un evento dura poco; lo distinto es lo que te resuena y te ancla tu porqué". Añadido a `OUTPUTS/2026-07-24-deck-capacitacion-alumbra.md` y a `evento-alumbra.md`.
- ⚠️ Nota de atribución: la voz de ese pasaje (04/06) podría ser una co-líder, no Mariano (transcripción sin etiquetas de hablante). Marcado como tal.

## 2026-07-24 — Procesado: 10 transcripciones Zoom → análisis de patrones
- **Fuente:** 10 `.vtt` de mentorías/capacitaciones PROA (ene–jul 2026). Audios `.m4a` originales quedaron en Drive (gitignored).
- **Nuevo OUTPUT `patron-capacitaciones-proa-2026-07-24.md`:** análisis transversal — 4 tipos de espacio (mentorías por calificación / capas de salud / negocio-evento / técnica), 7 patrones recurrentes, frases-marca, molde de las capas de salud, objeciones típicas.
- **`metodologia-proa.md`** ampliado con los 4 tipos de espacio + frases-marca de la cultura.
- **Enriquecido el perfil desde la capacitación de Mariano del 04/06:** hija **Martina** (~12), dejó la relación de dependencia (~abril 2026) para full Fuxion (⚠️ a conciliar con [[torque]]), ganó Leadership Academy + viaje a Curazao, bebida favorita Vita.
- **Hallazgo:** una de las grabaciones (04/06) es la propia capacitación de Mariano sobre Alumbra → material directo para el deck.
- ✅ Primer análisis de patrones sobre un corpus grande. Circuito escala a lotes.

## 2026-07-24 — Procesado: transcripción Zoom de coaching PROA
- **Fuente:** `RAW/GMT20260723-160739_Recording.cc.vtt` (transcripción Zoom de un espacio de coaching PROA, inicio de periodo). Se deja el `.vtt` intacto como fuente original.
- **Nuevo tema `metodologia-proa.md`** (tema 20): cómo se lidera/acompaña en PROA — trabajo por periodos, sacar la carga emocional de la meta→plan, medir la acción (no el resultado) con herramienta, pedir permiso, plan de 90 días (PRO 1K / presentaciones / duplicación), el error de no soltar ("odio la palabra potencial"), volver al sistema, respetar lo que quiere el socio.
- **`gente.md`:** sumados referentes del sistema PROA (Luca Meloni, Vale, Buva, Lucas) e integrantes del coaching (Silvi, Marce, Jime).
- **Conexión fuerte detectada:** la "herramienta de medición diaria" que enseñan en PROA es justo lo que automatiza [[proa-crm]] → valida el diferencial del CRM. Y la metodología calza con [[marco-ejecucion]] (acción>intención). Anotado en el tema.
- ✅ Segundo tipo de fuente al circuito (Zoom .vtt) procesado con éxito.

## 2026-07-23 — Corrección de nombre: Umbra → Alumbra
- Mariano confirmó que el evento se llama **Alumbra** (el "Umbra" original venía de una transcripción de audio errada).
- Renombrados: `WIKI/evento-umbra.md` → `evento-alumbra.md` y `RAW/…-umbra.md` → `…-alumbra.md`.
- Actualizados todos los enlaces `[[evento-umbra]]` → `[[evento-alumbra]]` (index, fuxion-proa, estado-actual) y eliminada la nota de "nombre a confirmar". Contradicción resuelta.

## 2026-07-23 — Procesado: capacitación evento Alumbra (prueba del circuito completo)
- **Fuente:** conversación compartida de Claude, traída vía navegador (RAW `…-capacitacion-alumbra.md`).
- **Nuevo tema `evento-alumbra.md`** (tema 18): evento anual de Fuxion en Perú (20 años, estadio 20.000, 37 países) + la capacitación que Mariano da el miércoles (deck Canva, 10 slides, 3 ejes: analogía pizzero / asistir cambia mindset / mentalidad-entorno).
- Actualizados `fuxion-proa.md` (link al evento), `index.md`, `estado-actual.md` (deadline del miércoles).
- ✅ Primer procesado de una nota capturada desde el celular: circuito RAW → WIKI validado.

## 2026-07-23 — Dashboard + sincronización multi-dispositivo
- **Nuevo tema `estado-actual.md`** (dashboard único de bloqueantes/decisiones/fechas), enlazado desde `index.md`.
- **Privacidad:** datos sensibles de terceros (tema fiscal de un downline) movidos a `H:\CEREBRO-PRIVADO-LOCAL\` — carpeta **fuera** de SEGUNDO CEREBRO, invisible para Drive y GitHub. Redactadas todas las menciones en archivos que se suben.
- **Repo git local inicializado** + `.gitignore`. Commit inicial `e26ab4d` (sin datos sensibles en el árbol).
- **Setup híbrido de sync** documentado en `SINCRONIZACION.md`: Google Drive (captura desde el celular) + GitHub privado (backup versionado). Helper `backup-github.bat`.
- Pendiente del usuario: (1) reflejar la carpeta en Drive, (2) crear el repo privado en GitHub y pasarme la URL para conectar y hacer el primer push.

## 2026-07-23 — Fase 3 (el loop): síntesis, patrones, auto-mejora, health check
- **OUTPUTS creados (3):**
  - `2026-07-23-mejores-apuestas.md` — las 3 mejores apuestas (Despertate Bien / Fuxion+CRM / Torque) con ventajas, limitaciones y mejor caso.
  - `patron-trabajo-2026-07-23.md` — análisis de patrones: invierte más en construir que en terminar; cuello de botella = cerrar/vender; 3 temas a investigar.
  - `health-check-2026-07-23.md` — contradicciones, afirmaciones sin fuente, temas sin página, 3 artículos gap prioritarios.
- **Los 3 OUTPUTS enlazados desde `index.md`.**
- **Auto-mejora:** creado `CLAUDE.md` (no existía) con las 5 reglas intactas + nueva sección **"Contexto personal"** con patrones detectados. Instrucciones ampliadas, no borradas.
- **Nota de salud del wiki:** 🟢 buena; debilidades de frescura (datos que envejecen) y de medición (faltan baselines). Gap top: crear `estado-actual.md`.

## 2026-07-23 — Relectura de RAW + análisis transversal
- **Relectura completa de `RAW/`:** sin material nuevo. El único contenido sigue siendo `2026-07-23-perfil-completo-mariano.md`, ya volcado. La wiki de 15 temas ya lo reflejaba íntegro → no se reconstruyó (habría sido idéntico).
- **Nuevo tema `conexiones.md`** (tema 16): patrones que cruzan proyectos y no se ven tema por tema. Enlazado desde `index.md`.
- Cross-links reales agregados en `despertate-bien.md` (Higgsfield) y `sofi-agente-wp.md` (Iva/Sofi).

### 🔗 Conexiones inesperadas encontradas
1. **Cuello de botella de video-IA sistémico:** Higgsfield frena a la vez a `despertate-bien`, `nueva-frecuencia` y `planeta-limpio-corsair`. El `generador-guiones.html` destraba los tres.
2. **"Iva" (CRM) y "Sofi" (WhatsApp) son un solo pipeline partido en dos:** califican y gestionan el mismo funnel Fuxion; hoy viven separados.
3. **El ebook es el lead magnet de front-end de Fuxion:** sus upsells (Prunex1, Floraliv, Vita XT) *son* productos Fuxion; una sola audiencia corrida como 4 marcas.
4. **Fricción fiscal argentina recurrente:** aparece en Torque (CUIT de Lucas), en la red (tema fiscal de un integrante) y en la propia gestión. Mismo dolor, negocios distintos.
5. **"Fábrica de calculadoras HTML/PWA" no nombrada:** 6+ proyectos armaron calculadoras interactivas por separado → es una capacidad repetible, no N one-offs.
6. **El marco de ejecución ya trae el antídoto al sprawl:** la identidad "terminar lo que decido" choca con ~11 frentes; la pregunta filtro + "Sueños/Libertad" son la tijera para podar.

## 2026-07-23 — Primer procesado de RAW
- **Fuente:** `RAW/2026-07-23-perfil-completo-mariano.md` (perfil consolidado, 2 exports fusionados).
- **Acción:** digerido a WIKI. Creados **15 temas** enlazados entre sí:
  - Núcleo: `perfil-mariano`, `marco-ejecucion`, `gente`.
  - Negocios físicos: `torque`, `truck-parts`, `residencia-ancianos`.
  - Fuxion: `fuxion-proa`, `proa-crm`, `sofi-agente-wp`.
  - Digitales: `despertate-bien`, `nueva-frecuencia`, `planeta-limpio-corsair`, `otros-proyectos`.
  - Personal: `finanzas-personales`, `salud-longevidad`.
- `index.md` reescrito con los 15 temas agrupados por categoría.
- RAW original conservado como fuente.

## 2026-07-23 — Inicialización
- Sistema creado: estructura `RAW/` · `WIKI/` · `OUTPUTS/`.
- Archivos base: `README.md`, `WIKI/index.md`, `changelog.md`.
- Estado: sin material procesado todavía. Esperando primeros volcados en `RAW/`.
