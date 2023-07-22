from telebot import TeleBot
from telebot.types import Message

from telegram_bot.src.handler.base.base_handler import BaseHandler
from telegram_bot.src.markup.reply_keyboard_markups import ReplyKeyboardMarkups


class MessageHandler(BaseHandler):

    def __init__(self, chatId, message: Message, bot: TeleBot):
        super().__init__(message, bot)
        self.chatId = chatId

    def handleMessage(self, message):

        if self.message.text == '/start':
            self.bot.send_message(chat_id = self.chatId, text = "Ваш телефон нужен", reply_markup = ReplyKeyboardMarkups.requestContact())

        if self.message.text == 'oxun':
            self.bot.send_message(chat_id = self.chatId, text = "HI, MY NAME IS OXUNJON")

        if self.message.text == 'sherzod':
            self.bot.send_message(chat_id = self.chatId, text = 'HI, MY NAME IS SHERZOD')

        if self.message.text == 'button1':
            self.bot.send_message(chat_id = self.chatId, text = "Отправьте ваше имя")