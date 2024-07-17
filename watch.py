from git import Repo
import time

class Watcher:
    # This class watches the current direcory, assuming it is a git repository. It uses git status to check for changes.

    def __init__(self, callback):
        self.repo = Repo(".")
        self.callback = callback

        self._prev_is_dirty = False

    def check(self):
        if self.repo.is_dirty():
            self.callback()
            self._prev_is_dirty = True
        elif self._prev_is_dirty:
            self.callback()
            self._prev_is_dirty = False

    def watch(self):
        while True:
            try:
                self.check()
                time.sleep(1)
            except KeyboardInterrupt:
                break
