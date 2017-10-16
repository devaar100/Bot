from flask import Flask , request
from flask_mail import Mail , Message
import os
import logging
import telegram

app = Flask(__name__)

bot = telegram.Bot(token='427815024:AAG_4OHSiublONg_bgZACbpkISrAouhUHSE')
botName = "Chiku_bot"

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'aarnavjindal1000@gmail.com',
	MAIL_PASSWORD = 'xbvpudzlderrcauq'
	)

mail = Mail(app)

@app.route("/")
def setWebhook():
    logging.info("Hello, Telegram!")
    print("Done")
    return "Hi from telebot"

@app.route("/mail/<name>", methods=['GET'])
def send_mail(name):
    msg = Message('Hello', sender='aarnavjindal1000@gmail.com', recipients=[name])
    msg.body = "Sent from server automatically"
    mail.send(msg)
    return "Mail sent"

@app.route("/verify", methods=["POST"])
def verification():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True),bot)
        if update is None:
            return "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        handle_message(update.message)
        return "ok"


def handle_message(msg):
    text = msg.text
    print(msg)
    # An echo bot
    bot.sendMessage(chat_id=msg.chat.id, text=text)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

