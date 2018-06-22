from .dictionary_helper import DictionaryHelper


class ColorHelper:

    @classmethod
    def convert_color(cls, color):
        if color is None:
            return 'transparent'

        red = DictionaryHelper.get(color, 'red', 1)
        blue = DictionaryHelper.get(color, 'blue', 1)
        green = DictionaryHelper.get(color, 'green', 1)
        alpha = DictionaryHelper.get(color, 'alpha', 1)

        if alpha == 1:
            return '#%02x%02x%02x' % (int(red * 255), int(green * 255), int(blue * 255))

        return '#%02x%02x%02x%02x' % (int(red * 255), int(green * 255), int(blue * 255), int(alpha * 255))
