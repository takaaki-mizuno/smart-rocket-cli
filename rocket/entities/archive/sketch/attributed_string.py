from rocket.helpers import DictionaryHelper, ColorHelper


class AttributeString:

    def __init__(self, string, attribute):
        self.string = string
        self.attribute = attribute

        self.start = DictionaryHelper.get(attribute, 'location', 0)
        self.length = DictionaryHelper.get(attribute, 'length', 0)
        self.font_name = DictionaryHelper.get(
            attribute,
            'attributes.MSAttributedStringFontAttribute.attributes.name',
            '')
        self.font_size = DictionaryHelper.get(
            attribute,
            'attributes.MSAttributedStringFontAttribute.attributes.size',
            0)
        self.font_color = ColorHelper.convert_color(DictionaryHelper.get(attribute, 'MSAttributedStringColorAttribute'))
        self.alignment = DictionaryHelper.get(attribute, 'paragraphStyle.alignment', 0)

    def get_string(self):
        return self.string[self.start:self.length]

    def get_alignment(self):
        if self.alignment == 2:
            return 'center'
        elif self.alignment == 3:
            return 'right'

        return 'left'
