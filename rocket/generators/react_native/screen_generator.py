from .base_generator import BaseGenerator
from rocket.services import ArchiveService
from rocket.entities.archive.sketch.sketch import Sketch


class ScreenGenerator(BaseGenerator):
    excludes = ['List']

    def __init__(self, project_path, sketch_file_path):
        self.project_path = project_path
        self.sketch_file_path = sketch_file_path

    def generate(self, name=None):
        directory = ArchiveService.extract(self.sketch_file_path)
        sketch = Sketch(directory)
        if name is None:
            for name, screen in sketch.screens.items():
                print(name)
                print(screen.elements)

            return

        screen = sketch.get_screen(name)
        if screen is None:
            return

        print(screen.elements)
