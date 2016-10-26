
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

        status_file_path = os.path.abspath(os.path.join('dist', '%s.app' % self.test_name, 'Contents', 'MacOS',
                                                        spafit.get_status_file_path()))

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')
        # osnap expects this dir so we have to make it, even though its empty
        os.makedirs(self.test_name, exist_ok=True)

        subprocess.check_call('./make_osnapy.sh', shell=True)  # has to be via shell since we have to get elevated sudo
        subprocess.check_call('./make_installer.sh', shell=True)

        try:
            os.remove(status_file_path)
        except FileNotFoundError:
            pass
        subprocess.check_call('open ./dist/%s.app' % self.test_name, env={}, shell=True)
        while not os.path.exists(status_file_path):
            time.sleep(3)
            print('waiting for %s (%s)' % (status_file_path, str(time.time())))
        shutil.move(status_file_path, '%s_status.txt' % self.test_name)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestOsnapMac()
    t.run()
