from pathlib import Path
import os


class File:

    def __init__(self, path):
        self._path = os.path.realpath(path)

    def exists(self) -> bool:
        return os.path.exists(self._path)

    def save(self, content: str) -> None:
        path = Path(self._path)
        with path.open('w') as file:
            file.write(content)

    def append(self, content: str):
        path = Path(self._path)
        with path.open('a') as file:
            file.write(content)

    def get(self) -> str:
        if not self.exists():
            return ''

        path = Path(self._path)
        with path.open() as file:
            content = file.read()
            return content

    def path(self) -> str:
        return self._path
