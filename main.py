import sys
from PyQt5.QtCore import QCoreApplication

from watch import DirectoryWatcher

# from git import upload

def callback(message):
    print(message)

def main():
    app = QCoreApplication(sys.argv)
    watcher = DirectoryWatcher('test/', callback)

    return app

def signal_handler(sig, frame):
    print('Exiting...')
    sys.exit(0)

if __name__ == '__main__':
    app = main()

    sys.exit(app.exec_())
