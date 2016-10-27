
import subprocess

import spafit.spafit as spafit


def main():
    if spafit.is_mac():
        subprocess.check_call('./test_osnap_mac.sh', cwd='test_osnap_mac', shell=True)
        subprocess.check_call('./test_py2app.sh', cwd='test_py2app', shell=True)
    elif spafit.is_windows():
        subprocess.check_call('test_osnap_win.bat', cwd='test_osnap_win', shell=True)
        subprocess.check_call('test_pynsist.bat', cwd='test_pynsist', shell=True)

if __name__ == '__main__':
    main()