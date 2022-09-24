from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from data.config import ADMINS, CHANNELS
from keyboards.inline.phonesInlineKeyboardKiril import newSecondMenuKiril, statePhoneMenuKiril, boxPassPhoneMenuKiril, exchangePhoneMenuKiril, lookMenuKiril, userConfirmationMenuKiril, newAdsMenuKiril, writeFormsMenuKiril
from keyboards.inline.callback_dataKiril import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, new_ads_callback, write_forms_callback
from states.personalDataKiril import PersonalDataKiril

from loader import dp, bot

#################################################################################################################################
@dp.message_handler(text = "🇺🇿 Тилни танланг")
async def uz_language(message: Message, state: FSMContext):
    for x in range(1, 11):
        try:                
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-x)
            await message.delete()
        except:
            pass    
    #await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAK3HmMebiyIj_SlZaOs-VQtJ0FOlssmAALMHAACeRz5SNPAuItUxJ8JKQQ', caption="sassassasasasas")
    await message.answer(f"<b>Эълонни қандай кўринишда бермоқчисиз?</b>", reply_markup = writeFormsMenuKiril)
    await PersonalDataKiril.writeForms.set()
#################################################################################################################################
@dp.callback_query_handler(write_forms_callback.filter(), state=PersonalDataKiril.writeForms)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "write":
        await call.message.answer(f"<b>Эълонни қуйидаги кўринишда ёзинг</b>")
        await call.message.answer(f"Мисол учун\n\n<b>📱Телефон номи : Xiaomi Poco F3\n💾Хотираси : 128/6 Gb\n📆Ишлатилган вақти : 1 йил ишлатилган\n⚙️Ҳолати : Аъло\n⛔️Айби, камчилиги : Йўқ\n🌈Ранги : black\n📦📄Коробка, хужжати : йўқ, Паспорт нусха берилади\n🎁Аксессуарлар : AirPods 2\n♻️Айирбошлаш(обмен) : Йўқ\n💰Нархи : 280$\n📞Алоқа учун : +998990000000</b>")
        await PersonalDataKiril.writePost.set()
    elif callback_data["item_name"] == "forms":
        await call.message.answer(f"<b>Телефон номи ва моделини қуйидаги кўринишда ёзинг</b>", reply_markup = ReplyKeyboardRemove())
        await call.message.answer(f"Мисол учун\n\n<b>iPhone 13 Pro Max\n\nЁки\n\nXiaomi Poco F3</b>")
        await call.answer(cache_time = 60)
        await PersonalDataKiril.modelName.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Каналдан олиб ташланадиган эълон ID рақамини ёзинг</b>")        
        await PersonalDataKiril.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.writeForms)
async def post_unknown(message: Message, state: FSMContext):    
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        try:                
            await message.delete()    
            await bot.delete_message(message.from_user.id, message.message_id-1)
            await bot.delete_message(message.from_user.id, message.message_id-2)
        except:
            pass      
        await message.answer(f"<b>Эълонни қандай кўринишда бермоқчисиз?</b>", reply_markup = writeFormsMenuKiril)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.writePost)
async def answer_modelName(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        msg = f"{message.text}"
        await state.update_data(msg = msg)
        await state.update_data(number = 0)
        await state.update_data(photoIds = {})
        await state.update_data(videoId = 0)
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>9 та гача Фото ва 1 дона Видео (видео мажбурий эмас) жўнатинг</b>")
        await PersonalDataKiril.photoVideo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.modelName)
async def answer_modelName(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        modelName = f"📱Телефон номи : {message.text}\n"  
        await state.update_data(msg = modelName)
        await state.update_data(number = 0)
        await state.update_data(photoIds = {})
        await state.update_data(videoId = 0)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Телефон хотирасини қуйидаги кўринишда ёзинг</b>")
        await message.answer(f"Мисол учун\n\n<b>32/3\n\nЁки\n\n128</b>")
        await PersonalDataKiril.memoryRam.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.memoryRam)
