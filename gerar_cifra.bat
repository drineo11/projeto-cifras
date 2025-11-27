@echo off
chcp 65001 > nul
echo.
echo === Gerador de PDF do Cifra Club ===
echo.

:: Check if a file was dragged onto the script icon
if not "%~1"=="" (
    set "input=%~1"
    goto :run
)

:ask
set /p "input=Cole a URL ou arraste o arquivo aqui: "

:: Remove surrounding quotes if present (in case of drag-and-drop into terminal)
set "input=%input:"=%"

:run
echo.
echo Processando: "%input%"
python cifra_formatter.py "%input%"
echo.
pause
