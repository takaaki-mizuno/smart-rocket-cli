from .reference import Reference
from rocket.helpers.string_helper import StringHelper


class Property:

    def __init__(self, name, definition, required=False):
        self.name = name
        self.definition = definition
        self.required = required

        self.type = 'unknown'
        self.description = ''
        self.item_property = ''
        self.object_reference = None

        self.parse()

    def parse(self):
        self.type = self.definition['type'] if 'type' in self.definition else 'unknown'
        self.description = self.definition['description'] if 'description' in self.definition else ''

        if self.type == 'array' and 'items' in self.definition:
            self.item_property = Property('items', self.definition['items'], True)
        elif self.type == 'object' and '$ref' in self.definition:
            self.object_reference = Reference(self.definition['$ref'])

    def get_default_value(self):
        if self.type in {'string'}:
            return "''"
        elif self.type in {'number', 'integer'}:
            return '0'
        elif self.type in {'boolean', 'bool'}:
            return 'false'
        elif self.type in {'array'}:
            return '[]'
        elif self.type in {'object'}:
            return 'null'

        return 'null'

    def get_mock_value(self):
        if self.name == 'id':
            return 'Faker.random.number()'
        elif StringHelper.endswith(self.name, 'name') and self.type in {'string'}:
            return 'Faker.name.findName()'
        elif StringHelper.endswith(self.name, 'imageUrl') and self.type in {'string'}:
            return 'ModelHelper.getDummyImageUrl(800, 600)'
        elif StringHelper.endswith(self.name, 'url') and self.type in {'string'}:
            return 'Faker.internet.url()'
        elif StringHelper.endswith(self.name, 'email') and self.type in {'string'}:
            return 'Faker.internet.email()'
        elif StringHelper.endswith(self.name, 'description') and self.type in {'string'}:
            return 'Faker.lorem.sentence()'
        elif StringHelper.endswith(self.name, 'at') and self.type in {'integer'}:
            return '0'

        if self.type in {'string'}:
            return "''"
        elif self.type in {'number', 'integer'}:
            return '0'
        elif self.type in {'boolean', 'bool'}:
            return 'false'
        elif self.type in {'array'}:
            return '[]'
        elif self.type in {'object'}:
            return self.object_reference.name + '.mock()'

        return 'null'
