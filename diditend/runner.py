from .notifiers.manager import Manager
from .parser import Parser 
from .util.prompt import Functions
import datetime

def main():
    parser = Parser()
    service = None 
    message = None 

    if parser.args.service is None:
        service = "TelegramNotifier"
    else:
        service = parser.args.service

    if parser.args.command is not None:
        if parser.args.command == "list":
            lst = [notifr["class"] for notifr in Manager.NOTIFIERS]
            print("The following notifiers are available: {}.".format(" ".join(lst)))
            exit(0)

        if parser.args.command == "mkconfig":
            Functions.create_config_prompt()
            exit(0)

    if parser.args.message is None:
        message = "Your terminal job has finished! Current time: {}".format(datetime.datetime.now())
    else:
        message = parser.args.message

    if parser.args.date is not None and parser.args.message is not None:
        message += " [Time this notification was generated: {}]".format(datetime.datetime.now())

    notifier_cls = Manager.get_notifier(service)
    notifier = notifier_cls()
    notifier.send_message(message)

    #parser.parser.print_help()
