# 🧠 Segundo Cerebro

Sistema personal de conocimiento de Mariano. Claude actúa como **bibliotecario**: lee lo crudo, lo organiza, responde con contexto real y guarda lo importante.

---

## Estructura

```
SEGUNDO CEREBRO/
├── README.md        ← este archivo (cómo funciona el sistema)
├── changelog.md     ← qué se procesó y cuándo
├── RAW/             ← ⬇️  ENTRADA. Aquí TÚ tiras todo en crudo
├── WIKI/            ← 📚  CONOCIMIENTO ORGANIZADO. Solo lo edita Claude
│   ├── index.md     ← mapa de todos los temas
│   └── <tema>.md    ← un archivo por tema, enlazados con [[nombre-tema]]
└── OUTPUTS/         ← 💾  Respuestas importantes guardadas con fecha
```

## Las 5 reglas del bibliotecario

1. **LEER** → Cuando digas "procesa RAW" (o un archivo), Claude lee `RAW/` y lo digiere.
2. **ORGANIZAR** → Claude crea/actualiza `WIKI/`. **Tú NUNCA editas WIKI a mano.**
3. **RESPONDER** → Antes de contestar, Claude busca en `WIKI/` y `RAW/`. Contexto real, no genérico.
4. **GUARDAR** → Respuestas importantes van a `OUTPUTS/` con fecha, enlazadas desde el índice.
5. **MEJORAR** → Claude detecta los 3 mayores huecos y sugiere qué añadir.

## Cómo lo usas (comandos en lenguaje natural)

| Dices… | Claude hace… |
|---|---|
| "Procesá RAW" | Lee todo lo nuevo en `RAW/`, actualiza `WIKI/` y `changelog.md` |
| "Procesá `RAW/archivo.md`" | Digiere solo ese archivo |
| "¿Qué sé sobre X?" | Busca en WIKI/RAW y responde con tu contexto real |
| "Guardá esto" | Escribe la respuesta en `OUTPUTS/YYYY-MM-DD-tema.md` |
| "¿Qué me falta?" | Lista los 3 mayores gaps de conocimiento |

## Flujo de trabajo

```
TÚ tiras notas → RAW/  →  "procesá RAW"  →  Claude organiza → WIKI/
                                                              ↓
        preguntás ← respuesta con contexto ← Claude busca en WIKI + RAW
                                                              ↓
                                    lo importante se archiva → OUTPUTS/
```

## Convenciones de la WIKI

- **Un archivo por tema.** Nombre en `kebab-case` (ej. `fuxion-productos.md`).
- **Enlaces internos** con `[[nombre-tema]]` (sin `.md`).
- Cada tema arranca con una línea de resumen y la fecha de última actualización.
- `index.md` es el mapa maestro: una línea por tema con su gancho.
