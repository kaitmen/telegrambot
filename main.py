import telebot

import settings
from extensions import APIException, Exchanger

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, settings.START_MSG)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.reply_to(message, settings.VALUES_MSG)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    parameters = message.text.split(' ')
    try:
        result = Exchanger.get_price(*parameters)
    except APIException as e:
        bot.reply_to(message, f"Хм... Ты допустил ошибку в команде:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Ой, у меня тут ошибка... Напиши разработчикам:\n{e}")
    else:
        bot.reply_to(message, result)


bot.polling()
