import json
import os
from .manager import Manager

class Notifier():

    def __init__(self):
        self.config_file_path = os.path.expanduser("~") + os.path.sep + ".diditend.json"
        if os.path.exists(self.config_file_path): 
            with open(self.config_file_path, "r") as cfg_json:
                self.config = json.load(cfg_json)
        else:
            self.config = {}
            self.config[self.__class__.__name__] = {}
            self.save_config()

        self.create_needed_config_entries()
        Manager.register(self.__class__.__name__)

    def create_config(self, cfg_str):
        if not cfg_str in self.config[self.__class__.__name__].keys():
            self.config[self.__class__.__name__][cfg_str] = ""
            self.save_config()

    def get_config(self, cfg_str):
        if not cfg_str in self.config[self.__class__.__name__].keys() or self.config[self.__class__.__name__][cfg_str] == "":
            raise KeyError("Config " + cfg_str + " not set in config file.")
        else:
            return self.config[self.__class__.__name__][cfg_str]
        return 

    def send_message(self, message):
        self.send_to_my_service(message)

    def save_config(self):
        with open(self.config_file_path, 'w+') as cfg_json:
            json.dump(self.config, cfg_json)
            cfg_json.close()

