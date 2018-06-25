import os
from .file import File


class Directory:

    def __init__(self, path):
        self.path = os.path.realpath(path)

    def exists(self) -> bool:
        return os.path.exists(self.path)

    def create(self):
        if not self.exists():
            os.makedirs(self.path)

    def file(self, name: str):
        return File(self.path + '/' + name)

    def directory(self, name: str):
        return Directory(self.path + '/' + name)
