

import sys
import os
import shutil
import subprocess

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.spafit_mac as spafit_mac


class TestBriefcaseMac(spafit.Spafit):
    def __init__(self):
        super().__init__('briefcase_win')

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

        # todo: make a function to make the log file name (don't do it manually every time - could end up with inconsistencies)
        with open('briefcase_1_error.log', 'w') as f:
            cmd = '%s setup.py win' % os.path.join('venv', 'scripts', 'python.exe')
            print(cmd)
            subprocess.check_call(cmd, env={}, stdout=f, stderr=f, shell=True)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestBriefcaseMac()
    t.run()