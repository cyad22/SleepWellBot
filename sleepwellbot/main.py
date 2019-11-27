import telebot

myChatID = "325791759"
bot = telebot.TeleBot("989082753:AAHYNJHhBQqMqjoXAMerC0g-_BfAYziLtAY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id)
    bot.reply_to(message.chat.id, message.text)

for i in range(10):
    bot.send_message(myChatID, "Hello")

bot.polling()
