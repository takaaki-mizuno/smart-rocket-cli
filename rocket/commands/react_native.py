from rocket.generators.react_native import ModelGenerator
from rocket.generators.react_native import ScreenGenerator

from rocket.services import OpenApiService, ArchiveService
from rocket.entities.archive.sketch.sketch import Sketch


class ReactNative(object):

    @classmethod
    def generate_model(cls, project_path, swagger_path, model_name=None):

        specification = OpenApiService.parse(swagger_path)
        generator = ModelGenerator(project_path, specification)

        if model_name is not None:
            if model_name not in specification.responses.keys():
                print("[Error] This name is not defined in the api definition file: " + model_name)
                return "ERROR"
            if not generator.need_to_create(model_name):
                print("[Error] This name is in the exclude model name list: " + model_name)
                return "ERROR"
            print("Generate Model: " + model_name)
            generator.generate(model_name)

        for name, response in specification.responses.items():
            if generator.need_to_create(name):
                print("Generate Model: " + name)
                generator.generate(name)

        return "OK"

    @classmethod
    def generate_screen(cls, project_path, sketch_file_path, screen_name=None, ):

        archive = ArchiveService.extract(sketch_file_path)
        sketch = Sketch(archive)

        generator = ScreenGenerator(project_path, sketch)

        if screen_name is not None:
            screen = sketch.get_screen(screen_name)
            if screen is None:
                print("[Error] This name is not defined in the sketch file: SCREEN_" + screen_name)
                return "ERROR"
            generator.generate(screen)

        for name, screen in sketch.screens.items():
            generator.generate(screen)

        return "OK"
