from collections import OrderedDict
from .reference import Reference
from .property import Property


class Response:

    def __init__(self, name, definition, spec):
        self.definition = definition
        self.name = name
        self.spec = spec
        self.required = []
        self.properties = OrderedDict()

        self.set_response()

    def set_required(self):
        if 'required' not in self.definition:
            return

        self.required = self.definition['required']

    def resolve_all_of(self, all_of):
        reference = None
        definition = None
        for item in all_of:
            if "$ref" in item:
                reference = Reference(item['$ref'])
            elif "properties" in item:
                definition = item

        if reference is not None and definition is not None:
            if reference.name in self.spec.definition['definitions']:
                self.set_properties(self.spec.definition['definitions'][reference.name])
                self.set_properties(definition)

    def set_response(self):
        if "allOf" in self.definition:
            self.resolve_all_of(self.definition['allOf'])
        else:
            self.set_properties(self.definition)

    def set_properties(self, response):
        if "properties" not in response:
            return
        for name, definition in response["properties"].items():
            required = name in self.required
            self.properties[name] = Property(name, definition, required)

    def get_properties(self):
        return self.properties.values()

    def has_object_reference(self):
        for target_property in self.get_properties():
            if target_property.type == 'object':
                return True

        return False
