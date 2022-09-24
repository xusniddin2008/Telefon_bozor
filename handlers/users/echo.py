from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    #print(message.answer)
    #await bot.send_message(message.chat.id.1799255555, message.text)
    #await message.answer(message.text)
    pass
