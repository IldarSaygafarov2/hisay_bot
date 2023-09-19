from telebot import types

from data.loader import bot
from data.config import CHANNEL_ID


@bot.callback_query_handler(func=lambda call: 'delete' in call.data)
def get_tag_for_deletion_from_channel(call: types.CallbackQuery):

    _, tag, chat_id = call.data.split('_')


    bot.send_message(chat_id, 'Теги проходят модерацию, это займет несколько минут')


    # print(call)
    # print(call.data)
    # print(call.message)
