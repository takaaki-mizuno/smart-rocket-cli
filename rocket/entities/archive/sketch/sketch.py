import json

class Sketch:

    def __init__(self, directory):
        self.directory = directory
        self.pages = []

    def parse_screens(self):
        meta = json.loads(self.directory.get_real_path_content('meta.json'), object_pairs_hook=True)
        for page_id, page_info in meta['pagesAndArtboards'].items():
            page = json.loads(self.directory.get_real_path_content('pages/' + page_id +'.json'), object_pairs_hook=True)
            if 'artboards' in page_info:
                for artboard_id, artboard_info in page_info['artboards'].items():


