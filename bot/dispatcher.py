from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

TOKEN =os.environ["Token"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot,storage=MemoryStorage())
