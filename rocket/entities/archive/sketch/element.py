from rocket.helpers import DictionaryHelper, ColorHelper


class Element:

    def __init__(self, object_id, name, layer, parent, directory):
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
        self.parent = parent
        self.data = {
            "width": 0,
            "height": 0,
            "x": 0,
            "y": 0,
            "elements": [],
            "background_color": 'transparent'
        }

        self.parse()

    def parse(self):
        self.get_size()
        self.get_background_color()
        self.get_image()
        self.parse_specific_info()

    def parse_specific_info(self):
        pass

    def get_size(self):
        self.data['width'] = DictionaryHelper.get(self.layer, 'frame.width', 0)
        self.data['height'] = DictionaryHelper.get(self.layer, 'frame.height', 0)
        self.data['x'] = DictionaryHelper.get(self.layer, 'frame.x', 0)
        self.data['y'] = DictionaryHelper.get(self.layer, 'frame.y', 0)

    def get_background_color(self):
        has_background_color = DictionaryHelper.get(self.layer, 'hasBackgroundColor', False)
        if not has_background_color:
            self.data['background_color'] = 'transparent'
            return

        self.data['background_color'] = ColorHelper.convert_color(
            DictionaryHelper.get(self.layer, 'backgroundColor', {}))

    def get_image(self):
        image = DictionaryHelper.get(self.layer, 'image', False)

        return image

    def get(self, name, default=None):
        return DictionaryHelper.get(self.data, name, default)

    @classmethod
    def name(cls):
        return "Element"

    def get_calculated_size(self):
        self.parent.get('x')

    def get_styles(self):
        return {

        }
