
import os
import sys
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestOsnapMac(spafit.Spafit):
    def __init__(self):
        super().__init__('osnap_mac')

    def run(self):

        for d in ['build', 'dist', 'venv']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')
        # osnap expects this dir so we have to make it, even though its empty
        os.makedirs(self.test_name, exist_ok=True)

        subprocess.check_call('./make_venv.sh', shell=True)
        subprocess.check_call('./make_osnapy.sh', shell=True)
        subprocess.check_call('./make_installer.sh', shell=True)

        status_file = 'spafit_status.txt'  # we don't pass in a parameter so it's the generic name
        status_file_path = os.path.join('dist', '%s.app' % self.test_name, 'Contents', 'MacOS', status_file)
        try:
            os.remove(status_file_path)
        except FileNotFoundError:
            pass
        subprocess.check_call('open ./dist/%s.app' % self.test_name, env={}, shell=True)
        while not os.path.exists(status_file_path):
            time.sleep(3)
            print('waiting for %s' % status_file_path)
        shutil.move(status_file_path, '%s_status.txt' % self.test_name)

if __name__ == '__main__':
    t = TestOsnapMac()
    t.run()
