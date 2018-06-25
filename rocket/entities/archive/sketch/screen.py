from .element import Element
import stringcase


class Screen(Element):

    @classmethod
    def type(cls):
        return "Screen"

    def get_locale_name(self):
        return stringcase.snakecase(self.name)
