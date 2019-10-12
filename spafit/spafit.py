
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

    def get_status_file_name(self):
        return get_status_file_name(self.test_name)


def is_windows():
    return platform.system().lower()[0] == 'w'


def is_mac():
    # darwin
    return platform.system().lower()[0] == 'd'


def is_linux():
    return platform.system().lower()[0] == 'l'


def get_pip_path():
    return os.path.join(get_python_dir(), 'pip3')


def get_python_path():
    return os.path.join(get_python_dir(), 'python3')


def get_python_dir():
    # todo: allow to be set via en environment variable
    if is_mac():
        return '/Library/Frameworks/Python.framework/Versions/3.5/bin'
    elif is_linux():
        return '/usr/bin'
    elif is_windows():
        # figure this out when I get to Windows
        raise NotImplementedError
    else:
        raise NotImplementedError


def get_status_file_name(test_name=DEFAULT_TEST_NAME):
    return '%s_status.log' % test_name


def copy_files(src_dir, dest_dir):
    files = ['main.py']
    if is_windows():
        files.append('main.bat')
    elif is_mac():
        # darwin == mac
        files.append('main.sh')
    elif is_linux():
        pass
    else:
        raise NotImplementedError
    [shutil.copy2(os.path.join(src_dir, fn), os.path.join(dest_dir, fn)) for fn in files]


def trim_log(test_name):
    app_name = 'main'

    system_log_path = os.path.join(os.sep, 'private', 'var', 'log', 'system.log')

    input('please hit return when the log window comes up')
    print('ok - continuing - reading %s' % system_log_path)

    lines = []
    print('reading %s' % system_log_path)
    with open(system_log_path, 'rb') as f:
        for l in f:
            try:
                l = l.decode()
            except UnicodeDecodeError:
                l = None
            if l:
                l = l.strip()
            # print(l)
            if l:
                lines.append(l.strip())

    # e.g.:
    # Oct 26 23:44:42 jamesmacbookpro main[72126]: main Error
    # Oct 26 23:44:42 jamesmacbookpro main[72126]: 2016-10-26 23:44:42.881 main[72126:4588758] main Error
    # ...
    match = re.search(r'%s\[(\d+)\]' % app_name, lines[-1])
    key_string = None
    if match:
        key_string = '%s[%s]' % (app_name, match.group(1))

    # e.g.:
    # Oct 27 22:21:11 jamesmacbookpro com.apple.xpc.launchd[1] (co.abel.main.368672[4464]): Service exited with abnormal code: 1
    # (need to then look at the output from the app separately from running the .app)
    if 'co.abel.main' in lines[-1]:
        key_string = lines[-1]
    with open('%s_1_error.log' % test_name, 'w') as f:
        for line in lines:
            if key_string and key_string in line:
                f.write('%s\n' % line)
