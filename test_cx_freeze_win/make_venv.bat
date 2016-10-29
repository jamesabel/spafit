REM c:\Users\james\AppData\Local\Programs\Python\Python35\python.exe c:\Users\james\AppData\Local\Programs\Python\Python35\Tools\scripts\pyvenv.py --clear venv
REM cx_freeze does not yet support Python 3.5
c:\python34\python.exe c:\Python34\Tools\Scripts\pyvenv.py --clear venv
venv\Scripts\pip3.exe install -U pip
venv\Scripts\pip3.exe install -U setuptools
venv\Scripts\pip3.exe install -U -r requirements.txt
