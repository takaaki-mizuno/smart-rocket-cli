from rocket.helpers import DictionaryHelper
from .element import Element


class Image(Element):

    def parse_specific_info(self):
        self.get_image()

    def get_image(self):
        path = DictionaryHelper.get(self.layer, 'image._ref')
        if path is not None:
            self.data['image_path'] = path
