from configparser import ConfigParser
import os
import json

class Config:
    def __init__(self, directory):
        #On parse le config.ini. On obtient un dictionnaire avec la valeur du fichier dialogflow_secret.json
        parser = ConfigParser()
        absolute_file_path = os.path.join(directory, 'config.ini')
        file_list = parser.read(absolute_file_path)
        if not file_list:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

        #On extrait la valeur du project_id du fichier dialogflow_secret.json et on l'associe à l'instance self.project_id
        absolute_file_path_dialogflow_secret = os.path.join(directory, self.__getattribute__('dialogflow_secret'))
        f = open(absolute_file_path_dialogflow_secret)
        data = json.load(f)
        self.project_id = data['project_id']

    def get(self, name):
        return self.__getattribute__(name)

config = Config(os.path.dirname(__file__))

