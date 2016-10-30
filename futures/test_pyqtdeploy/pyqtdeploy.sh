#!/usr/bin/env bash
rm -rf build dist .eggs venv
../util/copy_files.sh .. .
./make_venv.sh
# py2app won't work from my venv so I have to install (pollute) my base python3
# e.g. https://bitbucket.org/ronaldoussoren/py2app/issues/61/py2app-run-in-virtualenv-does-not-copy
#  and https://github.com/micahflee/onionshare/issues/241
pip3 install -U -r requirements.txt
# python3 setup.py py2app
# run as if we double clicked on the app
#open ./dist/main.app
#venv/bin/python3 ../util/trim_log.py
#cat ./system.log
