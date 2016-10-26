
import osnap.osnapy

import spafit.spafit as spafit


def get_python_version():
    # we'll change this over time ... perhaps use an env var if set
    return '3.5.2'


def get_test_name():
    if spafit.is_mac():
        return 'osnap_mac'
    elif spafit.is_windows():
        return 'osnap_win'
    else:
        raise NotImplementedError


def make_osnapy(verbose):
    osnap.osnapy.make_osnapy(get_python_version(), get_test_name(), force_app_uninstall=True, verbose=verbose)
