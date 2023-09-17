import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = 'http://hisayapi.pythonanywhere.com/api/v1'
BASE_URL2 = 'http://127.0.0.1:8000'


telegram_url = "https://api.telegram.org/file/bot{bot_token}/{file_path}"