async def answer_memoryRam(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        memoryRam = f"💾Хотираси : {message.text} ГБ\n"
        await state.update_data(msg = msg + memoryRam)        
        data = await state.get_data()
        msg = data.get("msg")    
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await state.update_data(step = "stepNewSecond")
        await message.answer(f"<b>Телефон ҳолатини танланг</b>", reply_markup = newSecondMenuKiril)
        await PersonalDataKiril.newSecond.set()
#################################################################################################################################
@dp.callback_query_handler(new_second_callback.filter(), state=PersonalDataKiril.newSecond)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "newPhone":
        data = await state.get_data()
        msg = data.get("msg")
        newSecond = f"📆Ишлатилган вақти : Янги\n"
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Телефон рангини ёзинг</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataKiril.phoneColor.set()
    elif callback_data["item_name"] == "secondHand":
        await state.update_data({"newSecond": "ишлатилган"})
        await call.message.answer(f"<b>Телефон қанча вақт ишлатилганини қуйидаги кўринишда ёзинг</b>")
        await call.message.answer(f"Мисол учун\n\n<b>1.5 ой\n\nЁки\n\n2 йил</b>")
        await state.update_data(step = "stepPhoneWorkingTime")
        await PersonalDataKiril.phoneWorkingTime.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.newSecond)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:    
        await message.answer("<b>Телефон ҳолатини танланг</b>", reply_markup = newSecondMenuKiril)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.phoneWorkingTime)
async def answer_phoneWorkingTime(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")    
        newSecond = f"📆Ишлатилган вақти : {message.text} ишлатилган\n"        
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepStatePhone")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Телефон ҳолатини танланг</b>", reply_markup = statePhoneMenuKiril)
        await PersonalDataKiril.statePhone.set()
#################################################################################################################################
@dp.callback_query_handler(state_phone_callback.filter(), state=PersonalDataKiril.statePhone)
async def state_phone(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:                
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    statePhone = callback_data["item_name"]
    data = await state.get_data()
    msg = data.get("msg")    
    statePhone = f"⚙️Ҳолати : {statePhone}\n"        
    await state.update_data(msg = msg + statePhone)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
    await call.message.answer("<b>Телефон айби ва камчиликларини ёзинг</b>")
    await call.message.answer("Мисол учун\n\n<b>Телефон озгина қирилган\n\nОрқа қопқоғи синган\n\nТелефон уста кўрган, очилган\n\nУмуман айби йўқ</b>")
    await PersonalDataKiril.phoneProblem.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.statePhone)
async def post_unknown(message: Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        await message.answer("<b>Телефон ҳолатини танланг</b>", reply_markup = statePhoneMenuKiril)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.phoneProblem)
async def answer_phoneProblem(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        phoneProblem = f"⛔️Айби, камчилиги : {message.text}\n"        
        await state.update_data(msg = msg + phoneProblem)
        data = await state.get_data()
        msg = data.get("msg")   
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await message.answer("<b>Телефон рангини ёзинг</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataKiril.phoneColor.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.phoneColor)
async def answer_phoneColor(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        phoneColor = f"🌈Ранги : {message.text}\n"        
        await state.update_data(msg = msg + phoneColor)
        data = await state.get_data()
        msg = data.get("msg") 
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepBoxPass")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Коробкаси, хужжати борми?</b>", reply_markup = boxPassPhoneMenuKiril)
        await PersonalDataKiril.boxPass.set()
#################################################################################################################################
@dp.callback_query_handler(box_pass_callback.filter(), state=PersonalDataKiril.boxPass)
async def box_pass(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    data = await state.get_data()
    msg = data.get("msg")
    boxPass = callback_data["item_name"]
    boxPass = f"📦📄Коробка, хужжати : {boxPass}\n"        
    await state.update_data(msg = msg + boxPass)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
    await call.message.answer(f"<b>Қўшимча аксессуарларни рўйхатини қуйидаги кўринишда ёзинг</b>")
    await call.message.answer(f"Мисол учун\n\n<b>Наушник, Зарядка, Airpods, Bluetooth наушник lenovo lp40\n\nYo`q</b>")    
    await state.update_data(step = "stepAccessories")
    await PersonalDataKiril.accessories.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.boxPass)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:    
        await message.answer(f"<b>Коробкаси, хужжати борми?</b>", reply_markup = boxPassPhoneMenuKiril)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.accessories)
async def answer_accessories(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        accessories = f"🎁Аксессуарлар : {message.text}\n"        
        await state.update_data(msg = msg + accessories)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepExchange1")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Айирбошлаш(обмен) борми?</b>", reply_markup = exchangePhoneMenuKiril)
        await PersonalDataKiril.exchange_callback.set()
#################################################################################################################################
@dp.callback_query_handler(exchange_callback.filter(), state=PersonalDataKiril.exchange_callback)
async def exchange(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()    
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "no":
        data = await state.get_data()
        msg = data.get("msg")
        exchange = f"♻️Айирбошлаш(обмен) : Йўқ\n"
        await state.update_data(msg = msg + exchange)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Қўшимча маълумотларни ёзинг</b>")
        await call.message.answer(f"Мисол учун\n\n<b>🔋Батарейка даражаси : 85%\n\nЁки\n\nПул кераклиги учун арзон сотаяпман</b>")
        await PersonalDataKiril.addInfo.set()
    elif callback_data["item_name"] == "yes":
        await call.message.answer(f"<b>Телефон айирбошлаш(обмен) шартларини ёзинг</b>")
        await call.message.answer(f"Мисол учун\n\n<b>iPhone 13 Pro Max га алмашаман\n\nЁки\n\niPhone 13 Pro Max га алмашиб устига 100$ бераман</b>")
        await state.update_data(step = "stepExchange2")
        await PersonalDataKiril.exchange.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.exchange_callback)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:   
        await message.answer(f"<b>Айирбошлаш(обмен) борми?</b>", reply_markup = exchangePhoneMenuKiril)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.exchange)
