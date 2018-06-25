from .element import Element


class Header(Element):

    def parse_specific_info(self):
        self.data['title_text'] = ''
        self.data['left_button'] = None
        self.data['right_button'] = None

        self.set_content()

    def set_content(self):
        pass

    @classmethod
    def type(cls):
        return "Header"

    def generate_react_native_component(self):
        return ""

    def component_name(self):
        return self.name
