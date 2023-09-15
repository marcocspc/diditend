import argparse
from .notifiers.manager import Manager

class Parser():

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-m", "--message", help="Message to send to service.", action="store")
        self.parser.add_argument("-s", "--service", help="Service to use. Currently can be one of the following options: {}.".format(" ".join(Manager.NOTIFIERS)), action="store")
        self.parser.add_argument("-d", "--date", help="Send date together with message, if message is different from default one.", action="store_true")
        self.subparsers = self.parser.add_subparsers(help='commands', dest='command')
        self.list_cmd = self.subparsers.add_parser('list', help="List available notifiers.")
        self.args = self.parser.parse_args()
