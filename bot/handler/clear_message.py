from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.dispatcher import dp


@dp.message_handler(state="clear")
async def message_clear_handler(msg:types.Message,state=FSMContext):
    unli = "aeiou"
    count = 0
    check = msg.text
    if msg.text.isalpha():
        for i in check:
            if i in unli:
                count+=1
        if count > 5:
            await msg.answer(f"{msg.text} Bu so`zda 5tadan ko`p unli harf bo`lganligi uchun ochirib tashlandi ")
            await msg.delete()
    else:
        await msg.answer("Siz so`z kiritmadingiz")

