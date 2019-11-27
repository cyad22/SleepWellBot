import telebot

bot = telebot.TeleBot("989082753:AAHYNJHhBQqMqjoXAMerC0g-_BfAYziLtAY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id)
    bot.send_message(message, message.text)

bot.polling()
