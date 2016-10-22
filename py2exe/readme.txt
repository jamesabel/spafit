
- py2exe does not support 3.5 (through 3.4 only)

- PyQt5 doesn't install with PIP, so you have to install it from something like "PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x64.exe".
  And this doesn't install into a venv, so we have to pollute our base Python installation.

- even with all of that, we still get:

Traceback (most recent call last):
  File "main.py", line 4, in <module>
  File "c:\python34\lib\site-packages\zipextimporter.py", line 109, in load_module
    self.get_data)
ImportError: No module named 'sip'

This is copied to main.log BTW.

