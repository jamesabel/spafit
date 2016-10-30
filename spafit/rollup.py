
import glob

def rollup():
    for d in glob.glob('test_*'):
        print(d)
