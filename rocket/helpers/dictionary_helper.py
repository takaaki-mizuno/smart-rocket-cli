class DictionaryHelper:

    @classmethod
    def get(cls, dictionary, path, default=None):
        elements = path.split('.')
        item = dictionary
        for element in elements:
            if not isinstance(item, dict):
                return default
            if element in item:
                item = item[element]
            else:
                return default

        return item
