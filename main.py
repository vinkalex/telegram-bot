import telebot
from requests import get
from bs4 import BeautifulSoup

TOKEN = "5093490971:AAExcTTTEmxPmRRRbrsFIdwm4oHmVtjuT70"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Я Film_Online бот, какой фильм хочешь посмотреть?")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет! Какой фильм ты хочешь посмотреть? (напиши в таком формате: фильм <название>")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        film = message.text
        s = "http://google.ru/search?q=" + film + "смотреть онлайн"
        result = get(s)
        c = result.text
        soup = BeautifulSoup(c, 'html.parser')
        for link in soup.findAll('a'):
            string = str(link.get('href'))
            if string.find('kinopoisk') > 0:
                bot.send_message(message.from_user.id, string)
                print(link.get('href'))
                break

bot.polling()
