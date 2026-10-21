@echo off
title ForgeGuard System Prototype Launcher
echo ========================================================
echo  ForgeGuard: Digital Transaction Receipt Forgery Detection
echo  NDMC BSCS Thesis 2026 - Ungab ^& Bacanto
echo ========================================================
echo.

cd /d "%~dp0"

if exist "%~dp0venv\Scripts\python.exe" (
    set "PY_CMD=%~dp0venv\Scripts\python.exe"
    goto :found_python
)
if exist "%~dp0..\venv\Scripts\python.exe" (
    set "PY_CMD=%~dp0..\venv\Scripts\python.exe"
    goto :found_python
)
if exist "%~dp0..\.venv312\Scripts\python.exe" (
    set "PY_CMD=%~dp0..\.venv312\Scripts\python.exe"
    goto :found_python
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PY_CMD=python"
    goto :found_python
)

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PY_CMD=py"
    goto :found_python
)

echo [ERROR] Python was not found in your system PATH.
echo Please install Python 3.10 - 3.12 and ensure it is added to PATH.
pause
exit /b 1

:found_python
echo [1/2] Verifying Python dependencies from 02_Project_Files...
if exist "02_Project_Files\requirements.txt" (
    %PY_CMD% -m pip install -q -r "02_Project_Files\requirements.txt"
) else if exist "requirements.txt" (
    %PY_CMD% -m pip install -q -r "requirements.txt"
)

echo [2/2] Launching ForgeGuard webapp from 01_Source_Code...
cd /d "%~dp001_Source_Code"
%PY_CMD% -m streamlit run app.py --server.headless false --browser.gatherUsageStats false

pause
