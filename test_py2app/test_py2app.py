
import sys
import shutil
import subprocess

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestPy2app(spafit.Spafit):
    def __init__(self):
        super().__init__('py2app')

    def run(self):

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

        subprocess.check_call('open ./dist/main.app', env={}, shell=True)
        spafit.trim_log(self.test_name)

        return True

if __name__ == '__main__':
    t = TestPy2app()
    t.run()
