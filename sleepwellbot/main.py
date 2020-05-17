import telebot
import logging
import time
import flask

app = flask.Flask("SleepWellBot")

API_TOKEN = "989082753:AAHTQctnhWRqUVtGo3f1kyKla8rC1S7d73Y"
# CHAT_ID = 325791759
HOST = '80.211.33.52'
PORT = 80
LISTEN = '0.0.0.0'
URL_BASE = f"https://{HOST}:{PORT}"
CHAT_ID = 325791759

bot = telebot.TeleBot(API_TOKEN)

@app.route('/test', methods=['GET'])
def test_hook():
    bot.send_message(CHAT_ID, "Test")
    return "Done"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    CHAT_ID = message.chat.id
    bot.reply_to(message, f"Now your this chat used for alarming. Chat id: {CHAT_ID}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

# bot.set_webhook(url=f"{URL_BASE}/")

app.run(host=LISTEN,
        port=PORT,
        debug=True)