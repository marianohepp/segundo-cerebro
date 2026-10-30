#!/usr/bin/env python3
"""hoy.py — la fecha de hoy en TU zona horaria, igual en Mac, Linux y Windows.

    python3 hoy.py                 2026-10-08
    python3 hoy.py --hora          2026-10-08 23:41
    python3 hoy.py --zona America/Mexico_City

(En Windows: `python hoy.py` o `py -3 hoy.py`.)

POR QUE EXISTE
  El comando de shell `TZ='America/Argentina/Buenos_Aires' date` en el Git Bash
  de Windows ignora la zona y devuelve la hora UTC: entre las 21:00 y la
  medianoche argentinas fecha las notas con el día SIGUIENTE, sin dar error.

LA ZONA
  1. --zona si se pasa;  2. la variable CEREBRO_ZONA;  3. Buenos Aires.
  Windows no trae la base de zonas horarias: si falta (y no está el paquete
  `tzdata`), para Argentina se usa UTC-3 fijo —Argentina no tiene horario de
  verano— y para otra zona se pide `pip install tzdata` en vez de adivinar.
"""
import argparse
import os
import sys
from datetime import datetime, timedelta, timezone

# Windows: con la salida redirigida (así la lee Claude Code) Python escribe en
# cp1252: revienta al imprimir ✓ o →, y lee mal (o se cae) con el texto en UTF-8.
for _flujo in (sys.stdin, sys.stdout, sys.stderr):
    try:
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


POR_DEFECTO = "America/Argentina/Buenos_Aires"
# Zonas sin horario de verano: su desfasaje fijo es exacto todo el año.
FIJAS = {
    "America/Argentina/Buenos_Aires": -3,
    "America/Buenos_Aires": -3,
    "America/Montevideo": -3,
    "America/Bogota": -5,
    "America/Lima": -5,
    "America/Mexico_City": -6,
}


def zona_horaria(nombre):
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(nombre)
    except Exception:
        if nombre in FIJAS:
            return timezone(timedelta(hours=FIJAS[nombre]))
        sys.exit(f"[error] esta máquina no conoce la zona «{nombre}». "
                 f"Instalá la base de zonas:  python -m pip install tzdata")


def main():
    ap = argparse.ArgumentParser(description="Fecha de hoy en una zona horaria fija.")
    ap.add_argument("--zona", default=os.environ.get("CEREBRO_ZONA") or POR_DEFECTO)
    ap.add_argument("--hora", action="store_true", help="agrega la hora (HH:MM)")
    a = ap.parse_args()
    ahora = datetime.now(zona_horaria(a.zona))
    print(ahora.strftime("%Y-%m-%d %H:%M" if a.hora else "%Y-%m-%d"))


if __name__ == "__main__":
    main()
