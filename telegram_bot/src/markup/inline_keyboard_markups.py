from telebot import types

class InlineKeyboardMarkups:

    @staticmethod
    def helloMarkup():
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
        markup.add(btn1)
        return markup