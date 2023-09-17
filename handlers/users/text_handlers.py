from telebot import types

from data.loader import bot
from helpers import api
from keyboards.reply import services_menu, location_menu, continue_kb, start_menu
from .commands import command_start


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
    bot.register_next_step_handler(message, process_new_hashtags, title, description, message.text)


def process_new_hashtags(message: types.Message, title, description, username):
    chat_id = message.chat.id
    service_id = api.get_service_id(message.text)
    hashtags = api.get_hashtags_by_service(service_id['service_id'])
    str_hashtags = ', '.join(hashtags['hashtags'])
    msg = f"""
Выбранная вами услуга: <b>{message.text}</b>

Теги для услуг, которые вы предоставляете:
{str_hashtags}

Если вы хотите добавить новые хештеги нажмите на кнопку 'Добавить'.
Если нет, то на кнопку 'Не добавлять' и мы присвоим вашей услуге уже готовые хештеги, что представлены выше
    """

    bot.send_message(chat_id, msg, reply_markup=continue_kb(), parse_mode="HTML")
    bot.register_next_step_handler(message, get_service_process_tags, title, description, username, service_id)


@bot.message_handler(func=lambda msg: msg.text in ('Не добавлять', 'Добавить'))
def get_service_process_tags(message: types.Message, title, description, username, service_id):
    chat_id = message.chat.id
    if message.text == 'Не добавлять':
        bot.send_message(chat_id, "Нажмите на кнопку ниже чтобы мы смогли сохранить вашу локацию",
                         reply_markup=location_menu())
        bot.register_next_step_handler(message, collect_all_data, title, description, username, service_id)
    elif message.text == 'Добавить':
        bot.send_message(chat_id, """
Вы можете написать ваши хештеги и мы присвоим их для данной услуги.
Пример: '#tag, #tag2, #tag3'
""", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, generate_new_tags, title, description, username, service_id)


def generate_new_tags(message: types.Message, title, description, username, service_id):
    chat_id = message.chat.id
    tags = [tag.strip() for tag in message.text.split(',')]
    api.add_hashtags_to_service(service_id=service_id['service_id'], tags_list=tags)
    bot.send_message(chat_id, "Нажмите на кнопку ниже чтобы мы смогли сохранить вашу локацию",
                     reply_markup=location_menu())
    bot.register_next_step_handler(message, collect_all_data, title, description, username, service_id)


def collect_all_data(message: types.Message, title, description, username, service):
    coordinates = f"{message.location.latitude}, {message.location.longitude}"
    chat_id = message.chat.id

    request_data = {
        "chat_id": chat_id,
        "title": title,
        "body": description,
        "username": username,
        "service": service['service_id'],
        "location": coordinates,
    }

    api.create_user_request(request_data)
    bot.send_message(chat_id, "Заявка отправлена, ожидайте, скоро вам ответят")
    command_start(message)

