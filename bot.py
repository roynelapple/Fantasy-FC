# coding: utf-8
import os
import telebot
from api import get_league, get_partials


bot = telebot.TeleBot(os.environ['8658774454:AAH-QF_YZT1MRfQJ0kMiXOzmn_kVuTRty0I'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hola Bienvenido a Football King Team!")


@bot.message_handler(commands=['liga'])
def send_league_data(message):
    bot.reply_to(message, get_league())


@bot.message_handler(commands=['parciais'])
def send_partials(message):
    bot.reply_to(message, get_partials())

bot.polling()
