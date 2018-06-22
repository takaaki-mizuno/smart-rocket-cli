import json
from .screen import Screen


class Page:

    def __init__(self, page_id, artboards, directory):
        self.directory = directory
        self.artboards = artboards
        self.page_id = page_id
        self.json = None
        self.screens = []

        self.parse()

    def find_layer_by_id(self, object_id):
        return self._find_layer_by_id(self.json['layers'], object_id)

    def _find_layer_by_id(self, layers, object_id):
        for layer in layers:
            if layer['do_objectID'] == object_id:
                return layer
            if 'layers' in layer:
                result = self._find_layer_by_id(layer['layers'], object_id)
                if result is not None:
                    return result

        return None

    def parse(self):
        self.json = json.loads(
            self.directory.get_real_path_content('pages/' + self.page_id + '.json'),
            object_pairs_hook=True
        )
        for artboard_id, artboard_info in self.artboards.items():
            if artboard_info['name'].startswith('SCREEN_'):
                layer = self.find_layer_by_id(artboard_id)
                self.screens.append(Screen(artboard_id, artboard_info['name'][7:], layer, self.directory))

    @classmethod
    def type(cls):
        return "Page"
