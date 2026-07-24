# 🔄 Sincronización y captura desde cualquier dispositivo

Cómo llegan tus conversaciones al cerebro desde el celular o cualquier equipo, y cómo se respalda todo.

## Arquitectura (híbrida)

```
        CAPTURA rápida                 RESPALDO versionado
        (Google Drive)                    (GitHub privado)
             │                                  │
   📱 Celular / tablet / otra PC          💻 Tu PC principal
     tirás la conversación en    ┌──►  "procesá RAW" → WIKI/
        SEGUNDO CEREBRO/RAW/      │     git push → backup con historial
             │                    │
             └── se sincroniza ───┘
```

- **Google Drive** = capa de **captura**. La carpeta se refleja en la nube; desde el celular tirás notas en `RAW/` sin comandos.
- **GitHub (privado)** = capa de **respaldo**. Historial de cambios (diffs) de todo el cerebro. Se actualiza desde la PC.

---

## 📥 Cómo capturar una conversación (desde cualquier dispositivo)

1. **Guardá el texto** de la conversación (Claude, ChatGPT, WhatsApp, lo que sea) como archivo `.md` o `.txt`.
2. **Ponelo en `RAW/`** con este nombre:
   ```
   AAAA-MM-DD-fuente-tema.md
   ```
   Ejemplos: `2026-07-24-claude-ideas-ads-despertate.md` · `2026-07-25-whatsapp-charla-rosa.md`
3. En tu PC, cuando quieras, decime **"procesá RAW"** → lo digiero en la wiki.

### Desde el celular
- Abrí la **app de Google Drive** → carpeta `SEGUNDO CEREBRO/RAW` → **＋ / Subir** (o "Crear archivo de texto").
- O usá **Compartir** desde la app de chat → Google Drive → carpeta RAW.

### Desde otra PC
- Si tiene Drive para escritorio, la carpeta aparece sola: guardás el archivo en `RAW/` y listo.

---

## 🗂️ Setup de Google Drive (una sola vez, en tu PC)

Drive para escritorio ya está instalado. Falta **reflejar** esta carpeta:

1. Abrí **Google Drive** (ícono en la barra de tareas). Iniciá sesión si hace falta.
2. Engranaje ⚙️ → **Preferencias** → **Google Drive** (o "Carpetas de tu computadora" → **Agregar carpeta**).
3. Elegí `H:\SEGUNDO CEREBRO` y opción **"Reflejar" (Mirror)**.
4. Listo: la carpeta queda en `H:\` **y** en la nube, visible desde cualquier dispositivo.

> "Reflejar" mantiene la carpeta donde está (`H:\`) y la copia a la nube. "Transmitir/Stream" la movería a la unidad virtual — no lo uses, romperías las rutas locales.

---

## 💾 Respaldo a GitHub (desde la PC)

Una vez conectado el repo remoto (ver más abajo), respaldás con:

```bash
cd "H:/SEGUNDO CEREBRO"
git add -A
git commit -m "backup: <qué cambió>"
git push
```

O corré el helper: **`backup-github.bat`** (hace add + commit con fecha + push de una).

---

## 🔒 Qué NO se sincroniza
- Toda la carpeta **`_PRIVADO-LOCAL/`** — datos sensibles de terceros. Vive solo en esta PC (está en `.gitignore` y **no** la subas a Drive: si reflejás toda la carpeta, excluí esa subcarpeta o guardala fuera).

> ⚠️ **Importante con Drive:** el reflejo de Drive **no respeta `.gitignore`**. Si reflejás toda `SEGUNDO CEREBRO`, `_PRIVADO-LOCAL/` también subiría a Drive. Para evitarlo: o guardás `_PRIVADO-LOCAL/` en otra carpeta fuera del reflejo, o reflejás solo las subcarpetas `RAW/`, `WIKI/`, `OUTPUTS/`. Decime y lo dejo armado como prefieras.
