import telebot
from requests import get
from bs4 import BeautifulSoup

TOKEN = "625226017:AAGhQfpa-Nqeo7BCH1rkApp09BygMaRfEys"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, какой фильм ты хочешь посмотреть? (напиши в таком формате: фильм <название>")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        film = message.text
        s = "http://google.ru/search?q=" + film + "watchonline"
        result = get(s)
        c = result.text
        soup = BeautifulSoup(c, 'lxml')
        for h in soup.findAll('h3', attrs={"class": 'r'}):
            link = h.find('a')
            link["href"] = "http://www.google.ru" + link['href']
            bot.send_message(message.from_user.id, str(link))
            break


bot.polling()