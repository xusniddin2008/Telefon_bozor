from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from data.config import ADMINS, CHANNELS
from keyboards.inline.phonesInlineKeyboardRu import newSecondMenuRu, statePhoneMenuRu, boxPassPhoneMenuRu, exchangePhoneMenuRu, lookMenuRu, userConfirmationMenuRu, newAdsMenuRu, writeFormsMenuRu
from keyboards.inline.callback_dataRu import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, new_ads_callback, write_forms_callback
from states.personalDataRu import PersonalDataRu

from loader import dp, bot

#################################################################################################################################
@dp.message_handler(text = "🇷🇺 Выберите язык")
async def uz_language(message: Message, state: FSMContext):    
    for x in range(1, 11):
        try:                
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-x)
            await message.delete()
        except:
            pass    
    #await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAK3HmMebiyIj_SlZaOs-VQtJ0FOlssmAALMHAACeRz5SNPAuItUxJ8JKQQ', caption="sassassasasasas")
    await message.answer(f"<b>В каком виде подать объявление?</b>", reply_markup = writeFormsMenuRu)
    await PersonalDataRu.writeForms.set()
#################################################################################################################################
@dp.callback_query_handler(write_forms_callback.filter(), state=PersonalDataRu.writeForms)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "write":
        await call.message.answer(f"<b>Напишите объявление ниже указанном виде</b>")
        await call.message.answer(f"На пример\n\n<b>📱Названия телефона : Xiaomi Poco F3\n💾Память : 128/6 ГБ\n📆Время использования : пользовался 2 года\n⚙️Состояния : Идеал\n⛔️Неисправность, недостатки : Нет\n🌈Цвет : black\n📦📄Коробка, Документ : Нет, Даю копию паспорта\n🎁Аксессуары : AirPods 2\n♻️Обмен : Нет\n💰Цена : 280$\n📞Для контакта : +998990000000</b>")
        await PersonalDataRu.writePost.set()
    elif callback_data["item_name"] == "forms":
        await call.message.answer(f"<b>Напишите названия телефона ниже указанном виде</b>", reply_markup = ReplyKeyboardRemove())
        await call.message.answer(f"На пример\n\n<b>iPhone 13 Pro Max\n\nИли\n\nXiaomi Poco F3</b>")
        await call.answer(cache_time = 60)
        await PersonalDataRu.modelName.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Напишите ID объявления который хотите убрать с канала</b>")        
        await PersonalDataRu.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.writeForms)
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
        await message.answer(f"<b>В каком виде подать объявление?</b>", reply_markup = writeFormsMenuRu)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.writePost)
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
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Отправьте до 9 фотографий и 1 Видео (видео не обязательно)</b>")
        await PersonalDataRu.photoVideo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.modelName)
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
        modelName = f"📱Названия телефона : {message.text}\n"  
        await state.update_data(msg = modelName)
        await state.update_data(number = 0)
        await state.update_data(photoIds = {})
        await state.update_data(videoId = 0)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Напишите памят телефона ниже указанном виде</b>")
        await message.answer(f"На пример\n\n<b>32/3\n\nИли\n\n128</b>")
        await PersonalDataRu.memoryRam.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.memoryRam)
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
        memoryRam = f"💾Памят : {message.text} ГБ\n"
        await state.update_data(msg = msg + memoryRam)        
        data = await state.get_data()
        msg = data.get("msg")    
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await state.update_data(step = "stepNewSecond")
        await message.answer(f"<b>Выберите состояния телефона</b>", reply_markup = newSecondMenuRu)
        await PersonalDataRu.newSecond.set()
#################################################################################################################################
@dp.callback_query_handler(new_second_callback.filter(), state=PersonalDataRu.newSecond)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "newPhone":
        data = await state.get_data()
        msg = data.get("msg")
        newSecond = f"📆Время использования : Новий\n"
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Принятие информации:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Напишите цвет телефона</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataRu.phoneColor.set()
    elif callback_data["item_name"] == "secondHand":
        await state.update_data({"newSecond": "Бывший в Употреблении"})
        await call.message.answer(f"<b>Напишите время использования телефона ниже указанном виде</b>")
        await call.message.answer(f"На пример\n\n<b>1.5 месяц\n\nИли\n\n2 год</b>")
        await state.update_data(step = "stepPhoneWorkingTime")
        await PersonalDataRu.phoneWorkingTime.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.newSecond)
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
        await message.answer("<b>Выберите состояния телефона</b>", reply_markup = newSecondMenuRu)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.phoneWorkingTime)
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
        newSecond = f"📆Время использования : {message.text}\n"        
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepStatePhone")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Выберите состояния телефона</b>", reply_markup = statePhoneMenuRu)
        await PersonalDataRu.statePhone.set()
