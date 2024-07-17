import git
import time

class Watcher:
    # This class watches the current direcory, assuming it is a git repository. It uses git status to check for changes.

    def __init__(self, path, callback):
        self.callback = callback

        try:
            self.repo = git.Repo(path)
        except git.InvalidGitRepositoryError:
            print("This is not a git repository")
            exit(1)

    def check(self):
        if self.repo.is_dirty() or self.repo.untracked_files:
            print("Detected changes at " + str(time.time()))
            self.callback(self.repo, time.time())

    def watch(self):
        while True:
            try:
                self.check()
                time.sleep(1)
            except KeyboardInterrupt:
                break
