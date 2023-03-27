import telebot
import requests


def generate_response(message):

    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer OPENAI_API_KEY"}

    data = {
        "prompt": f"{message}",
        "temperature": 0.7,
        "max_tokens": 60
    }


    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["text"]

# 2й блок
TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.reply_to(message, "Hello! I am a bot and I can chat with you.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    bot.reply_to(message, "Sorry, I didn't understand your request.")


bot.polling()

# 3й блок


def echo_all(message):
    response = generate_response(message.text)


bot.reply_to(message, response)
