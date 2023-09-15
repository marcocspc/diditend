import importlib
import sys
import inspect
from ..notifiers.manager import Manager

class Functions():

    def create_config_prompt():
        print("Please choose one of the following:")

        for i in range(len(Manager.NOTIFIERS)):
            print("{} - {}".format(i+1, Manager.NOTIFIERS[i]["class"]))

        print("0 - Cancel.")
        print()
        option = Functions.get_int_input("Input your number: ", 0)

        if option == 0:
            print("Bye!")
        else:
            ntf_dct = Manager.NOTIFIERS[option - 1]
            ntf_dct["filename"] = ntf_dct["filename"].replace(".py", "")
            notifier_module = importlib.import_module("diditend.notifiers.{}".format(ntf_dct["filename"]))
            notifier_cls = getattr(notifier_module, ntf_dct["class"])
            notifier = notifier_cls()
            for entry in notifier.get_config_entries():
                option = Functions.get_string_input("Insert a value for {}: ".format(entry), "")
                if option == "":
                    print("Your input must not be empty!")
                    exit(0)
                else:
                    notifier.set_config(entry, option)
            
            notifier.save_config()
            print("Done.")
                

    def get_int_input(message, default_value):
        try:
            return int(input(message + " [Default " + str(default_value) + "] "))
        except ValueError:
            return default_value

    def get_string_input(message, default_value):
        try:
            string = str(input(message + " [Default " + str(default_value) + "] "))
            return string if string != "" else default_value
        except ValueError:
            return default_value

