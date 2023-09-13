import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = 'http://hisayapi.pythonanywhere.com/api/v1'


telegram_url = "https://api.telegram.org/file/bot{bot_token}/{file_path}"
