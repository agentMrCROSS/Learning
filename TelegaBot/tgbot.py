# Импортирую все что потребуется
import telebot
from telebot import types
from config import TOKEN
from classes import APIException, Convertor

# PDEV-27 Павел Андреевич С.
"""Для того,чтобы всё заработало нужно скачать 3 файла - classes.py , config.py , ну и основной файл tgbot.py"""
"""В телеграмме в поиске вводите @AgentCrossBot - у него будет имя PabloEscobar. Общайтесь!"""

bot = telebot.TeleBot(TOKEN)  # Присваиваю боту свой токен
# Создаю словарь с доступными валютами и их значениями
valuta = {
    'Bitcoin': 'BTC',
    'Ethereum': 'ETH',
    'Arbitrum': 'ARB',
    'Tether': 'USDT',
    'Cardano': 'ADA',
    'XRP': 'XRP',
    'Dogecoin': 'DOGE',
    'SOLANA': 'SOL',
    'Доллар': 'USD'
}


@bot.message_handler(commands=['start'])  # Реализую команду /start и создаю кнопочку
def url(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Сайт,с которого берутся актуальные данные',
                                        url='https://www.cryptocompare.com/')
    markup.add(button)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт. /help для вызова помощи"
                                           " или /values для просмотра списка доступных валют", reply_markup=markup)


@bot.message_handler(commands=['help'])  # Реализую команду /help и кнопку
def starthelp(message: telebot.types.Message):
    text = 'Для конвертации валют вводи данные в формате Валюта Валюта Количество'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # Реализую команду /values
def values(message: telebot.types.Message):
    text = 'Валюты:'
    for key in valuta.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    base, quote, amount = message.text.split(' ')
    value = base, quote, amount
    try:
        if len(value) != 3:
            raise APIException('Неверное количество параметров!')
        answer = Convertor.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling(none_stop=True, interval=0)  # Чтобы бот всегда работал и не тупил
