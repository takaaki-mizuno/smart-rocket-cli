import random
import string


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

    @classmethod
    def random_string(cls, length: int) -> str:
        char_set = string.ascii_uppercase + string.digits
        return ''.join(random.sample(char_set*length, length))
