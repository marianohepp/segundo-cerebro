@echo off
REM Respaldo rapido del Segundo Cerebro a GitHub.
REM Hace add + commit (con fecha) + push. Requiere el remoto 'origin' ya configurado.
cd /d "%~dp0"
echo === Respaldando Segundo Cerebro a GitHub ===
git add -A
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do set HOY=%%a-%%b-%%c
git commit -m "backup: %HOY%"
git push
echo === Listo ===
pause
