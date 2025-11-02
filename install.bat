@echo off
call venv\Scripts\activate
python run.py --execution-provider cuda
pause