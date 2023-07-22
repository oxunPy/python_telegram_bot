from telebot import TeleBot
from telebot.types import Message

from telegram_bot.src.handler.base.base_handler import BaseHandler
from telegram_bot.src.handler.contact_handler import ContactHandler
from telegram_bot.src.handler.message_handler import MessageHandler


class UpdateHandler(BaseHandler):
    def __init__(self, message: Message, bot: TeleBot):
        super().__init__(message, bot)
        self.messageHandler = MessageHandler(message.from_user.id, message, bot)
        self.contactHandler = ContactHandler(message.from_user.id, message, bot)
    def handleMessage(self, message: Message):
        if message.content_type == 'text':
            self.messageHandler.handleMessage(message)
        elif message.content_type == 'contact':
            self.contactHandler.handleMessage(message)

# bot.send_message(message.from_user.id, "Assalomu alaykum!",
#                       reply_markup=ReplyKeyboardMarkups.helloMarkup())

# self.bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра",
#                  reply_markup=InlineKeyboardMarkups.helloMarkup())
