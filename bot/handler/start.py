from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.dispatcher import dp


@dp.message_handler(commands = "start")
async def start_handler(msg:types.Message,state:FSMContext):
    await msg.answer("salom")
    await state.set_state("clear")
