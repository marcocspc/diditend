from .. import notifiers
import inspect

class Manager:

    NOTIFIERS = [
            {"filename": "telegram.py", "class" :"TelegramNotifier"},
            ]
