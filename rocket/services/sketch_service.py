from ..helpers import DictionaryHelper
from ..entities.archive.sketch import Button, Label, Image, View, TextEdit, Icon


class SketchService:

    @classmethod
    def parse_screen_elements(cls, element, archive, names: list):
        elements = []
        if 'layers' not in element.layer:
            return
        layers = element.layer['layers']
        if layers is None:
            return
        for layer in layers:
            element_object = cls.parse_element(layer, element, archive, names)
            if element_object is not None:
                children = cls.parse_screen_elements(element_object, archive, names)
                element_object.elements = children
                elements.append(element_object)

        return elements

    @classmethod
    def parse_element(cls, layer, parent, archive, names: list):
        object_id = DictionaryHelper.get(layer, 'do_objectID')

        if object_id is None:
            return None

        is_visible = DictionaryHelper.get(layer, 'isVisible', True)
        if not is_visible:
            return None

        name = DictionaryHelper.get(layer, 'name', '')
        _class = DictionaryHelper.get(layer, '_class', '')

        if name.startswith('BUTTON_'):
            element = Button(object_id, name[7:], layer, parent, archive, names)
        elif _class == 'text':
            element = Label(object_id, name, layer, parent, archive, names)
        elif _class == 'image':
            element = Image(object_id, name, layer, parent, archive, names)
        elif name.startswith('TEXTEDIT_'):
            element = TextEdit(object_id, name[9:], layer, parent, archive, names)
        elif name.startswith('ICON_'):
            element = Icon(object_id, name[5:], layer, parent, archive, names)
        elif name.startswith('VIEW_'):
            element = View(object_id, name[5:], layer, parent, archive, names)
        else:
            element = View(object_id, name, layer, parent, archive, names)

        return element
