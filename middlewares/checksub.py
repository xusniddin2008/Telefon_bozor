import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from keyboards.default.menuLanguageKeyboard import menuLanguage

from data.config import CHANNELS
from utils.misc import subscription
from loader import bot

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):        
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                for x in range(1, 9):
                    try:
                        await update.message.delete()   
                        await update.message.delete()
                    except:
                        pass
                    try:             
                        await bot.delete_message(chat_id=update.message.chat.id, message_id=update.message.message_id-x)
                    except:
                        pass
                #await state.reset_state(with_data=False)
                await update.message.answer("<b>Telefon bozori yordamchi botiga xush kelibsiz</b>")
                await update.message.answer("<b>Вас приветствует bot канала Telefon bozori</b>", reply_markup=menuLanguage)
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:\n"
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"👉 <a href='{invite_link}'>{channel.title}</a>\n")

        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            raise CancelHandler()
