import requests
from telebot import types


def get_files_bytes(file_url):
    return requests.get(file_url).content



def __get_phone_number(message: types.Message) -> str:
    """Получаем номер телефона в зависимости от того, как его ввел пользователь."""
    phone_number = ""

    if message.contact:
        phone_number = message.contact.phone_number
    elif message.text:
        phone_number = message.text

    return phone_number