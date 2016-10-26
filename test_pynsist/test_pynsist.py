
import os
import sys
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestPynsist(spafit.Spafit):
    def __init__(self):
        super().__init__('pynsist')

    def run(self):

        # todo: make this common across pynsist and osnap
        elevate_tool_path = os.path.join(os.sep, 'Elevation', 'elevate.cmd')

        for d in ['build']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        # todo: make a routine that gets us the base dir for installed files
        uninstall_cmd = '%s' % os.path.join(os.sep, 'Program Files', 'pynsist', 'uninstall.exe')
        if os.path.exists(uninstall_cmd):
            print(uninstall_cmd)
            subprocess.check_call(uninstall_cmd, shell=True)

        spafit.copy_files('..', '.')

        nsist_cmd = '%s -m nsist installer.cfg' % os.path.join('venv', 'Scripts', 'python.exe')
        print(nsist_cmd)
        subprocess.check_call(nsist_cmd)
        time.sleep(2)

        if not os.path.exists(elevate_tool_path):
            print('error: %s does not exist' % elevate_tool_path)
            print('get it from http://download.microsoft.com/download/f/d/0/fd05def7-68a1-4f71-8546-25c359cc0842/Elevation2008_06.exe')
            print('see https://technet.microsoft.com/en-us/library/cc510320.aspx for more information')
            return False
        install_cmd = '%s %s' % (elevate_tool_path, os.path.join('build', 'nsis', 'pynsist_1.0.exe'))
        print(install_cmd)
        subprocess.check_call(install_cmd)

        pyw_exe = os.path.join(os.sep, 'Windows', 'pyw.exe')
        launch_pyw = os.path.join(os.sep, 'Program Files', 'pynsist', 'pynsist.launch.pyw')
        while not os.path.exists(launch_pyw):
            print('waiting for %s' % launch_pyw)
            time.sleep(5)
        time.sleep(10)  # ensure all files written out
        launch_cmd = '%s "%s" %s' % (pyw_exe, launch_pyw, os.path.abspath(spafit.get_status_file_path(self.test_name)))
        print(launch_cmd)
        subprocess.check_call(launch_cmd, shell=True)

        return True

if __name__ == '__main__':
    t = TestPynsist()
    t.run()
