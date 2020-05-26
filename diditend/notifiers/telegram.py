from .base import Notifier
from json import 
import requests

class TelegramNotifier(Notifier):

    def __init__(self):
        super().__init__()
        self.bot_chat_id = self.get_config('bot_chat_id')
        self.bot_token = self.get_config('bot_token')

    def send_to_my_service(message):
        send_text = "https://api.telegram.org/bot{token}/sendMessage?chat_id={bid}&parse_mode=Markdown&text={msg}"

        response = requests.get(send_text.format(token=self.bot_token, bid=self.bot_chat_id, msg=message))

        return response



