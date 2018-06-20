from collections import OrderedDict
from .endpoint import Endpoint
from .response import Response


class Specification:

    def __init__(self, definition):
        self.definition = definition
        self.responses = OrderedDict()
        self.endpoints = OrderedDict()

        self.set_response()
        self.set_endpoint()

    def set_endpoint(self):
        for name, methods in self.definition['paths'].items():
            for method, definition in methods.items():
                self.endpoints[name + ':' + method] = Endpoint(name, method, definition, self)

    def set_response(self):
        for name, definition in self.definition["definitions"].items():
            self.responses[name] = Response(name, definition, self)
        pass

    def get_response(self, name):
        if name in self.responses:
            return self.responses[name]

        return None
