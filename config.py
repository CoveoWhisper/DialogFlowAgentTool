from configparser import ConfigParser
import os
import json

class Config:
    def __init__(self, directory):
        #We parse the config.ini file. We get a dictionnary with dialogflow_secret.json as value.
        parser = ConfigParser()
        absolute_file_path = os.path.join(directory, 'config.ini')
        file_list = parser.read(absolute_file_path)
        if not file_list:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

        #We extract the project_id from the dialogflow_secret.json file and we associate it to self.project_id.
        absolute_file_path_dialogflow_secret = os.path.join(directory, self.__getattribute__('dialogflow_secret'))
        f = open(absolute_file_path_dialogflow_secret)
        data = json.load(f)
        self.project_id = data['project_id']

    def get(self, name):
        return self.__getattribute__(name)

config = Config(os.path.dirname(__file__))

