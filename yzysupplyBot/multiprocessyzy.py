import subprocess
import multiprocessing
from subprocess import call
import os

def worker(file):
    # subprocess.call(['python', file])
    # subprocess.Popen(['screen', file])
    os.system('python ' + file)

if __name__ == "__main__":
    files = ['multiprocessyzy.py']
    for i in files:
        p = multiprocessing.Process(target=worker(i))
        p.start()
