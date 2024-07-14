import telebot
import sqlite3
import random
from telebot import types

import os
from fuzzywuzzy import fuzz


# Создаем экземпляр бота
bot = telebot.TeleBot('7248391842:AAF5JAtGafgPG_aLeBozmJfNWK9rKP659VE')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start", 'help', 'info', 'msu'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text", 'document', 'audio'])
def handle_text(message):
    # # Если юзер прислал 1, выдаем ему случайный факт
    # if message.text.strip() == 'Факт':
    #     answer = random.choice(facts)
    # # Если юзер прислал 2, выдаем умную мысль
    # elif message.text.strip() == 'Поговорка':
    #     answer = random.choice(thinks)
    # # Отсылаем юзеру сообщение в его чат
    # bot.send_message(message.chat.id, answer)

    if message.text.rstrip() == 'info':


        attrs = dir(message.chat)
        txt = [f'HELLO {message.chat.username}\n'+'#'*10]
        txt.append('\nmessage.chat attributes\n')
        for attr in attrs:
            if (not attr.startswith('_')) and (not attr.endswith('_')):
                txt.append(f'{attr} : {getattr(message.chat, attr)}\n')
        txt.append('#'*10 + '\n')

        bot.send_message(message.chat.id, "".join(txt))
    else:
        pass
        # bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)