#################################################################################################################################
@dp.callback_query_handler(state_phone_callback.filter(), state=PersonalDataRu.statePhone)
async def state_phone(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:                
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    statePhone = callback_data["item_name"]
    data = await state.get_data()
    msg = data.get("msg")    
    statePhone = f"⚙️Состояния : {statePhone}\n"        
    await state.update_data(msg = msg + statePhone)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
    await call.message.answer("<b>Напишите неисправности и недостатки телефона</b>")
    await call.message.answer("На пример\n\n<b>Есть немного царапина\n\nСломан задний крышка\n\nТелефон ремонтировался, очилган\n\nНикаких недостатки нет</b>")
    await PersonalDataRu.phoneProblem.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.statePhone)
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
        await message.answer("<b>Выберите состояния телефона</b>", reply_markup = statePhoneMenuRu)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.phoneProblem)
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
        phoneProblem = f"⛔️Неисправности, недостатки : {message.text}\n"        
        await state.update_data(msg = msg + phoneProblem)
        data = await state.get_data()
        msg = data.get("msg")   
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await message.answer("<b>Напишите цвет телефона</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataRu.phoneColor.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.phoneColor)
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
        phoneColor = f"🌈Цвет : {message.text}\n"        
        await state.update_data(msg = msg + phoneColor)
        data = await state.get_data()
        msg = data.get("msg") 
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepBoxPass")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Коробка, Документ есть?</b>", reply_markup = boxPassPhoneMenuRu)
        await PersonalDataRu.boxPass.set()
#################################################################################################################################
@dp.callback_query_handler(box_pass_callback.filter(), state=PersonalDataRu.boxPass)
async def box_pass(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    data = await state.get_data()
    msg = data.get("msg")
    boxPass = callback_data["item_name"]
    boxPass = f"📦📄Коробка, Документ : {boxPass}\n"        
    await state.update_data(msg = msg + boxPass)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
    await call.message.answer(f"<b>Напишите список аксессуаров ниже указанном виде</b>")
    await call.message.answer(f"На пример\n\n<b>Наушник, Зарядное устройство, Airpods, Bluetooth наушник lenovo lp40\n\nYo`q</b>")    
    await state.update_data(step = "stepAccessories")
    await PersonalDataRu.accessories.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.boxPass)
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
        await message.answer(f"<b>Коробка, Документ есть?</b>", reply_markup = boxPassPhoneMenuRu)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.accessories)
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
        accessories = f"🎁Аксессуары : {message.text}\n"        
        await state.update_data(msg = msg + accessories)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepExchange1")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Обмен есть?</b>", reply_markup = exchangePhoneMenuRu)
        await PersonalDataRu.exchange_callback.set()
