class Reference:

    def __init__(self, path):
        self.fullpath = path
        self.name = ""
        self.type = ""

        self.parse()

    def parse(self):
        elements = self.fullpath.split('/')

        if elements[0] == "#":
            if len(elements) > 1:
                self.type = elements[1]
            self.name = elements[-1]
