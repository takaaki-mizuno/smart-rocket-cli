import fire
from rocket.commands import ReactNative

__version__ = '0.0.1'


def main():
    fire.Fire(Pipeline)


class Pipeline(object):

    def __init__(self):
        self.react_native = ReactNative()
