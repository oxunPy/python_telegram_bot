from telebot import types


class ReplyKeyboardMarkups:

    @staticmethod
    def helloMarkup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        return markup

    @staticmethod
    def requestContactTest():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btnContact = types.KeyboardButton("Contact1", request_contact=True)
        markup = markup.row(btnContact)
        btnContact2 = types.KeyboardButton("Contact2", request_contact=True)
        markup = markup.row(btnContact2)
        return markup

    @staticmethod
    def requestContact():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnContact = types.KeyboardButton("Отправьте свой контакт", request_contact=True)
        markup.add(btnContact)
        return markup

    @staticmethod
    def mainMenu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("button1")
        btn2 = types.KeyboardButton("button2")
        markup = markup.row(btn1, btn2)
        btn3 = types.KeyboardButton("button3")
        btn4 = types.KeyboardButton("button4")
        markup = markup.row(btn3, btn4)
        return markup
