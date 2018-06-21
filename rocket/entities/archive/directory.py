import shutil
from pathlib import Path
import os
import tempfile
import zipfile


class Directory:

    def __init__(self, path):
        self.path = path
        self.temporary_directory = None

    def __del__(self):
        self.delete_directory()

    def extract(self):
        self.temporary_directory = tempfile.TemporaryDirectory().name
        zip_ref = zipfile.ZipFile(self.path, 'r')
        zip_ref.extractall(self.temporary_directory)
        zip_ref.close()

    def delete_directory(self):
        directory = Path(self.temporary_directory)
        if directory.exists():
            shutil.rmtree(self.temporary_directory)
            return True

        return False

    def get_real_path(self, relative_path):
        if relative_path[0] != '/':
            relative_path = '/' + relative_path

        return os.path.realpath(self.temporary_directory + relative_path)

    def get_real_path_content(self, relative_path):
        path = Path(self.get_real_path(relative_path))
        if not path.exists():
            return None

        with path.open() as file:
            content = file.read()

        return content

    def get_directory_files(self, relative_path, extension=None):

        path = Path(self.get_real_path(relative_path))
        if not path.is_dir():
            return []

        result = []

        files = os.listdir(path.absolute())
        if extension is not None:
            if extension[0] != '.':
                extension = '.' + extension

        for file in files:
            file_path = Path(os.path.realpath(path.absolute() + '/' + file))
            if extension is not None:
                if file.endswith(extension):
                    result.append(file_path)
            else:
                result.append(file_path)

        return result
