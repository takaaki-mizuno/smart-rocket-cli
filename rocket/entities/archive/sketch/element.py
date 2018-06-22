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
        self.get_style()
        self.get_image()
        self.parse_specific_info()

    def parse_specific_info(self):
        pass

    def get_style(self):
        style = DictionaryHelper.get(self.layer, 'style', 0)
        borders = DictionaryHelper.get(style, 'borders', [])
        for border in borders:
            if not DictionaryHelper.get(border, 'isEnabled', False):
                continue
            self.data['border_width'] = DictionaryHelper.get(border, 'thickness', 1)
            self.data['border_color'] = ColorHelper.convert_color(DictionaryHelper.get(border, 'color', None))

        fills = DictionaryHelper.get(style, 'fills', [])
        for fill in fills:
            if not DictionaryHelper.get(fill, 'isEnabled', False):
                continue
            self.data['background_color'] = ColorHelper.convert_color(DictionaryHelper.get(fill, 'color', None))

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
    def type(cls):
        return "Element"

    def get_calculated_sizes(self):
        sizes = {
            'width': self.get('width', 0),
            'height': self.get('height', 0),
            'y': self.get('y', 0) - self.parent.get('y', 0) if self.parent is not None else self.get('y', 0),
            'x': self.get('x', 0) - self.parent.get('x', 0) if self.parent is not None else self.get('y', 0),
            'paddingTop': 0,
            'paddingBottom': 0,
            'paddingLeft': 0,
            'paddingRight': 0
        }
        if self.parent is not None:
            margin = self.parent.get('width', 0) - self.get('width', 0)
            left = self.get('x', 0) - self.parent.get('x', 0)
            if abs(margin / 2 - left) < 2:
                sizes['width'] = "DeviceHelper.getScreenWidth() - %d" % margin
                sizes['paddingLeft'] = int(margin / 2)
                sizes['paddingRight'] = int(margin / 2)

        return sizes

    def get_styles(self):
        styles = self.get_calculated_sizes()

        if 'background_color' in self.data:
            styles['backgroundColor'] = self.data['background_color']
        if 'border_color' in self.data:
            styles['borderColor'] = self.data['border_color']
            styles['borderStyle'] = self.data['solid']
            styles['borderWidth'] = DictionaryHelper.get(self.data, 'border_width', 0)

        return styles

    def generate_react_native_component(self):
        if self.elements is None or len(self.elements) == 0:
            return '<View style={styles.%s}/>' % self.name

        children = []
        for element in self.elements:
            children.append(element.generate_react_native_component())

        return """
<View style={styles.%s}>
%s
</View>
        """ % (self.name, "\n".join(children))

    def generate_react_native_styles(self):
        styles = self.get_styles()
        style_content = ""
        for key, value in styles.items():
            style_content = style_content + '%s: %s,\n' % (key, value)

        style_data = """
%s: {
%s
},
        """ % (self.name, style_content)

        if self.elements is not None and len(self.elements) > 0:
            for element in self.elements:
                style_data = style_data + element.generate_react_native_styles()

        return style_data
