class Parameter:

    def __init__(self, definition):
        self.definition = definition
        self.name = ""
        self.type = ""
        self.place = ""
        self.required = False

        self.parse()

    def parse(self):
        self.name = self.definition['name'] if 'name' in self.definition else ''
        self.type = self.definition['type'] if 'type' in self.definition else ''
        self.place = self.definition['in'] if 'in' in self.definition else ''
        self.required = True if 'required' in self.definition and self.definition['required'] == 'true' else False
