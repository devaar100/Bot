from flask import Flask , request
import os
import logging
import telegram
import requests

app = Flask(__name__)

bot = telegram.Bot(token='427815024:AAG_4OHSiublONg_bgZACbpkISrAouhUHSE')
botName = "Chiku_bot"

@app.route("/", methods=["POST", "GET"])
def setWebhook():
    if request.method == "GET":
        logging.info("Hello, Telegram!")
        print "Done"
        return "OK, Telegram Bot!"

@app.route("/verify", methods=["GET"])
def verification():
    if request.method == "GET":
        update = telegram.Update.de_json(request.get_json(force=True),bot)
        if update is None:
            return "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        handle_message(update.message)
        return "ok"


def handle_message(msg):
    text = msg.text
    print msg
    # An echo bot
    bot.sendMessage(chat_id=msg.chat.id, text=text)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