#################################################################################################################################
@dp.callback_query_handler(exchange_callback.filter(), state=PersonalDataRu.exchange_callback)
async def exchange(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()    
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "no":
        data = await state.get_data()
        msg = data.get("msg")
        exchange = f"♻️Обмен : Нет\n"
        await state.update_data(msg = msg + exchange)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Принятие информации:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Напишите дополнительные информации</b>")
        await call.message.answer(f"На пример\n\n<b>🔋Износ батареи : 85%\n\nИли\n\nПродаю потому что нужны деньги</b>")
        await PersonalDataRu.addInfo.set()
    elif callback_data["item_name"] == "yes":
        await call.message.answer(f"<b>Напишите условия обмена</b>")
        await call.message.answer(f"На пример\n\n<b>Обменяю на iPhone 13 Pro Max\n\nИли\n\nОбменяю на iPhone 13 Pro Max с моей доплатой</b>")
        await state.update_data(step = "stepExchange2")
        await PersonalDataRu.exchange.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.exchange_callback)
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
        await message.answer(f"<b>Обмен есть?</b>", reply_markup = exchangePhoneMenuRu)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.exchange)
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
        exchange = f"♻️Обмен : {message.text}\n"        
        await state.update_data(msg = msg + exchange)    
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")    
        await message.answer("<b>Напишите дополнительные информации</b>")
        await message.answer(f"На пример\n\n<b>🔋Износ батареи : 85%\n\nИли\n\nПродаю потому что нужны деньги</b>")   
        await PersonalDataRu.addInfo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.addInfo)
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
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Напишите цену</b>")
        await message.answer(f"На пример\n\n<b>500$\n\nИли\n\n3500000 Сум</b>")
        await PersonalDataRu.price.set()    
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.price)
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
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Напишите номер телефона (или Телеграм профиль) ниже указанном виде</b>")
        await message.answer(f"На пример\n\n<b>+998990000000\n\nИли\n\n@TelefonBozorii_uzAdmin\n\nИли оба сразу\n\n+998990000000, @TelefonBozorii_uzAdmin</b>")
        await PersonalDataRu.phoneNumber.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.phoneNumber)
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
        phoneNumber = f"📞Для контакта : <i>{message.text}</i>\n"        
        await state.update_data(msg = msg + phoneNumber)
        await state.update_data(step = "stepPhoneNumber")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Принятие информации:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Отправьте до 9 фотографий и 1 Видео (видео не обязательно)</b>")
        await PersonalDataRu.photoVideo.set()
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.PHOTO, state=PersonalDataRu.photoVideo)
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
            await message.answer(f"<b>Фотография принято</b>", reply_markup = lookMenuRu)
        if number != 1:
            try:
                await bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message_id-1, text=f"<b>Фотография принято</b>", reply_markup = lookMenuRu)
            except:
                pass
    else:
        await message.answer(f"<b>Фотографии не должны превышать 9ти!</b>")
    await message.delete()    
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.VIDEO, state=PersonalDataRu.photoVideo)
async def get_file_id_v(message: types.Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f"<b>Видео принято</b>")    
    idVideo = message.video.file_id
    await state.update_data(videoId = idVideo)
#################################################################################################################################
@dp.callback_query_handler(look_callback.filter(), state=PersonalDataRu.photoVideo)
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
    await call.message.answer(f"<b>_______________________________________</b>", reply_markup = userConfirmationMenuRu)
    await call.answer(cache_time = 60)
    await PersonalDataRu.finished.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.photoVideo)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.callback_query_handler(user_confirmation_callback.filter(), state=PersonalDataRu.finished)
async def finished(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data["item_name"] == "post":
        data = await state.get_data()
        album = data.get("media")
        await call.message.edit_reply_markup()
        await call.answer("объявления отправлено в админ, объявления будет размещено на канал в ближайшее время", show_alert=True)
        data = await state.get_data()
        album = data.get("media")
        await dp.bot.send_media_group(ADMINS[0], media=album)
        await bot.send_message(ADMINS[0], f"First name: {call.message.chat.first_name}\nUser name: @{call.message.chat.username}\nUser ID: {call.message.chat.id}\nФойдаланувчи тепадаги постни чоп этмоқчи:")
        await bot.send_message(ADMINS[0], f"<b>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</b>")
        await call.message.answer(f"<b>Подать новий объявления</b>", reply_markup = newAdsMenuRu)
    elif callback_data["item_name"] == "cancel":
        await call.message.delete()
        try:
            for x in range(1, 11):                
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-x)
        except:
            pass
        await call.message.answer(f"Подать новий объявления", reply_markup = newAdsMenuRu)
    await call.answer(cache_time = 60)
    await PersonalDataRu.new_ads.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.finished)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False) 
#################################################################################################################################
@dp.callback_query_handler(new_ads_callback.filter(), state=PersonalDataRu.new_ads)
async def new_ads(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "newAds":
        await call.message.answer(f"<b>_______________________________________</b>")
        await call.message.answer(f"<b>В каком виде подать объявление?</b>", reply_markup = writeFormsMenuRu)
        await PersonalDataRu.writeForms.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Напишите ID объявления который хотите убрать с канала</b>")        
        await PersonalDataRu.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.new_ads)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.message_handler(state=PersonalDataRu.deletePost)
async def answer_modelName(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        await bot.send_message(ADMINS[0], f"First name: {message.chat.first_name}\nUser name: @{message.chat.username}\nUser ID: {message.chat.id}\nПользователь просит удалить пост номер {message.text} с канала")
        await message.answer(f"Админу отправлено сообщение об удалении объявления ElonID: {message.text}\n\nОбъявления скоро будет удалена с канала")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Подать новий объявления</b>", reply_markup = newAdsMenuRu)
        await PersonalDataRu.new_ads.set()
#################################################################################################################################