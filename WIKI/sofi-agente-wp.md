# Sofi — agente IA de WhatsApp

> Agente conversacional "Sofi" que califica leads de Fuxion por WhatsApp automáticamente. Node.js + Twilio + API de Claude.

_Última actualización: 2026-07-23_

## Stack
- **Node.js + Express + Twilio + API de Claude.**
- Corre en la PC Windows de Mariano (`H:\AGENTE IA FUXION WP`) con **ngrok**.
- Usa **sandbox de Twilio**.

## Qué hace
- Dos flujos de calificación:
  1. **Compradores de producto.**
  2. **Prospectos de oportunidad de negocio.**
- También da **soporte post-compra de [[despertate-bien]]**.

## Objetivo
Automatizar la calificación de leads para que el único trabajo manual de Mariano sea **dar presentaciones 1-a-1 ya precalificadas**.

## Nota de arquitectura
Sofi (califica *antes*) y el bot "Iva" de [[proa-crm]] (gestiona *después*) son las dos mitades del mismo pipeline de WhatsApp con Claude → ver [[conexiones]] #2.

## Relacionado
- [[fuxion-proa]] · [[proa-crm]] · [[despertate-bien]] · [[conexiones]]
