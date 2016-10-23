rmdir /s /q build
call ..\util\copy_files.bat .. .
c:\Users\james\AppData\Local\Programs\Python\Python35\python.exe c:\Users\james\AppData\Local\Programs\Python\Python35\Tools\scripts\pyvenv.py --clear venv
venv\Scripts\pip3.exe install -U pip
venv\Scripts\pip3.exe install -U setuptools
venv\Scripts\pip3.exe install -U -r requirements.txt
venv\Scripts\python.exe -m nsist installer.cfg
build\nsis\pynsist_1.0.exe
