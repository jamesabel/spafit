
# todo: make the mac and win versions source the same file, since they are identical except for application name

import osnap.installer


def make_installer(verbose):
    osnap.installer.make_installer('3.5.2', 'osnap_win', 'author', 'osnap_win', 'www.abel.co', verbose=verbose)


if __name__ == '__main__':
    make_installer(True)