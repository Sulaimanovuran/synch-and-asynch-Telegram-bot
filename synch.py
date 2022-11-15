import random

import telebot
from telebot import types

bot = telebot.TeleBot('Your telegrambot token')


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Hello, {message.from_user.full_name}!'
#     bot.send_message(message.chat.id, mess)


#
# #
# @bot.message_handler(content_types=['photo'])
# def start(message):
#     mess = f'Wow, {message.from_user.full_name}, great photo!'
#     bot.send_message(message.chat.id, mess)


#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.full_name}')


# @bot.message_handler(commands=['telegram'.lower()])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Перейти в группу', url='https://t.me/+IbSCffwmPsIzOWIy'))
#     bot.send_message(message.chat.id, f'{message.from_user.full_name} лови ссылку', reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton('/telegram')
#     photo = types.KeyboardButton('/photo')
#     start = types.KeyboardButton('/start')
#
#     markup.add(website, photo, start)
#     bot.send_message(message.chat.id, 'Commands 👇', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Курсы валют')
    item3 = types.KeyboardButton('Информация')
    item4 = types.KeyboardButton('Другое')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    # if message.text == 'private':
    if message.text == 'Рандомное число':
        bot.send_message(message.chat.id, f'Your number: {str(random.randint(0, 1000))}')
    elif message.text == 'Курсы валют':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('USD')
        item2 = types.KeyboardButton('EUR')
        item3 = types.KeyboardButton('... Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Курсы валют', reply_markup=markup)

    elif message.text == 'Информация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('О Боте')
        item2 = types.KeyboardButton('Что в коробке?')
        item3 = types.KeyboardButton('... Назад')
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Информация', reply_markup=markup)

    elif message.text == 'Другое':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Натройки')
        item2 = types.KeyboardButton('Подписка')
        item3 = types.KeyboardButton('Стикер')
        item4 = types.KeyboardButton('... Назад')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, 'Другое', reply_markup=markup)

    elif message.text == '... Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Рандомное число')
        item2 = types.KeyboardButton('Курсы валют')
        item3 = types.KeyboardButton('Информация')
        item4 = types.KeyboardButton('Другое')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=markup)

    elif message.text == 'Стикер':
        stick = open('/home/uran/Downloads/грин.jpg', 'rb')
        bot.send_photo(message.chat.id, stick)


bot.polling(none_stop=True)
