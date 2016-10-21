#!/usr/bin/env bash
# usage: copy_files.sh source_dir dest_dir
echo $0
set -x
if [ -z "$1" ]; then echo "error: parameter 1 not set - exiting"; exit; fi
if [ -z "$2" ]; then echo "error: parameter 2 not set - exiting"; exit; fi
cp -f $1/main.py $2
cp -f $1/make_venv.sh $2
cp -f $1/main.sh $2
