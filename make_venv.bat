if "%1"=="3.4" goto do34
c:\Users\james\AppData\Local\Programs\Python\Python35\python.exe c:\Users\james\AppData\Local\Programs\Python\Python35\Tools\scripts\pyvenv.py --clear venv
goto pip
:do34
REM use system site packages for PyQt5
c:\Python34\python.exe c:\Python34\Tools\Scripts\pyvenv.py --system-site-packages --clear venv
REM get pip
c:\Python34\python.exe c:\Python34\Tools\Scripts\pyvenv.py venv
:pip
venv\Scripts\pip3.exe install -U pip
venv\Scripts\pip3.exe install -U setuptools
venv\Scripts\pip3.exe install -U -r requirements.txt
