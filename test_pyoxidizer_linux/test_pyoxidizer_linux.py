
import sys
import os
import shutil
import subprocess
import time

sys.path.insert(0,'..')
import spafit.spafit as spafit


class TestBriefcaseLinux(spafit.Spafit):
    def __init__(self):
        super().__init__('pyoxidizer_linux')

    def run(self):

        for d in ['myapp']:
            try:
                shutil.rmtree(d)
            except FileNotFoundError:
                pass

        spafit.copy_files('..', '.')

        with open('pyoxidizer_1_error.log', 'w') as f1:
            cmd = 'cargo install pyoxidizer'
            assert subprocess.call(cmd, stderr=f1, shell=True) == 0
            cmd = '~/.cargo/bin/pyoxidizer init myapp'
            assert subprocess.call(cmd, stderr=f1, shell=True) == 0
            time.sleep(2)
            cmd = 'cp pyoxidizer.toml myapp'
            assert subprocess.call(cmd, stderr=f1, shell=True) == 0
            cmd = '~/.cargo/bin/pyoxidizer build myapp'
            assert subprocess.call(cmd, stderr=f1, shell=True) == 0
            time.sleep(2)

        with open('pyoxidizer_2_error.log', 'w') as f2:
            main_dir = os.path.abspath(os.path.join('myapp/build/apps/myapp/x86_64-unknown-linux-gnu/debug'))
            main_exe_path = os.path.join(main_dir, 'myapp')
            cmd = [main_exe_path, self.get_status_file_name()]
            subprocess.call(cmd, cwd='.', stderr=f2)

        print('%s done' % self.test_name)

        return True

if __name__ == '__main__':
    t = TestBriefcaseLinux()
    t.run()
