# Despertate Bien — producto digital (foco prioritario)

> Ebook + app de bienestar sobre sueño/energía/salud intestinal. Infraestructura casi completa, pero ventas en cero: bloqueado por creativos de video con IA con texto alucinado.

_Última actualización: 2026-07-23_

## Producto
- Ebook **"Despertate con Energía"**: sueño, salud intestinal, energía, reducción de azúcar. Incluye técnica bonus **"Respiración Gamma"**.
- Upsells naturales integrados: **Prunex1, Floraliv, Vita XT** (afiliados → ligados a [[fuxion-proa]]).

## Venta e infraestructura
- **Shopify** (`despertatebien.com`) + **MercadoPago Checkout Pro**, en ARS.
  - Variant ID `52515306733890`, precio **~$7.999 ARS**.
- **Funnel** en Netlify + **Klaviyo** (flows: recuperación de paywall, onboarding post-compra, reactivación).
- **Meta Pixel** ID `26395877520024900` + Conversions API (pendiente integrar con Shopify/CAPI, postergado hasta resolver lo creativo).
- **App PWA** (`despertatebien.netlify.app`): mecánica tipo Netflix, desbloqueo diario, **paywall efecto Zeigarnik** (Día 1 gratis, Días 2–7 con token `DB2026` tras compra), persistencia en localStorage.
- Soporte post-compra vía [[sofi-agente-wp]].

## 🔴 Bloqueante actual
- Infraestructura prácticamente completa, pero **Meta Ads pausados y ventas en cero**.
- Causa: creativos de video con IA con **texto alucinado** (rastreado a **Higgsfield**).
- ⚠️ Mismo Higgsfield frena también a [[nueva-frecuencia]] y [[planeta-limpio-corsair]] → ver [[conexiones]] #1.

## Solución en curso
- **Generador de storyboards** (`generador-guiones.html`) que usa la API de Claude para crear guiones de video **sin texto** para Kling/Veo/Sora, con líneas de overlay en español para CapCut. Integrado con **aimlapi.com** (pago por uso).
- **Banco de contenido:**
  - **7 ángulos narrativos:** templos oníricos de Egipto, Carl Jung, ciencia de Matthew Walker, data de productividad, prácticas oníricas esotéricas, investigación REM/microbioma, testimonios UGC.
  - **3 patrones ganadores (mercado argentino):** confesión en primera persona; "¿Te imaginás?" con plazos específicos; contradicción-revelación.
  - Basado en análisis de **174 ads argentinos activos**.

## Foco actual (checklist semanal)
Terminar y **reactivar la campaña de Meta Ads**.

## Relacionado
- [[perfil-mariano]] · [[fuxion-proa]] · [[sofi-agente-wp]] · [[marco-ejecucion]]
