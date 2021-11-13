from aiogram import Bot, Dispatcher
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
