
import glob
import re
import os
import collections


def test_name_os_from_dir(test_dir):
    """
    takes a test name and returns a tuple with the test name and the OS
    :param test_dir: raw name of test dir
    :return: tuple with <test_name> , <OS>
    """
    # tolerates _ in test name
    s = re.search(r'test_([0-9a-z_]+)_(mac|win)', test_dir)
    return s.group(1), s.group(2)


def test_os_to_strings(test_name, supported, test_os, issues):
    if supported:
        status_file_path = os.path.join('test_' + test_name + '_' + test_os, test_name.replace('test_', '') + '_' + test_os + '_status.log')
        if os.path.exists(status_file_path):
            with open(status_file_path) as f:
                status = f.readline().strip()
            if 'pass' in status.lower():
                status = ':white_check_mark: %s' % status
            else:
                status = ':x: %s' % status
        else:
            status = ':x: FAILED'
        # issues.append(test_name)
    else:
        status = ':no_entry: Not Supported'
    return status


def rollup():
    tests = collections.defaultdict(list)
    for d in [d for d in glob.glob('test_*')]:
        test, test_os = test_name_os_from_dir(d)
        tests[test].append(test_os)
    print(tests)

    intro = "\
## SPAFIT - Small Python Application Freezer/Installer Test ##\n\
\
Notes\n\
- Generally tried to use Python 3.5.  If a tool failed with 3.5 I tried 3.4.\
  However, no tool that failed on 3.5 then passed on 3.4.\n\
    "

    with open('readme.md', 'w') as f:
        f.write(intro)
        f.write('\n')
        f.write('| Tool | Win | Mac | Issue |\n')
        f.write('|------|-----|-----|-------|\n')
        for test in sorted(tests):
            issues = []
            win = test_os_to_strings(test, 'win' in tests[test], 'win', issues)
            mac = test_os_to_strings(test, 'mac' in tests[test], 'mac', issues)
            f.write('| %s | %s | %s | %s |\n' % (test, win, mac, str(issues)))
