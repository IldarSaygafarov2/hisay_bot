from telebot import types


def new_tags_admin_action(tag, chat_id):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton(text="Удалить", callback_data=f'delete_{tag}_{chat_id}'),
        types.InlineKeyboardButton(text="Оставить", callback_data=f'save_{tag}_{chat_id}'),
    )
    return markup
