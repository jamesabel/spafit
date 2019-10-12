
import sys
import os
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestCxFreeze(spafit.Spafit):
    def __init__(self):
        super().__init__('cx_freeze_linux')

    def run(self):

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        with open('cx_freeze_linux_1_error.log', 'w') as f1:
            cmd = '%s setup.py build' % os.path.join('venv', 'bin', 'python')
            print(cmd)
            subprocess.call(cmd, stderr=f1, stdout=f1, shell=True)
            time.sleep(2)

        with open('cx_freeze_linux_2_error.log', 'w') as f2:
            main_dir = os.path.abspath(os.path.join('build', 'exe.linux-x86_64-3.7'))
            main_exe_path = os.path.join(main_dir, 'main')
            subprocess.call(main_exe_path, cwd='.', stderr=f2)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestCxFreeze()
    t.run()
