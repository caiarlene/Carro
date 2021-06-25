import configparser
import os.path

class ReadConfig:
    config = ''
    def __init__(self):
        self.config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd()) + '/Carro/config/config.ini'

        self.config.read(file_path)

    def getConfigValue(self,section,key):
        value = self.config.get(section, key)
        return value