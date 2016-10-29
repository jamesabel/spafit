
import sys
import os
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.spafit_mac as spafit_mac


class TestPy2app(spafit.Spafit):
    def __init__(self):
        super().__init__('cx_freeze_mac')

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

        with open('cx_freeze_mac_1_error.log', 'w') as f1:
            cmd = '%s setup.py build' % os.path.join('venv', 'bin', 'python')
            print(cmd)
            subprocess.call(cmd, stderr=f1, stdout=f1, shell=True)
            time.sleep(2)

        # todo: if this ever works, actually call the app

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestPy2app()
    t.run()
