
import os
import sys
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestCxFreeze(spafit.Spafit):
    def __init__(self):
        super().__init__('cx_freeze')

    def run(self):
        # doesn't even install on Python 3.5
        # last PyPI is from 2014-12-26
        raise NotImplementedError

if __name__ == '__main__':
    t = TestCxFreeze()
    t.run()
