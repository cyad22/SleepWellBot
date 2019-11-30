import telebot
import logging
import time
import flask

app = flask.Flask("SleepWellBot")

API_TOKEN = "989082753:AAHYNJHhBQqMqjoXAMerC0g-_BfAYziLtAY"
CHAT_ID = 325791759
HOST = '80.211.33.52'
PORT = 80
LISTEN = '0.0.0.0'
URL_BASE = f"https://{HOST}:{PORT}"

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

@app.route('/', methods=['GET', 'HEAD'])
def webhook():
    data = flask.request.query_string
    bot.process_new_updates([data])
    return data

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    CHAT_ID = message.chat.id
    bot.reply_to(message, f"Now your this chat used for alarming. Chat id: {CHAT_ID}")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     print(message.chat.id)
#     bot.reply_to(message.chat.id, message.text)

bot.remove_webhook()

time.sleep(0.1)

bot.set_webhook(url=f"{URL_BASE}/")

app.run(host=HOST,
        port=PORT,
        debug=True)