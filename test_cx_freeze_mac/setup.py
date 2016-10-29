
from cx_Freeze import setup, Executable

executables = [
    Executable('main.py')
]

setup(name='cx_freeze_mac',
      version='0.1',
      description='cx_freeze_mac',
      executables=executables
      )
