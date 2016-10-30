
import sys
import os
import shutil
import subprocess

sys.path.insert(0,'..')
import spafit.spafit as spafit
import spafit.spafit_mac as spafit_mac


class TestPy2app(spafit.Spafit):
    def __init__(self):
        super().__init__('py2app_mac')

    def run(self):

        status_file_path = spafit_mac.get_mac_status_file_path(self.test_name)
        try:
            os.remove(status_file_path)
        except FileNotFoundError:
            pass

        for d in ['build', 'dist', '.eggs']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        # py2app won't work from my venv so I have to install (pollute) my base python3
        # e.g. https://bitbucket.org/ronaldoussoren/py2app/issues/61/py2app-run-in-virtualenv-does-not-copy
        #  and https://github.com/micahflee/onionshare/issues/241
        subprocess.check_call('%s install -U -r requirements.txt' % spafit.get_pip_path(), env={}, shell=True)
        subprocess.check_call('%s setup.py py2app' % spafit.get_python_path(), env={}, shell=True)

        try:
            subprocess.check_call('open ./dist/main.app', env={}, shell=True)
        except subprocess.CalledProcessError:
            pass

        try:
            shutil.move(status_file_path, spafit.get_status_file_name(self.test_name))
        except FileNotFoundError:
            pass

        spafit.trim_log(self.test_name)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestPy2app()
    t.run()
