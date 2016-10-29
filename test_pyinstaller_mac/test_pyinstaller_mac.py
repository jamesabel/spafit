
import sys
import os
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.spafit_mac as spafit_mac


class TestPyinstaller(spafit.Spafit):
    def __init__(self):
        super().__init__('pyinstaller_mac')

    def run(self):

        status_file_path = spafit_mac.get_mac_status_file_path(self.test_name)
        try:
            os.remove(status_file_path)
        except FileNotFoundError:
            pass

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        with open('pyinstaller_mac_1_error.log', 'w') as f1:
            # --windowed provides the main.app (OSX 'application')
            pyinstaller_cmd = '%s -y --noupx --windowed -d main.py' % os.path.join('venv', 'bin', 'pyinstaller')
            print(pyinstaller_cmd)
            subprocess.call(pyinstaller_cmd, stderr=f1, shell=True)
            time.sleep(2)

        with open('pyinstaller_mac_2_error.log', 'w') as f1:
            open_cmd = 'open ./dist/%s.app' % self.test_name
            print(open_cmd)
            subprocess.call(open_cmd, env={}, shell=True)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestPyinstaller()
    t.run()
