

import telebot

bot = telebot.TeleBot("5866280857:AAEH75kgK0bDZCoG-lh8-mbrsSV4xyjKews")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
