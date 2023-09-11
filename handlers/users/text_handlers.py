from telebot import types

from data.loader import bot
from helpers import api
from keyboards.reply import services_menu, location_menu


@bot.message_handler(func=lambda msg: msg.text == 'Начать')
def start_processing_request(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Напишите заголовок для вашего запроса", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_title_process_description)


def get_title_process_description(message: types.Message):
    chat_id = message.chat.id
    title = message.text

    bot.send_message(chat_id, "Напишите содержание/описание вашего запроса")
    bot.register_next_step_handler(message, get_description_process_user_name, title)


def get_description_process_user_name(message: types.Message, title: str):
    chat_id = message.chat.id
    description = message.text

    bot.send_message(chat_id, "Напишите ваш username в телеграмме, в дальнейшем сервис сможет с вами связаться")
    bot.register_next_step_handler(message, get_username_process_hashtags, title, description)


def get_username_process_hashtags(message: types.Message, title: str, description: str):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     "Выберите одну из представленных ниже категорий услуг, хештеги будут автоматически добавлены",
                     reply_markup=services_menu())
    bot.register_next_step_handler(message, get_hashtags_process_location, title, description, message.text)


def get_hashtags_process_location(message: types.Message, title: str, description: str, username: str):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Нажмите на кнопку ниже чтобы мы смогли сохранить вашу локацию",
                     reply_markup=location_menu())

    bot.register_next_step_handler(message, collect_all_data, title, description, username, message.text)


def collect_all_data(message: types.Message, title, description, username, service):
    coordinates = f"{message.location.latitude}, {message.location.longitude}"
    service_id = api.get_service_id(service)
    chat_id = message.chat.id

    request_data = {
        "chat_id": chat_id,
        "title": title,
        "body": description,
        "username": username,
        "service": service_id['service_id'],
        "location": coordinates,
    }

    api.create_user_request(request_data)

    # print(title, description, username, service, coordinates)