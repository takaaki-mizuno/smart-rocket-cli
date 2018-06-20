from rocket.entities.archive import Directory


class ArchiveService:

    @classmethod
    def extract(cls, path):
        directory = Directory(path)
        directory.extract()

        return directory
