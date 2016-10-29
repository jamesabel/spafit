
from cx_Freeze import setup, Executable

executables = [
    Executable('main.py')
]

setup(name='cx_freeze_win',
      version='0.1',
      description='cx_freeze_win',
      executables=executables
      )
