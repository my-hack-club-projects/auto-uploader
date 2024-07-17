import sys

from watch import Watcher
from upload import upload

def callback():
    print("A change has been detected")

def main(path):
    watcher = Watcher(path, upload)
    watcher.watch()

if __name__ == '__main__':
    path = None

    if len(sys.argv) < 2:
        print("Please input a path to a git repository")
        path = input("Path: ")
    else:
        path = sys.argv[1]

    main(path)