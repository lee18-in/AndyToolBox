@echo off
setlocal enabledelayedexpansion

REM === Step 1: Create Python virtual environment ===
echo [1/5] Creating Python virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo ❌ Failed to create venv. Make sure Python is installed and added to PATH.
    pause
    exit /b
)

REM === Step 2: Ensure requirements.txt exists, then install dependencies ===
echo [2/5] Installing dependencies from requirements.txt...

if not exist requirements.txt (
    echo ⚠️ requirements.txt not found. Creating an empty one...
    echo. > requirements.txt
)

powershell -NoProfile -ExecutionPolicy RemoteSigned -Command ^
    "& { .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt }"

REM === Step 3: Create .vscode/settings.json for VSCode interpreter path ===
echo [3/5] Creating VSCode settings...
mkdir .vscode >nul 2>&1

(
    echo {
    echo     "python.defaultInterpreterPath": "^${workspaceFolder}/.venv/Scripts/python.exe^",
    echo     "python.terminal.activateEnvironment": true,
    echo     "terminal.integrated.cwd": "^${workspaceFolder}^",
    echo     "//": "Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned; .\\.venv\\Scripts\\Activate.ps1"
    echo }
) > .vscode\settings.json



REM === Step 4: Create README.md with setup instructions ===
echo [4/5] Creating README.md...
(
    echo # ### Development Environment Setup ###
    echo # python -m venv venv
    echo # Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned; .\\.venv\\Scripts\\Activate.ps1
    echo # pip install -r requirements.txt
) > README.md


REM === Step 5: Done ===



echo [5/5] Setup completed successfully!
pause
