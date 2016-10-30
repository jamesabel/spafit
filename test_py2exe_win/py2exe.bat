rmdir /s /q dist
..\util\copy_files.bat .. .
REM we would like to use a venv but PyQt5 on Python 3.4 does not install to a venv
REM and we are on Python 3.4 since py2exe does not support Python 3.5
c:\python34\Scripts\pip3.exe install -U pip
c:\python34\Scripts\pip3.exe install -U setuptools
REM only have to do this the first time
downloads\PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x64.exe
c:\python34\Scripts\pip3.exe install -U -r requirements.txt
c:\python34\python.exe setup.py py2exe
dist\main.exe
move dist\main.log ..