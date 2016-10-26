
- use make_setup.sh to make the setup.py file, instead of trying
  to do it by hand initially
  - *** ISSUE ***: note that I couldn't run py2applet like it says in the tutorial:

jamesmacbookpro:py2app james$ py2applet --make-setup main.py
-bash: /usr/local/bin/py2applet: /usr/local/opt/python3/bin/python3.5: bad interpreter: No such file or directory
jamesmacbookpro:py2app james$ 

    so I had to run it like this:
    
venv/bin/python3 venv/lib//python3.5/site-packages/py2app/script_py2applet.py --make-setup main.py

- *** ISSUE ***: py2app doesn't work with venv, so I had to install (pollute) my regular python3 environment!!!

- *** ISSUE ***: I still get this error:

10/20/16 12:00:05.223 PM lsd[247]: LaunchServices: Could not store lsd-identifiers file at /private/var/db/lsd/com.apple.lsdschemes.plist
10/20/16 12:00:05.272 PM appleeventsd[52]: SecTaskLoadEntitlements failed error=22
10/20/16 12:00:05.275 PM launchservicesd[82]: SecTaskLoadEntitlements failed error=22
10/20/16 12:00:05.276 PM launchservicesd[82]: SecTaskLoadEntitlements failed error=22
10/20/16 12:00:07.402 PM main[5736]: main Error
10/20/16 12:00:07.402 PM main[5736]: 2016-10-20 12:00:07.402 main[5736:350507] main Error
10/20/16 12:00:08.744 PM sharedfilelistd[281]: SecTaskLoadEntitlements failed error=22
10/20/16 12:00:08.746 PM main[5736]: Traceback (most recent call last):
10/20/16 12:00:08.746 PM main[5736]:   File "/Users/james/projects/afit/py2app/dist/main.app/Contents/Resources/__boot__.py", line 351, in <module>
10/20/16 12:00:08.746 PM main[5736]:     _run()
10/20/16 12:00:08.746 PM main[5736]:   File "/Users/james/projects/afit/py2app/dist/main.app/Contents/Resources/__boot__.py", line 336, in _run
10/20/16 12:00:08.746 PM main[5736]:     exec(compile(source, path, 'exec'), globals(), globals())
10/20/16 12:00:08.746 PM main[5736]:   File "/Users/james/projects/afit/py2app/dist/main.app/Contents/Resources/main.py", line 2, in <module>
10/20/16 12:00:08.746 PM main[5736]:     import afit.afit
10/20/16 12:00:08.746 PM main[5736]:   File "afit/afit.pyc", line 3, in <module>
10/20/16 12:00:08.746 PM main[5736]:   File "PyQt5/QtWidgets.pyc", line 14, in <module>
10/20/16 12:00:08.746 PM main[5736]:   File "PyQt5/QtWidgets.pyc", line 10, in __load
10/20/16 12:00:08.746 PM main[5736]:   File "imp.pyc", line 342, in load_dynamic
10/20/16 12:00:08.746 PM main[5736]: ImportError: dlopen(/Users/james/projects/afit/py2app/dist/main.app/Contents/Resources/lib/python3.5/lib-dynload/PyQt5/QtWidgets.so, 2): Library not loaded: @rpath/QtWidgets.framework/Versions/5/QtWidgets
10/20/16 12:00:08.746 PM main[5736]:   Referenced from: /Users/james/projects/afit/py2app/dist/main.app/Contents/Resources/lib/python3.5/lib-dynload/PyQt5/QtWidgets.so
10/20/16 12:00:08.746 PM main[5736]:   Reason: image not found