async def answer_exchange(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        exchange = f"♻️Айирбошлаш(обмен) : {message.text}\n"        
        await state.update_data(msg = msg + exchange)    
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")    
        await message.answer("<b>Қўшимча маълумотларни ёзинг</b>")
        await message.answer(f"Мисол учун\n\n<b>🔋Батарейка даражаси : 85%\n\nЁки\n\nПул кераклиги учун арзон сотаяпман</b>")   
        await PersonalDataKiril.addInfo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.addInfo)
async def answer_addInfo(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        addInfo = f"{message.text}\n"        
        await state.update_data(msg = msg + addInfo)
        await state.update_data(step = "stepAddInfo")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Нархини ёзинг</b>")
        await message.answer(f"Мисол учун\n\n<b>500$\n\nЁки\n\n3500000 Сўм</b>")
        await PersonalDataKiril.price.set()    
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.price)
async def answer_price(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        price = f"\n💰Нархи : {message.text}\n"        
        await state.update_data(msg = msg + price)
        await state.update_data(step = "stepPrice")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Телефон рақамингизни(ёки Телеграм профил) қуйидаги кўринишда ёзинг</b>")
        await message.answer(f"Мисол учун\n\n<b>+998990000000\n\nЁки\n\n@telegram_profil\n\nЁки иккаласи\n\n+998990000000, @telegram_profil</b>")
        await PersonalDataKiril.phoneNumber.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.phoneNumber)
async def answer_phoneNumber(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
        await bot.delete_message(message.from_user.id, message.message_id-2)
        await bot.delete_message(message.from_user.id, message.message_id-3)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        data = await state.get_data()
        msg = data.get("msg")
        phoneNumber = f"📞Алоқа учун : <i>{message.text}</i>\n"        
        await state.update_data(msg = msg + phoneNumber)
        await state.update_data(step = "stepPhoneNumber")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Қуйидаги маълумотлар қабул қилинди!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>9 та гача Фото ва 1 дона Видео (видео мажбурий эмас) жўнатинг</b>")
        await PersonalDataKiril.photoVideo.set()
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.PHOTO, state=PersonalDataKiril.photoVideo)
async def get_file_id_p(message: types.Message, state: FSMContext):
    '''for x in range(1, 11):
        try:                
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-x)
        except:
            pass'''
    photoId = message.photo[-1].file_id
    data = await state.get_data()
    number = int(data.get("number"))     
    photoIds = data.get("photoIds")
    number = number + 1
    if number <= 9:
        await state.update_data(number = number)
        photoIds.update({f"photoId{number}": photoId})        
        await state.update_data(photoIds = photoIds)
        if number == 1:
            try:
                await bot.send_message(ADMINS[0], f"<b>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</b>")
                await dp.bot.forward_message(ADMINS[0], message.chat.id, message.message_id)
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-2)
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-3)
            except:
                pass
            await message.answer(f"<b>Фото қабул қилинди!</b>", reply_markup = lookMenuKiril)
        if number != 1:
            try:
                await bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message_id-1, text=f"<b>Фото қабул қилинди!</b>", reply_markup = lookMenuKiril)
            except:
                pass
    else:
        await message.answer(f"<b>Фото 9 тадан ошмаслиги керак!</b>")
    await message.delete()
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.VIDEO, state=PersonalDataKiril.photoVideo)
async def get_file_id_v(message: types.Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f"<b>Видео қабул қилинди!</b>")    
    idVideo = message.video.file_id
    await state.update_data(videoId = idVideo)
