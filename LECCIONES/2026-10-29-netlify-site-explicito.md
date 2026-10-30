---
area: deploy-apps
creada: 2026-09-06
validada: 2026-10-29
recurrencias: 1
---
# Netlify: siempre --site explícito

- **Qué pasó (2026-09-06):** al deployar la app buscadora de recetas con `--dir` a otra carpeta, el CLI publicó sobre `proa-app-627` y pisó la app de PROA en producción.
- **Por qué:** `--dir` no elige el sitio destino; el CLI usa el link de la carpeta desde donde se corre (o su padre).
- **Cómo evitarlo:** `netlify deploy --dir <carpeta> --site <sitio> --prod --no-build`, y después verificar el sitio buscando un texto único del proyecto.
- **Señal:** estás por correr `netlify deploy` sin `--site` → detenete.
