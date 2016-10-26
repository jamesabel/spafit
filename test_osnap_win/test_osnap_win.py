
import os
import sys
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.osnap_test_util as osnap_test_util

class TestOsnapWin(spafit.Spafit):
    def __init__(self):
        super().__init__('osnap_win')

    def run(self):

        # todo: make this common across pynsist and osnap
        elevate_tool_path = os.path.join(os.sep, 'Elevation', 'elevate.cmd')

        for d in ['build', 'dist']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        uninstall_cmd = '%s' % os.path.join(os.sep, 'Program Files (x86)', 'author', 'osnap_win', 'uninstall.exe')
        if os.path.exists(uninstall_cmd):
            print(uninstall_cmd)
            subprocess.check_call(uninstall_cmd, shell=True)
        # todo: figure out how to wait until the uninstall is completed

        spafit.copy_files('..', '.')
        # osnap expects this dir so we have to make it, even though its empty
        os.makedirs(self.test_name, exist_ok=True)

        osnap_test_util.make_osnapy(True)
        subprocess.check_call('make_installer.bat', shell=True)

        # todo: make this a function somehow to share across pynsist and osnap
        if not os.path.exists(elevate_tool_path):
            print('error: %s does not exist' % elevate_tool_path)
            print('get it from http://download.microsoft.com/download/f/d/0/fd05def7-68a1-4f71-8546-25c359cc0842/Elevation2008_06.exe')
            print('see https://technet.microsoft.com/en-us/library/cc510320.aspx for more information')
            return False
        install_cmd = '%s %s' % (elevate_tool_path, os.path.join('installers', 'osnap_win_installer.exe'))
        print(install_cmd)
        subprocess.check_call(install_cmd)

        # todo: make a routine that gets us the base dir for installed files
        osnap_win_exe = os.path.join(os.sep, 'Program Files (x86)', 'author', 'osnap_win', 'osnap_win.exe')
        while not os.path.exists(osnap_win_exe):
            print('waiting for %s' % osnap_win_exe)
            time.sleep(5)
        time.sleep(10)  # ensure all files written out
        launch_cmd = '"%s"' % osnap_win_exe
        print(launch_cmd)
        subprocess.check_call(launch_cmd, shell=True)

        # currently osnap doesn't take parameters
        status_file_path = 'spafit.txt'
        while not os.path.exists(status_file_path):
            time.sleep(3)
            print('waiting for %s' % status_file_path)
        shutil.move(status_file_path, spafit.get_status_file_path(self.test_name))

        return True

if __name__ == '__main__':
    t = TestOsnapWin()
    t.run()
