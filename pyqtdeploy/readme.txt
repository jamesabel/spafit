
- I had to set (export) SYSROOT.  See run_pyqtdeploy.sh  and the docs for pyqtdeploy .

- In the pyqtdeploy app, you have to select the Build tab and hit the Build button.

- I needed qmake - to get that I had to:
  - brew install qt
  - brew linkapps qt
  - Fill in the qmake executable path (in this case: /usr/local/Cellar/qt/4.8.7_2/bin/qmake) in the pyqtdeploy app.
  - export CPATH=/System/Library/Frameworks/Python.framework/Headers to get the C headers.

- HOWEVER, I still got this when I ran 'make' from the 'build' directory:

make: *** No rule to make target `/Library/Frameworks/Python.framework/Versions/3.5/src/Python-3.5.2/Modules/_heapqmodule.c', needed by `_heapqmodule.o'.  Stop.

So, it appears that this tool has created a C app that is a representation of the Python app.
