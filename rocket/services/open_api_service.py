from prance import BaseParser
from rocket.entities.api import Specification


class OpenApiService:
    @classmethod
    def parse(cls, path):
        try:
            parser = BaseParser(path)
        except Exception as e:
            raise e

        spec = Specification(parser.specification)

        return spec
