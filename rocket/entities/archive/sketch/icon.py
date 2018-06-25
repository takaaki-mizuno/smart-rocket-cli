from .element import Element


class Icon(Element):

    def parse_specific_info(self):
        self.data['icon_name'] = 'None'
        self.data['icon_color'] = '#000000'

        self.set_content()

    @classmethod
    def type(cls):
        return "Icon"

    def set_content(self):
        pass

    def get_icon_name(self) -> str:
        return self.data['icon_name']

    def get_icon_color(self) -> str:
        return self.data['icon_color']

    def generate_react_native_component(self):
        return """
<Icon
    size={size}
    name="%s"
    color="%s"/>
        """ % (self.get_icon_name(), self.get_icon_color())

    def component_name(self):
        return self.name
