import telebot
import  requests
import time
from threading import Thread
from telebot import types
import Parser

# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

token = "822697899:AAFIN-iJ6dMFHcHKMkYjJeLSo8scXmA0elc"
bot = telebot.TeleBot(token=token)

users = []
doc = []
notes = []



@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id

    bot.send_message(user, "Привет!Я бот ЦИАН, какую квартиру ты хочешь найти?",)

@bot.message_handler(commands=['spam'])
def add_user(message):
    global user
    user_id = message.chat.id
    if user_id not in notes:
        bot.send_message(user_id, "Вы мне еще не писали.")
    else:
        bot.send_message(user_id, notes[user_id])

@bot.message_handler(commands=['flats'])
def add_doc(message):
    global doc
    #doc = message.chat.id
    bot.send_message('Вот что я нашел ' ,doc)



@bot.message_handler(commands=['stop'])
def remove_user(message):
    user = message.chat.id
    users.remove(user)
    bot.send_message(user, "Все, все.")

def spam():
    global users
    while True:
        for user in users:
            bot.send_message(user, "Тут появилось кое-что новенькое!")
        time.sleep(3600)

@bot.message_handler(commands=['help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Чтобы найти квартиру вам нужно ввести команду /flat, чтобы я тебя запомнил -- /start, чтобы прекратить общение -- /stop")



def polling():
    bot.polling(none_stop=True)

polling_thread = Thread(target=polling)
spam_thread = Thread(target=spam)

polling_thread.start()
spam_thread.start()
