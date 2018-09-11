from configparser import ConfigParser
import os


class Config:
    def __init__(self, directory):
        parser = ConfigParser()
        absolute_file_path = os.path.join(directory, 'config.ini')
        file_list = parser.read(absolute_file_path)
        if not file_list:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

    def get(self, name):
        return self.__getattribute__(name)


config = Config(os.path.dirname(__file__))

