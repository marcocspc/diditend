import argparse

class Parser():

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-m", "--message", help="Message to send to service.", action="store")
        self.parser.add_argument("-s", "--service", help="Service to use. Currently can be one of the following options: Telegram.", action="store")
        self.parser.add_argument("-d", "--show-date", help="Send date together with message, if message is different from default one.", action="store_true")
        self.args = self.parser.parse_args()
