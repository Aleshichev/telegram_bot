@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot


set TOKEN=5558415436:AAGPfA9STLgPOGX-uJ6RDOIkUHgzf3Qzt74

python test\inline_buttons.py

pause
