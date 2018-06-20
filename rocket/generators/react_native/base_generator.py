import os
from pathlib import Path
from rocket.services import TemplateService


class BaseGenerator(object):

    @classmethod
    def add_to_index(cls, statement, path):
        index_file = Path(os.path.dirname(path) + '/index.js')

        if index_file.is_file():
            index = 0
            found = -1
            with index_file.open() as file:
                for line in file:
                    if line.find(statement) >= 0:
                        found = index
                        break

            if found == -1:
                with index_file.open("a") as file:
                    file.write(statement + "\n")

        else:
            with index_file.open("w") as file:
                file.write(statement + "\n")
