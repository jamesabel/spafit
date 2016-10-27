
import os
import sys

sys.path.insert(0,'..')
import spafit.spafit as spafit


def get_mac_status_file_path(test_name):
    return os.path.abspath(os.path.join('dist', '%s.app' % test_name, 'Contents', 'MacOS',
                                                    spafit.get_status_file_name()))
