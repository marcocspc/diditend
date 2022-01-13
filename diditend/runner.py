from .notifiers.telegram import TelegramNotifier 
from .notifiers.manager import Manager
from .parser import Parser 
import datetime

def main():
    parser = Parser()
    service = None 
    message = None 

    if parser.args.service is None:
        service = "Telegram"
    else:
        service = parser.args.service

    if parser.args.command is not None:
        if parser.args.command == "list":
            print("The following notifiers are available: {}.".format(" ".join(Manager.__NOTIFIERS)))


    if parser.args.message is None:
        message = "Your terminal job has finished! Current time: {}".format(datetime.datetime.now())
    else:
        message = parser.args.message

    if parser.args.show_date and parser.args.message is not None:
        message += " [Time this notification was generated at: {}]".format(datetime.datetime.now())

    if service == "Telegram":
        notifier = TelegramNotifier()
        notifier.send_message(message)
