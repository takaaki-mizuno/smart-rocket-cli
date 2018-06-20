from rocket.helpers import DictionaryHelper


class Element:

    def __init__(self, object_id, name, layer, directory):
        self.directory = directory
        self.object_id = object_id
        self.name = name
        self.layer = layer
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        self.elements = []
        self.background_color = 'transparent'
        self.parse()

    def parse(self):
        self.get_size()
        self.get_background_color()
        self.parse_elements()

    def get_size(self):
        self.width = DictionaryHelper.get(self.layer, 'frame.width', 0)
        self.height = DictionaryHelper.get(self.layer, 'frame.height', 0)
        self.x = DictionaryHelper.get(self.layer, 'frame.x', 0)
        self.y = DictionaryHelper.get(self.layer, 'frame.y', 0)

    def get_background_color(self):
        has_background_color = DictionaryHelper.get(self.layer, 'hasBackgroundColor', False)
        if not has_background_color:
            self.background_color = 'transparent'
            return

        self.background_color = self.convert_color(DictionaryHelper.get(self.layer, 'backgroundColor', {}))

    def parse_elements(self):
        layers = DictionaryHelper.get(self.layer, 'layers')
        if layers is None:
            return
        for layer in layers:
            element = self.parse_element(layer)
            if element is not None:
                self.elements.append(element)

    def parse_element(self, layer):
        object_id = DictionaryHelper.get(self.layer, 'do_objectID')
        if object_id is not None:
            return None

        is_visible = DictionaryHelper.get(self.layer, 'isVisible', True)
        if not is_visible:
            return None

        name = DictionaryHelper.get(self.layer, 'name', True)

        element = Element(object_id, name, layer, self.directory)

        return element

    @classmethod
    def convert_color(cls, color):
        red = DictionaryHelper.get(color, 'red', 1)
        blue = DictionaryHelper.get(color, 'blue', 1)
        green = DictionaryHelper.get(color, 'green', 1)
        alpha = DictionaryHelper.get(color, 'alpha', 1)

        if alpha == 1:
            return '#%02x%02x%02x' % (red * 255, green * 255, blue * 255)

        return '#%02x%02x%02x%02x' % (red * 255, green * 255, blue * 255, alpha * 255)
