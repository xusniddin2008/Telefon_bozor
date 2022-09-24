from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuLanguageKeyboard import menuLanguage

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message): 
    #await message.delete()    
    #await message.answer("<b>Telefon bozori yordamchi botiga hush kelibsiz</b>")
    #await message.answer("<b>Вас приветствует bot канала Telefon bozori</b>", reply_markup=menuLanguage)
    
    pass
