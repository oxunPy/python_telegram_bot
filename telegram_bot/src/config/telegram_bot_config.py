from config import TOKEN, BOTNAME
from telebot import TeleBot
from telegram_bot.src.handler.update_handler import UpdateHandler

bot = TeleBot(TOKEN)

class MyTelegramBotConfig:
    def __init__(self, updateHandler: UpdateHandler = None):
        self.updateHandler = updateHandler
        updateHandler.handleMessage(updateHandler.message)


@bot.message_handler(commands = ['start'])
def start(message):
    MyTelegramBotConfig(UpdateHandler(message, bot))

@bot.message_handler(content_types = ['text'])
def text_messages(message):
    MyTelegramBotConfig(UpdateHandler(message, bot))

@bot.message_handler(content_types = ['contact'])
def contact(message):
    MyTelegramBotConfig(UpdateHandler(message, bot))

def main():
    bot.polling(none_stop = True, interval = 0)  # обязательная для работы бота часть


if __name__ == '__main__':
    main()