#################################################################################################################################
@dp.callback_query_handler(look_callback.filter(), state=PersonalDataKiril.photoVideo)
async def look(call: CallbackQuery, callback_data: dict, state: FSMContext):
    for x in range(0, 11):
        try:                
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-x)
        except:
            pass
    try:
        with open('./elonID1.txt') as fayl:
            elonID = int(fayl.read())
            elonID = elonID + 1        
        if elonID > 0:
            with open('./elonID2.txt') as fayl:
                elonID = int(fayl.read())
                elonID = elonID + 1        
        with open('./elonID1.txt','w') as fayl:
            fayl.write(f"{elonID}")        
        with open('./elonID2.txt','w') as fayl:
            fayl.write(f"{elonID}")
    except:
        with open('./elonID2.txt') as fayl:
            elonID = int(fayl.read())
            elonID = elonID + 1
        with open('./elonID1.txt','w') as fayl:
            fayl.write(f"{elonID}")        
        with open('./elonID2.txt','w') as fayl:
            fayl.write(f"{elonID}")
    try:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    data = await state.get_data()
    msg = data.get("msg")
    photoIds = data.get("photoIds")
    videoId = data.get("videoId")
    album = types.MediaGroup()
    for item, photoId in photoIds.items():
        if item == "photoId1":            
            album.attach_photo(photo=photoId, caption=f"<b>{msg}</b>\n\nElonID: {elonID}")
        else:
            album.attach_photo(photo=photoId)
    if videoId != 0:
        album.attach_video(video=videoId)
    await state.update_data(media = album)
    await call.message.answer_media_group(media=album)
    await call.message.answer(f"<b>_______________________________________</b>", reply_markup = userConfirmationMenuKiril)
    await call.answer(cache_time = 60)
    await PersonalDataKiril.finished.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.photoVideo)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.callback_query_handler(user_confirmation_callback.filter(), state=PersonalDataKiril.finished)
async def finished(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data["item_name"] == "post":
        data = await state.get_data()
        album = data.get("media")
        await call.message.edit_reply_markup()
        await call.answer("Эълон Админга юборилди, тез орада каналга жойланади", show_alert=True)
        data = await state.get_data()
        album = data.get("media")
        await dp.bot.send_media_group(ADMINS[0], media=album)
        await bot.send_message(ADMINS[0], f"First name: {call.message.chat.first_name}\nUser name: @{call.message.chat.username}\nUser ID: {call.message.chat.id}\nФойдаланувчи тепадаги постни чоп этмоқчи:")
        await bot.send_message(ADMINS[0], f"<b>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</b>")
        await call.message.answer(f"<b>Янги эълон бериш</b>", reply_markup = newAdsMenuKiril)
    elif callback_data["item_name"] == "cancel":
        await call.message.delete()
        try:
            for x in range(1, 11):                
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-x)
        except:
            pass
        await call.message.answer(f"Янги эълон бериш", reply_markup = newAdsMenuKiril)
    await call.answer(cache_time = 60)
    await PersonalDataKiril.new_ads.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.finished)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)  
#################################################################################################################################
@dp.callback_query_handler(new_ads_callback.filter(), state=PersonalDataKiril.new_ads)
async def new_ads(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "newAds":
        await call.message.answer(f"<b>_______________________________________</b>")
        await call.message.answer(f"<b>Эълонни қандай кўринишда бермоқчисиз?</b>", reply_markup = writeFormsMenuKiril)
        await PersonalDataKiril.writeForms.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Каналдан олиб ташланадиган эълон ID рақамини ёзинг</b>")        
        await PersonalDataKiril.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.new_ads)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.message_handler(state=PersonalDataKiril.deletePost)
async def answer_modelName(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        await bot.send_message(ADMINS[0], f"First name: {message.chat.first_name}\nUser name: @{message.chat.username}\nUser ID: {message.chat.id}\nФойдаланувчи {message.text} рақамли постни каналдан олиб ташланишини сўрамоқда")
        await message.answer(f"ElonID: {message.text} рақамли эълон олиб ташланиши хақидаги хабар админга юборилди\n\nЭълон каналдан тез орада олиб ташланади")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Янги эълон бериш</b>", reply_markup = newAdsMenuKiril)
        await PersonalDataKiril.new_ads.set()
#################################################################################################################################