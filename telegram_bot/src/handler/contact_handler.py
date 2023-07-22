from telebot import TeleBot
from telebot.types import Message

from telegram_bot.src.handler.base.base_handler import BaseHandler
from telegram_bot.src.markup.reply_keyboard_markups import ReplyKeyboardMarkups
from telegram_bot.src.service.contact_service import ContactService


class ContactHandler(BaseHandler):

    def __init__(self, chatId: int, message: Message, bot: TeleBot):
        super().__init__(message, bot)
        self.chatId = chatId
        self.contactService = ContactService()

    def handleMessage(self, message):
        # save contact
        contactIsSaved = self.contactService.saveContact(message.contact)

        if contactIsSaved:
            self.bot.send_message(chat_id = self.chatId, text = "Main menu", reply_markup = ReplyKeyboardMarkups.mainMenu())