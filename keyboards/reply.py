from telebot import types
from helpers import api


def start_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    kb.add(*[
        types.KeyboardButton(text="Пользователь"),
        types.KeyboardButton(text="Сервис"),
    ])
    return kb


def phone_number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    )
    return kb


def services_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    services = api.get_services()
    buttons = [
        types.KeyboardButton(text=service['name'])
        for service in services
    ]
    kb.add(*buttons)
    return kb


def start_request_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        types.KeyboardButton(text="Начать")
    )
    return kb


def continue_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        types.KeyboardButton(text="Не добавлять"),
        types.KeyboardButton(text="Добавить"),
    )
    return kb


def location_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        types.KeyboardButton(text="Отправить локацию", request_location=True)
    )
    return kb


def simple_user_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.row(
        types.KeyboardButton('Оставить заявку'),
        types.KeyboardButton('Мои заявки'),
    )
    return kb
