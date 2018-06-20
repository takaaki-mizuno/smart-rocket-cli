class StringHelper:

    @classmethod
    def endswith(cls, target, suffix):
        if target.endswith(cls.upper_first(suffix)):
            return True

        if target == suffix.lower():
            return True

        return False

    @classmethod
    def upper_first(cls, target):
        return target[0].upper() + target[1:]
