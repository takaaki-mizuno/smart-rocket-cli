from .base_generator import BaseGenerator


class ScreenGenerator(BaseGenerator):
    excludes = ['List']

    def __init__(self, project_path):
        self.project_path = project_path
