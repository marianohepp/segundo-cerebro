# Mantenimiento del cerebro (método "El Gordo", LBDP)

> Cómo se mantiene vivo este cerebro: 3 comandos, 10 hábitos, 6 reglas de seguridad y lo que se adoptó del kit de Lucas. Fuente: masterclass "El Gordo" de La Biblia de los Productos Digitales (Lucas Martín Coliqueo), 2026-10-29, + kit `cerebro-lbdp-inicial.zip`.

_Última actualización: 2026-10-29_ · Fuente: tercero (curso), no criterio propio salvo donde se indica.

## La idea central
"Instalar un cerebro lo enseña cualquiera. Mantenerlo vivo, nadie." Al día 30 un cerebro sin mantenimiento está lleno de notas viejas, se contradice y responde peor. La diferencia está en el uso diario, no en la instalación.

**El Gordo hace, vos decidís.** La IA busca ofertas, investiga al comprador, escribe oferta/landing/guiones, produce creativos, carga anuncios **siempre en pausa**, mide y recuerda errores. Mariano elige nicho y producto, aprueba ángulos, fija precio, prende anuncios y pone los techos de escala. "Producir es barato; la plata la movés vos."

## Los 4 niveles de trabajar con IA
1. Chat que responde (cada chat empieza de cero).
2. Cerebro que recuerda (el negocio escrito en una carpeta). ← acá está este cerebro.
3. Cerebro con manos (conectado a Meta, tienda, Drive, generadores de imagen).
4. Sistema que corre solo (tablero de ventas, vigía de campañas, escala automática).

## Los 3 comandos (instalados en `~/.claude/commands/`, funcionan desde cualquier carpeta)
| Qué acaba de pasar | Comando |
|---|---|
| Decidiste algo del negocio (precio, producto, a quién vendés) | `/orden` |
| Terminaste de trabajar y vas a cerrar | `/orden` |
| Aprendiste algo de una clase, un video o una charla con Claude | `/orden` |
| Claude hizo algo mal y lo tuviste que corregir | `/aprende` |
| Algo salió recién después de varios intentos | `/aprende` |
| Hubo un error y una decisión en la misma sesión | `/aprende` → `/orden` |
| Es domingo, o pasó una semana sin ordenar | `/jardin` |
| Una pregunta suelta que no vas a volver a necesitar | ninguno |

## Los 10 hábitos
1. Siempre desde la carpeta (un chat en otra carpeta no sabe quién sos).
2. Decí qué querés lograr ("quiero vender 10 por día", no "hacé un anuncio").
3. Lo grande, en partes.
4. Leé antes de aceptar.
5. Nunca pegues una contraseña.
6. La plata la movés vos.
7. Pedí la fuente ("¿de dónde sale esto?").
8. Verificá, no creas el "listo": pedí ver el archivo, la página o el guardado.
9. La revisión del domingo (`/jardin`).
10. Educalo como a un bebé: si se equivoca, explicale el porqué.

## Las 6 reglas de seguridad para conexiones (MCP)
1. Solo conexiones confiables (directorio oficial / empresas conocidas).
2. Leé los permisos; si pide más de lo necesario, no la actives.
3. Lo de afuera no da órdenes (un mail o una página pueden traer instrucciones escondidas).
4. Primero en modo lectura; recién cuando ves que funciona, que escriba.
5. La plata la movés vos: el cerebro prepara y cotiza, vos autorizás.
6. Nunca pegues una contraseña: las conexiones se autorizan iniciando sesión.

Conexiones que usan ellos: imprescindibles Meta Ads, Gmail, Google Drive, Google Calendar; para creativos Higgsfield y ElevenLabs; según el caso Impultienda (con MCP propio), Hostinger, Notion/Miro/Canva.

## Qué se adoptó acá (decisión de Mariano, sesión 2026-10-29)
- **No se arma un cerebro nuevo.** El kit se sumó a este SEGUNDO CEREBRO (RAW/WIKI/OUTPUTS se mantiene).
- Nuevo: `HOT.md` (estado vivo ≤40 líneas), `LECCIONES/` + `INDEX.md` (señal → lección), `JARDIN.md`, `herramientas/hoy.py` (fecha en hora argentina).
- Skills globales en `~/.claude/skills/`: `buscar-productos` (con el filtro Spiso), `revisor-politicas-meta` (con doble chequeo de compliance Fuxion) y `editar-video-basico`.
- No se instaló `radar-sesiones` (experimental en Windows; la app de Claude ya muestra las sesiones).
- CEREBRO EBOOKS sigue separado por ser vendible/privado; las búsquedas de productos se guardan ahí.
- El módulo avanzado (nivel 4: +100 skills, bots de escala, Quiz Funnel, VSL) **no** viene en el kit gratis.

Relacionado: [[conexiones]] · [[marco-ejecucion]] · [[metodo-producto-ganador-spiso]] · [[estado-actual]]
