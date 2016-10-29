
import subprocess

import spafit.spafit as spafit


def main():
    if spafit.is_mac():
        subprocess.check_call('./test_briefcase_mac.sh', cwd='test_briefcase_mac', shell=True)
        subprocess.check_call('./test_cx_freeze_mac.sh', cwd='test_pyinstaller_mac', shell=True)
        subprocess.check_call('./test_osnap_mac.sh', cwd='test_osnap_mac', shell=True)
        subprocess.check_call('./test_py2app.sh', cwd='test_py2app', shell=True)
        subprocess.check_call('./test_pyinstaller_mac.sh', cwd='test_pyinstaller_mac', shell=True)
    elif spafit.is_windows():
        # briefcase does not yet support Windows
        # subprocess.check_call('test_briefcase_win.bat', cwd='test_briefcase_win', shell=True)
        subprocess.check_call('test_cx_freeze_win.bat', cwd='test_cx_freeze_win', shell=True)
        subprocess.check_call('test_osnap_win.bat', cwd='test_osnap_win', shell=True)
        subprocess.check_call('test_py2exe.bat', cwd='test_py2exe', shell=True)
        subprocess.check_call('test_pyinstaller_win.bat', cwd='test_pyinstaller_win', shell=True)
        subprocess.check_call('test_pynsist.bat', cwd='test_pynsist', shell=True)

if __name__ == '__main__':
    main()
