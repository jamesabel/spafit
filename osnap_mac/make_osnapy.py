
import osnap.osnapy


def create_osnapy(verbose):
    osnap.osnapy.make_osnapy('3.5.2', 'osnap_mac', force_app_uninstall=True, verbose=verbose)


if __name__ == '__main__':
    create_osnapy(True)
