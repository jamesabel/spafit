
import distutils.core
import py2exe

# todo: WIP - finish on a Windows system

distutils.core.setup(

    name='spafit',
    version='0.0.0',
    author='abel',
    author_email='j@abel.co',
    url='http://www.github.com/jamesabel/spafit',
    license='LICENSE',  # points to the actual file
    description='py2exe test case',

    options = {'py2exe': {'bundle_files': 1,
                          #'compressed': True,
                          #'optimize': 0,
                          "includes" : ["PyQt5", "cryptography"]}},
    #console=[latus.const.MAIN_FILE],
    windows=['main.py'],
    # zipfile=None,  # a single executable
)
