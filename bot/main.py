from aiogram import executor
import logging
from bot.dispatcher import dp
from bot.handler import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)