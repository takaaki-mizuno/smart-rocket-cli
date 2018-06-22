from rocket.helpers import DictionaryHelper
from .element import Element
from .attributed_string import AttributeString


class Label(Element):

    def parse_specific_info(self):
        self.get_text()

    def get_text(self):
        self.data['string'] = DictionaryHelper.get(self.layer, 'attributedString.string')
        self.data['attribute_strings'] = []
        for attribute in DictionaryHelper.get(self.layer, 'attributedString.attributes', []):
            self.data['attribute_strings'].append(AttributeString(self.data['string'], attribute))

    @classmethod
    def type(cls):
        return "Label"
