import os
import sys
from PyQt5.QtCore import QFileSystemWatcher, QCoreApplication

class DirectoryWatcher:
    def __init__(self, directory_to_watch, callback):
        self.callback = callback
        self.directory_to_watch = directory_to_watch

        # Set up the file system watcher
        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(directory_to_watch)

        # Track files being watched
        self.files_watched = set()

        # Connect the signals to the appropriate slots
        self.watcher.directoryChanged.connect(self.on_directory_changed)
        self.watcher.fileChanged.connect(self.on_file_changed)

        # Add all files in the directory to the watcher
        self.add_files_in_directory()

    def add_files_in_directory(self):
        for filename in os.listdir(self.directory_to_watch):
            full_path = os.path.join(self.directory_to_watch, filename)
            if os.path.isfile(full_path) and full_path not in self.files_watched:
                self.watcher.addPath(full_path)
                self.files_watched.add(full_path)

    def on_directory_changed(self, path):
        # Handle directory change event
        self.callback(f"Directory changed: {path}")
        self.add_files_in_directory()

    def on_file_changed(self, path):
        # Handle file change event
        self.callback(f"File changed: {path}")
        # Re-add the file to the watcher to continue watching after change
        self.watcher.addPath(path)

if __name__ == '__main__':
    def print_callback(message):
        print(message)

    app = QCoreApplication(sys.argv)
    directory_to_watch = '/path/to/your/directory'  # Change this to the directory you want to watch
    watcher = DirectoryWatcher(directory_to_watch, print_callback)
    sys.exit(app.exec_())
