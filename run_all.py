
import subprocess

import spafit.spafit as spafit


def main():
    if spafit.is_mac():
        pass
    elif spafit.is_windows():
        subprocess.check_call('test_pynsist.bat', cwd='test_pynsist', shell=True)

if __name__ == '__main__':
    main()
