import json
from rocket.helpers import DictionaryHelper, ColorHelper
from rocket.services import SketchService
from .screen import Screen
from collections import OrderedDict


class Sketch:

    def __init__(self, directory):
        self.directory = directory
        self.screens = {}
        self.parse_screens()

    def parse_screens(self):
        meta = json.loads(self.directory.get_real_path_content('meta.json'), object_pairs_hook=OrderedDict)
        for page_id, page_info in meta['pagesAndArtboards'].items():
            page = json.loads(self.directory.get_real_path_content('pages/' + page_id + '.json'),
                              object_pairs_hook=OrderedDict)
            if 'artboards' in page_info:
                for artboard_id, artboard_info in page_info['artboards'].items():
                    name = DictionaryHelper.get(artboard_info, 'name', '')
                    if name.startswith('SCREEN_'):
                        artboard = self._find_object_id(DictionaryHelper.get(page, 'layers', []), artboard_id)
                        if artboard is not None:
                            screen = Screen(artboard_id, name[7:], artboard, None, self.directory)
                            screen.elements = SketchService.parse_screen_elements(screen, self.directory)
                            self.screens[name[7:]] = screen

    def _find_object_id(self, layers, target_object_id):
        for layer in layers:
            _class = DictionaryHelper.get(layer, '_class', '')
            object_id = DictionaryHelper.get(layer, 'do_objectID', '')
            if object_id == target_object_id:
                return layer
            else:
                children = DictionaryHelper.get(layer, 'layers', '')
                if children is not None:
                    result = self._find_object_id(children, target_object_id)
                    if result is not None:
                        return result

        return None

    def get_screen(self, name):
        if name in self.screens:
            return self.screens[name]

        return None
