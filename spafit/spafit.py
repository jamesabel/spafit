
import os
import shutil
import platform
import re


DEFAULT_TEST_NAME = 'spafit'


class Spafit():
    def __init__(self, test_name):
        self.test_name = test_name
        print('%s starting' % self.test_name)
        with open(get_status_file_name(test_name), 'w') as f:
            f.write('FAIL\n')

    def run(self):
        # derived classes provide this
        raise NotImplementedError


def is_windows():
    return platform.system().lower()[0] == 'w'


def is_mac():
    # darwin
    return platform.system().lower()[0] == 'd'


def get_pip_path():
    return os.path.join(get_python_dir(), 'pip3')


def get_python_path():
    return os.path.join(get_python_dir(), 'python3')


def get_python_dir():
    # todo: allow to be set via en environment variable
    if is_mac():
        return '/Library/Frameworks/Python.framework/Versions/3.5/bin'
    elif is_windows():
        # figure this out when I get to Windows
        raise NotImplementedError
    else:
        raise NotImplementedError


def get_status_file_name(test_name=DEFAULT_TEST_NAME):
    return '%s_status.txt' % test_name


def copy_files(src_dir, dest_dir):
    files = ['main.py']
    if is_windows():
        files.append('main.bat')
    elif is_mac():
        # darwin == mac
        files.append('main.sh')
    else:
        raise NotImplementedError
    [shutil.copy2(os.path.join(src_dir, fn), os.path.join(dest_dir, fn)) for fn in files]


def trim_log(test_name):
    app_name = 'main'

    system_log_path = os.path.join(os.sep, 'private', 'var', 'log', 'system.log')

    input('please hit return when the log window comes up')
    print('ok - continuing - reading %s' % system_log_path)

    with open(system_log_path) as f:
        lines = [l.strip() for l in f]
    match = re.search(r'%s\[(\d+)\]' % app_name, lines[-1])
    key_string = None
    if match:
        key_string = '%s[%s]' % (app_name, match.group(1))
    else:
        print('fatal error reading %s' % system_log_path)
        exit()
    with open('%s_error.log' % test_name, 'w') as f:
        for line in lines:
            if key_string in line:
                f.write('%s\n' % line)