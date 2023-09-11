from telebot import types

from data.loader import bot
from helpers import api
from keyboards.reply import start_menu, start_request_kb


@bot.message_handler(commands=['start'])
def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    service_ids = api.get_service_profiles_ids()
    simple_users_ids = api.get_simple_users_profiles_ids()

    if chat_id in service_ids["service_profiles"]:
        bot.send_message(chat_id, "Здравствуйте владелец сервиса")
        return
    if chat_id in simple_users_ids["simple_users"]:
        bot.send_message(chat_id, "Здравствуйте обычный пользователь")
        bot.send_message(chat_id, """
Напишите вашу заявку в представленном ниже виде.

Пример заявки:

Заголовок: <i>Ваш заголовок</i>
Содержание/описание: <i>Ваше содержание/описание</i>
user_name пользователя: <i>Ваш user_name в телеграмме</i>
Хештеги: <i>Ваши хештеги</i>
Геолокация
""", parse_mode="HTML", reply_markup=start_request_kb())
        return

    if chat_id not in service_ids["service_profiles"] or chat_id not in simple_users_ids["simple_users"]:
        bot.send_message(chat_id, f"Приветствую тебя, {first_name}. Чтобы начать использовать бот, пройди регистрацию",
                         reply_markup=start_menu())
