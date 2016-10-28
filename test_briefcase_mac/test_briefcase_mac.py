
import sys
import os
import shutil
import subprocess

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.spafit_mac as spafit_mac


class TestBriefcaseMac(spafit.Spafit):
    def __init__(self):
        super().__init__('briefcase_mac')

    def run(self):

        status_file_path = spafit_mac.get_mac_status_file_path(self.test_name)

        if False:
            try:
                os.remove(status_file_path)
            except FileNotFoundError:
                pass

            for d in ['build', 'dist', 'macOS']:
                try:
                    shutil.rmtree(d)
                except FileNotFoundError:
                    pass

            spafit.copy_files('..', '.')

            subprocess.check_call('venv/bin/pip3 install -U -r requirements.txt', env={}, shell=True)
            subprocess.check_call('venv/bin/python3 setup.py macos', env={}, shell=True)

        try:
            subprocess.check_call('open ./macOS/main.app', env={}, shell=True)
        except subprocess.CalledProcessError:
            pass

        try:
            shutil.move(status_file_path, spafit.get_status_file_name(self.test_name))
        except FileNotFoundError:
            pass

        spafit.trim_log(self.test_name)

        # if it doesn't work, do this so we can see the error
        # note that if it doesn't work, the call will fail, so we can't do a check_call()
        subprocess.call('./macOS/main.app/Contents/MacOS/main > %s_2_error.log 2>&1' % self.test_name, env={},
                        shell=True)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestBriefcaseMac()
    t.run()