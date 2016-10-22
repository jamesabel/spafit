echo off
if "%1"=="" goto blank
if "%2"=="" goto blank
goto docopy
:blank
echo on
echo "parameters not properly given"
goto done
:docopy
copy /Y %1\main.py %2
copy /Y %1\make_venv.bat %2
copy /Y %1\main.bat %2
:done