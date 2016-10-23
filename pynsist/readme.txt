
- GOOD NEWS: Running from Start menu and clicking the program ACTUALLY RUNS CORRECTLY!!!!

  A little bit of bad news: what its actually running is:

  C:\Windows\pyw.exe "C:\Program Files\pynsist\pynsist.launch.pyw"

  So, you can't necessarily just double-click on the .pyw (on my maching it brings .pyw up in IDLE).

  But for normal users this is probably OK.  We do need to get this to be what is executed on
  restart for program that are supposed to run on restart, but that shouldn't be a problem.

  I don't know exactly when this would have been fixed, but 1.8 was uploaded 2016-09-29.
  And 1.7 was 2016-05-19 and 1.6 was 2015-09-14. (see https://pypi.python.org/pypi/pynsist/json for all the times).
  My last test was at PyCon 2016 which would have been 1.6 or 1.7.  Now, I should have been on 1.7 which
  seems to work.  OR perhaps PyQt5 was fixed????

  From what I can tell, pynsist 1.6 didn't work (I tried pynsist=1.6 and got this):
Traceback (most recent call last):
  File "c:\Users\james\AppData\Local\Programs\Python\Python35\lib\runpy.py", line 184, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\Users\james\AppData\Local\Programs\Python\Python35\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\__main__.py", line 2, in <module>
    main()
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\__init__.py", line 490, in main
    ).run(makensis=(not options.no_makensis))
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\__init__.py", line 431, in run
    self.prepare_packages()
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\__init__.py", line 329, in prepare_packages
    py_version=self.py_version, exclude=self.exclude)
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\copymodules.py", line 224, in copy_modules
    mc.copy(modname, target, exclude)
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\copymodules.py", line 127, in copy
    check_package_for_ext_mods(pkgdir, self.py_version)
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\copymodules.py", line 41, in check_package_for_ext_mods
    check_ext_mod(os.path.join(path, dirpath, filename), target_python)
  File "c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\nsist\copymodules.py", line 34, in check_ext_mod
    raise ExtensionModuleMismatch(extensionmod_errmsg % ('Python '+target_python, path))
nsist.copymodules.ExtensionModuleMismatch: Found an extension module that will not be usable on Python 3.4.3:
c:\Users\james\projects\spafit\pynsist\venv\lib\site-packages\cryptography\hazmat\bindings\_constant_time.pyd
Put Windows packages in pynsist_pkgs/ to avoid this.

  However, 1.7 seems to work.  So, this was pretty terrible timing.  Also the prior version of PyQt5 (5.6) works.
  i.e., this:
    PyQt5==5.6
    cryptography
    pynsist==1.7

  So, it seems like I was either on an old Python (3.4) or pynsist 1.6. from before 2016-05-19.

  This is a huge bummer.  I've been telling everyone it didn't work, but it did with the latest versions ... even
  one version back for pynsist and PyQt5.

  One guess is that I had installed pynsist before going to PyCon - e.g. just before 2016-05-19 and didn't
  do an -U to my venv when I tried it, since I know I tried pynsist just before PyCon.

  But wait ... I think I tried it before PyBay .. look at the times in C:\Users\james\projects\experiments\pynsist_test,
  they are from 8/19.  But this install *** WORKS ***.  Why?????  I don't really understand what changed ... :(
  I even have logs with errors.  But I can't recreate those errors any longer ...

  Did I just benefit from all the improvements to the packaging tools?  Maybe ...