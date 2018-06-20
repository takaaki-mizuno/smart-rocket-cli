from .parameter import Parameter
from .response import Reference


class Endpoint:

    def __init__(self, path, method, definition, spec):
        self.path = path
        self.method = method
        self.definition = definition
        self.spec = spec

        self.parameters = []
        self.response = None
        self.parse()

    def parse(self):
        self.parse_parameters()
        self.parse_response()

    def parse_parameters(self):
        if 'parameters' not in self.definition:
            return

        for parameter in self.definition['parameters']:
            self.parameters.append(Parameter(parameter))

    def parse_response(self):
        if 'responses' not in self.definition:
            return

        for name, definition in self.definition['responses'].items():
            if name[0:1] == '2' and 'schema' in definition:
                self.response = Reference(definition['schema']['$ref'])
