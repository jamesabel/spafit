
import os
import sys
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestPyinstaller(spafit.Spafit):
    def __init__(self):
        super().__init__('pyinstaller_win')

    def run(self):

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        with open('pyinstaller_1_error.log', 'w') as f1:
            # eventually add --windowed but leave it out now so we can capture the error output from the executable
            pyinstaller_cmd = '%s -y --noupx -d main.py' % os.path.join('venv', 'Scripts', 'pyinstaller.exe')
            print(pyinstaller_cmd)
            subprocess.call(pyinstaller_cmd, stderr=f1)
            time.sleep(2)

        with open('pyinstaller_2_error.log', 'w') as f2:
            main_dir = os.path.abspath(os.path.join('dist', 'main'))
            main_exe_path = os.path.join(main_dir, 'main.exe')
            subprocess.call(main_exe_path, cwd=main_dir, stderr=f2)

        return True

if __name__ == '__main__':
    t = TestPyinstaller()
    t.run()
