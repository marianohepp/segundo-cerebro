---
area: deploy-apps
creada: 2026-07-21
validada: 2026-10-29
recurrencias: 2
---
# PROA: deployar la carpeta completa

- **Qué pasó:** regla pedida por Mariano el 2026-07-21. El 2026-09-06 un deploy sin `--functions=netlify/functions` dejó el bot en 404 durante 11 días aunque la página cargaba.
- **Por qué:** un deploy parcial deja el sitio inconsistente; sin netlify.toml, las funciones no suben solas.
- **Cómo evitarlo:** `netlify deploy --prod --site=<id PROA> --dir=. --functions=netlify/functions` desde la carpeta vigente, y probar el POST a `/.netlify/functions/chat`, no solo la home.
- **Señal:** estás por deployar PROA → carpeta entera + funciones + prueba del chat.
