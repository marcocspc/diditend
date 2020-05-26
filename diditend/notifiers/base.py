import json
import os

class Notifier():

    def __init__(self):
        with open(os.path.expanduser("~") + os.path.sep + ".diditend.json") as cfg_json:
            self.config = json.load(cfg_json)

    def get_config(cfg_str):
        return self.config[self.class.__name__][cfg_str]

    def send_message(self, message):
        self.send_to_my_service(message)
