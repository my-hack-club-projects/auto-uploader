import sys

from watch import Watcher

# from git import upload

def callback():
    print("A change has been detected")

def main():
    watcher = Watcher(callback)
    watcher.watch()

def signal_handler(sig, frame):
    print('Exiting...')
    sys.exit(0)

if __name__ == '__main__':
    main()
