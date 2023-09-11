from telebot import TeleBot

from . import config

bot = TeleBot(token=config.BOT_TOKEN)
