import os
from rocket.services import TemplateService
from .base_generator import BaseGenerator


class ModelGenerator(BaseGenerator):
    excludes = ['List']

    def __init__(self, project_path, specification):
        self.project_path = project_path
        self.specification = specification

    def need_to_create(self, name):
        return True if name not in self.excludes else False

    def get_path(self, name):
        return os.path.realpath(self.project_path + '/src/models/' + name + '.js')

    def get_index_path(self):
        return os.path.realpath(self.project_path + '/src/models/index.js')

    @classmethod
    def get_index_line(cls, name):
        return "export { default as " + name + " } from './" + name + "';"

    def generate(self, name):
        if not self.need_to_create(name):
            return False

        definition = self.specification.get_response(name)

        values = {
            'definition': definition
        }

        print(self.get_path(name))

        TemplateService.render_to_file('react_native/model.tmpl', values, self.get_path(name))

        self.add_to_index(self.get_index_line(name), self.get_index_path())
