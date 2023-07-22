from abc import abstractmethod

from telebot import TeleBot
from telebot.types import Message


class BaseHandler:
    def __init__(self, message: Message, bot: TeleBot):
        self.message = message
        self.bot = bot

    @abstractmethod
    def handleMessage(self, message: Message):
        pass

