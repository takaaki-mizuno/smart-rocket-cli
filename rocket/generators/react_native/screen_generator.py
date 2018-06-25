from .base_generator import BaseGenerator
from rocket.entities.archive.sketch.sketch import Sketch
from rocket.entities.archive.sketch.element import Element
from rocket.entities.archive.sketch import Screen
from rocket.entities.file import Directory, File
from rocket.helpers import StringHelper, LogHelper
from rocket.services import TemplateService
import os


class ScreenGenerator(BaseGenerator):
    excludes = ['List']

    def __init__(self, project_path, sketch: Sketch):
        self.project_path = project_path
        self.sketch = sketch

    def generate(self, screen: Screen) -> None:

        LogHelper.logger().info('Generate Screen: ' + screen.name)

        self.generate_screen(screen.name, screen)

        screen_directory = self.get_screen_directory(screen.name)
        component_directory = screen_directory.directory('components')
        component_directory.create()

        self.generate_component(component_directory, screen)

    def get_screen_directory(self, name: str) -> Directory:
        path = os.path.realpath(self.project_path + '/src/screens/' + StringHelper.upper_first(name))

        return Directory(path)

    def get_file(self, directory: Directory, name: str) -> File:
        directory.create()
        return directory.file(name)

    def generate_screen(self, name: str, screen: Screen) -> None:
        directory = self.get_screen_directory(name)

        TemplateService.render_to_file('react_native/screen/index.tmpl', {'screen': screen},
                                       self.get_file(directory, 'index.js').path())
        TemplateService.render_to_file('react_native/screen/screen.tmpl', {'screen': screen},
                                       self.get_file(directory, 'Screen.js').path())
        TemplateService.render_to_file('react_native/screen/store.tmpl', {'screen': screen},
                                       self.get_file(directory, 'Store.js').path())
        TemplateService.render_to_file('react_native/screen/styles.tmpl', {'screen': screen},
                                       self.get_file(directory, 'Styles.js').path())

    def generate_component(self, directory: Directory, element: Element) -> None:
        if element is None:
            return

        if element.should_export_component():
            file = directory.file(element.component_name() + '.js').path()
            TemplateService.render_to_file(element.component_template_name(), {'element': self}, file)
        else:
            if element.elements is not None:
                for child in element.elements:
                    self.generate_component(directory, child)

        return
