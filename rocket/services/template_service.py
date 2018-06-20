from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader(
    os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../templates')
    , encoding='utf8'))


class TemplateService:
    @classmethod
    def get_template_path(cls):
        return os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../templates')

    @classmethod
    def render(cls, template, values):
        template = env.get_template(template)
        html = template.render(values)

        return html

    @classmethod
    def render_to_file(cls, template, values, destination_path):
        html = cls.render(template, values)

        file = open(destination_path, 'w')
        file.write(html)
        file.close()
