@echo off
chcp 65001 > nul
cd /d "%~dp0"
title YLuna85 LABs / IF Baiano — Launcher
echo ========================================================
echo   Iniciando Aplicacao Local: Concurso SEFAZ Dashboard
echo ========================================================
python "%~dp0app.py"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERRO] Ocorreu uma falha durante a execucao da aplicacao.
    pause
)
