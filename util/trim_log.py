
import re
import os


def main():
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
    with open('system.log', 'w') as f:
        for line in lines:
            if key_string in line:
                f.write('%s\n' % line)

if __name__ == '__main__':
    main()
