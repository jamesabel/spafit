
import sys
import os
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestPyinstaller(spafit.Spafit):
    def __init__(self):
        super().__init__('pyinstaller_linux')

    def run(self):

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        with open('pyinstaller_onefile_1_error.log', 'w') as f1:
            # eventually add --windowed but leave it out now so we can capture the error output from the executable
            pyinstaller_cmd = '%s --onefile -y --noupx -d all main.py' % os.path.join('venv', 'bin', 'pyinstaller')
            print(pyinstaller_cmd)
            subprocess.call(pyinstaller_cmd, stderr=f1, shell=True)
            time.sleep(2)

        with open('pyinstaller_onefile_2_error.log', 'w') as f2:
            main_dir = os.path.abspath('dist')
            main_exe_path = os.path.join(main_dir, 'main')
            cmd = [main_exe_path, self.get_status_file_name()]
            subprocess.call(cmd, cwd='.', stderr=f2)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestPyinstaller()
    t.run()
