from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram import Bot
import os

load_dotenv()
storage = MemoryStorage()

ABSOLUTE_PATH = os.getenv('ABSOLUTE_PATH')
TOKEN = os.getenv('TOKEN_API')

bot = Bot(token=TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot, storage=storage)
