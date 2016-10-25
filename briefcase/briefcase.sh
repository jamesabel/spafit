#!/usr/bin/env bash
rm *.log
../util/copy_files.sh .. .
# follow the briefcase conventions
mkdir -p main
mv main.py main/app.py
touch main/__init__.py
./make_venv.sh
rm -r macOS/
venv/bin/python3 setup.py macos
# run as if we double clicked on the app
open macOS/main.app
grep -i co.abel.main  /private/var/log/system.log > system.log
# assuming it's not going to work, do this so we can see the error
./macOS/main.app/Contents/MacOS/main > status.log 2>&1
cat status.log
