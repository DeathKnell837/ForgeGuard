@echo off
title ForgeGuard System Prototype Launcher
echo ========================================================
echo  ForgeGuard: Digital Transaction Receipt Forgery Detection
echo  NDMC BSCS Thesis 2026 - Ungab ^& Bacanto
echo ========================================================
echo.

cd /d "%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python was not found in your system PATH.
    echo Please install Python 3.10 - 3.12 and ensure it is added to PATH.
    pause
    exit /b 1
)

echo [1/2] Verifying Python dependencies...
python -m pip install -q -r requirements.txt

echo [2/2] Launching ForgeGuard webapp...
python -m streamlit run src/app.py --server.headless false

pause
