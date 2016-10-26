
import osnap.osnapy
import spafit.osnap_test_util as osnap_test_util


def create_osnapy(verbose):
    osnap.osnapy.make_osnapy(osnap_test_util.get_python_version(), osnap_test_util.get_test_name(),
                             force_app_uninstall=True, verbose=verbose)


if __name__ == '__main__':
    create_osnapy(True)
