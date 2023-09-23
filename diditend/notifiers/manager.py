import importlib
from .. import notifiers

class Manager:

    NOTIFIERS = [
            {"filename": "telegram.py", "class" :"TelegramNotifier"},
            ]

    def get_notifiers_clss():
        cls_lst = []
        for ntf_dct in Manager.NOTIFIERS:
            ntf_dct["filename"] = ntf_dct["filename"].replace(".py", "")
            notifier_module = importlib.import_module("diditend.notifiers.{}".format(ntf_dct["filename"]))
            notifier_cls = getattr(notifier_module, ntf_dct["class"])
            cls_lst.append(notifier_cls)

    def get_notifier(classname):
        for ntf_dct in Manager.NOTIFIERS:
            if ntf_dct["class"] == classname:
                ntf_dct["filename"] = ntf_dct["filename"].replace(".py", "")
                notifier_module = importlib.import_module("diditend.notifiers.{}".format(ntf_dct["filename"]))
                notifier_cls = getattr(notifier_module, ntf_dct["class"])
                return notifier_cls
