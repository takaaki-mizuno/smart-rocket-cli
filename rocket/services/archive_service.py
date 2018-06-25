from rocket.entities.archive import Archive


class ArchiveService:

    @classmethod
    def extract(cls, path):
        archive = Archive(path)
        archive.extract()

        return archive
