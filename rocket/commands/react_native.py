from rocket.generators.react_native import ModelGenerator
from rocket.generators.react_native import ScreenGenerator

from rocket.services import OpenApiService


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
    def generate_screen(cls, project_path, screen_name, sketch_file_path):

        generator = ScreenGenerator(project_path)


        return "OK"
