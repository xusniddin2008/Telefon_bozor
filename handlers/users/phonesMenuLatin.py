from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from data.config import ADMINS, CHANNELS
from keyboards.inline.phonesInlineKeyboardLatin import newSecondMenuLatin, statePhoneMenuLatin, boxPassPhoneMenuLatin, exchangePhoneMenuLatin, lookMenuLatin, userConfirmationMenuLatin, newAdsMenuLatin, writeFormsMenuLatin
from keyboards.inline.callback_dataLatin import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, new_ads_callback, write_forms_callback
from states.personalDataLatin import PersonalDataLatin

from loader import dp, bot

#################################################################################################################################
@dp.message_handler(text = "🇺🇿 Tilni tanlang")
async def uz_language(message: Message, state: FSMContext):    
    for x in range(1, 11):
        try:                
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-x)
            await message.delete()
        except:
            pass    
    #await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAK3HmMebiyIj_SlZaOs-VQtJ0FOlssmAALMHAACeRz5SNPAuItUxJ8JKQQ', caption="sassassasasasas")
    await message.answer(f"<b>E`lonni qanday ko`rinishda bermoqchisiz?</b>", reply_markup = writeFormsMenuLatin)
    await PersonalDataLatin.writeForms.set()
#################################################################################################################################
@dp.callback_query_handler(write_forms_callback.filter(), state=PersonalDataLatin.writeForms)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "write":
        await call.message.answer(f"<b>E`lonni quyidagi ko`rinishda yozing!</b>")
        await call.message.answer(f"Misol uchun\n\n<b>📱Telefon nomi : Xiaomi Poco F3\n💾Xotirasi : 128/6 Gb\n📆Ishlatilgan vaqti : 1 yil ishlatilgan\n⚙️Holati : Alo\n⛔️Aybi, kamchiligi : Yo`q\n🌈Rangi : black\n📦📄Korobka, hujjati : yo`q, Pasport nusxa beriladi\n🎁Aksessuarlar : AirPods 2\n♻️Ayirboshlash(обмен) : Yo`q\n💰Narxi : 280$\n📞Aloqa uchun : +998990000000</b>")
        await PersonalDataLatin.writePost.set()
    elif callback_data["item_name"] == "forms":
        await call.message.answer(f"<b>Telefon nomi va modelini quyidagi ko`rinishda yozing!</b>", reply_markup = ReplyKeyboardRemove())
        await call.message.answer(f"Misol uchun\n\n<b>iPhone 13 Pro Max\n\nYoki\n\nXiaomi Poco F3</b>")
        await call.answer(cache_time = 60)
        await PersonalDataLatin.modelName.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Kanaldan olib tashlanadigan e`lon ID raqamini yozing</b>")        
        await PersonalDataLatin.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.writeForms)
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
        await message.answer(f"<b>E`lonni qanday ko`rinishda bermoqchisiz?</b>", reply_markup = writeFormsMenuLatin)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.writePost)
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
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>9 ta gacha Foto va 1 dona Video (video majburiy emas) jo`nating</b>")
        await PersonalDataLatin.photoVideo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.modelName)
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
        modelName = f"📱Telefon nomi : {message.text}\n"  
        await state.update_data(msg = modelName)
        await state.update_data(number = 0)
        await state.update_data(photoIds = {})
        await state.update_data(videoId = 0)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Telefon xotirasini quyidagi ko`rinishda yozing</b>")
        await message.answer(f"Misol uchun\n\n<b>32/3\n\nYoki\n\n128</b>")
        await PersonalDataLatin.memoryRam.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.memoryRam)
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
        memoryRam = f"💾Xotirasi : {message.text} Gb\n"
        await state.update_data(msg = msg + memoryRam)        
        data = await state.get_data()
        msg = data.get("msg")    
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await state.update_data(step = "stepNewSecond")
        await message.answer(f"<b>Telefon holatini tanlang</b>", reply_markup = newSecondMenuLatin)
        await PersonalDataLatin.newSecond.set()
#################################################################################################################################
@dp.callback_query_handler(new_second_callback.filter(), state=PersonalDataLatin.newSecond)
async def new_second(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "newPhone":
        data = await state.get_data()
        msg = data.get("msg")
        newSecond = f"📆Ishlatilgan vaqti : Yangi\n"
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Telefon rangini yozing</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataLatin.phoneColor.set()
    elif callback_data["item_name"] == "secondHand":
        await state.update_data({"newSecond": "ishlatilgan"})
        await call.message.answer(f"<b>Telefon qancha vaqt ishlatilganini quyidagi ko`rinishda yozing</b>")
        await call.message.answer(f"Misol uchun\n\n<b>1.5 oy\n\nyoki\n\n2 yil</b>")
        await state.update_data(step = "stepPhoneWorkingTime")
        await PersonalDataLatin.phoneWorkingTime.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.newSecond)
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
        await message.answer("<b>Telefon holatini tanlang</b>", reply_markup = newSecondMenuLatin)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.phoneWorkingTime)
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
        newSecond = f"📆Ishlatilgan vaqti : {message.text} ishlatilgan\n"        
        await state.update_data(msg = msg + newSecond)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepStatePhone")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Telefon holatini tanlang</b>", reply_markup = statePhoneMenuLatin)
        await PersonalDataLatin.statePhone.set()
#################################################################################################################################
@dp.callback_query_handler(state_phone_callback.filter(), state=PersonalDataLatin.statePhone)
async def state_phone(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:                
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    statePhone = callback_data["item_name"]
    data = await state.get_data()
    msg = data.get("msg")    
    statePhone = f"⚙️Holati : {statePhone}\n"        
    await state.update_data(msg = msg + statePhone)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
    await call.message.answer("<b>Telefon aybi va kamchiliklarini yozing</b>")
    await call.message.answer("Misol uchun\n\n<b>Telefon ozgina qirilgan\n\nOrqa qopqog`i singan\n\nTelefon usta ko`rgan, ochilgan\n\nUmuman aybi yo`q</b>")
    await PersonalDataLatin.phoneProblem.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.statePhone)
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
        await message.answer("<b>Telefon holatini tanlang</b>", reply_markup = statePhoneMenuLatin)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.phoneProblem)
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
        phoneProblem = f"⛔️Aybi, kamchiligi : {message.text}\n"        
        await state.update_data(msg = msg + phoneProblem)
        data = await state.get_data()
        msg = data.get("msg")   
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await message.answer("<b>Telefon rangini yozing</b>")
        await state.update_data(step = "stepPhoneColor")
        await PersonalDataLatin.phoneColor.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.phoneColor)
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
        phoneColor = f"🌈Rangi : {message.text}\n"        
        await state.update_data(msg = msg + phoneColor)
        data = await state.get_data()
        msg = data.get("msg") 
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepBoxPass")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Korobkasi, xujjati bormi?</b>", reply_markup = boxPassPhoneMenuLatin)
        await PersonalDataLatin.boxPass.set()
#################################################################################################################################
@dp.callback_query_handler(box_pass_callback.filter(), state=PersonalDataLatin.boxPass)
async def box_pass(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    data = await state.get_data()
    msg = data.get("msg")
    boxPass = callback_data["item_name"]
    boxPass = f"📦📄Korobka, xujjati : {boxPass}\n"        
    await state.update_data(msg = msg + boxPass)
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.delete() 
    await call.message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
    await call.message.answer(f"<b>Qo`shimcha aksessuarlarni ro`yhatini quyidagi ko`rinishda yozing</b>")
    await call.message.answer(f"Misol uchun\n\n<b>Naushnik, Zaryadka, Airpods, Bluetooth naushnik lenovo lp40\n\nYo`q</b>")    
    await state.update_data(step = "stepAccessories")
    await PersonalDataLatin.accessories.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.boxPass)
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
        await message.answer(f"<b>Korobkasi, xujjati bormi?</b>", reply_markup = boxPassPhoneMenuLatin)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.accessories)
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
        accessories = f"🎁Aksessuarlar : {message.text}\n"        
        await state.update_data(msg = msg + accessories)
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.update_data(step = "stepExchange1")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Ayirboshlash(обмен) bormi?</b>", reply_markup = exchangePhoneMenuLatin)
        await PersonalDataLatin.exchange_callback.set()
#################################################################################################################################
@dp.callback_query_handler(exchange_callback.filter(), state=PersonalDataLatin.exchange_callback)
async def exchange(call: CallbackQuery, callback_data: dict, state: FSMContext):
    try:
        await call.message.delete()    
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)
    except:
        pass
    if callback_data["item_name"] == "no":
        data = await state.get_data()
        msg = data.get("msg")
        exchange = f"♻️Ayirboshlash(обмен) : Yo`q\n"
        await state.update_data(msg = msg + exchange)
        data = await state.get_data()
        msg = data.get("msg")                
        await call.message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")    
        await call.message.answer("<b>Qo`shimcha ma`lumotlarini yozing</b>")
        await call.message.answer(f"Misol uchun\n\n<b>🔋Batareyka darajasi : 85%\n\nYoki\n\nPul kerekligi uchun arzon sotayapman</b>")
        await PersonalDataLatin.addInfo.set()
    elif callback_data["item_name"] == "yes":
        await call.message.answer(f"<b>Telefon Ayirboshlash(обмен) shartlarini yozing</b>")
        await call.message.answer(f"Misol uchun\n\n<b>iPhone 13 Pro Max ga almashaman\n\nyoki\n\niPhone 13 Pro Max ga almashib ustiga 100$ beraman</b>")
        await state.update_data(step = "stepExchange2")
        await PersonalDataLatin.exchange.set()    
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.exchange_callback)
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
        await message.answer(f"<b>Ayirboshlash(обмен) bormi?</b>", reply_markup = exchangePhoneMenuLatin)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.exchange)
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
        exchange = f"♻️Ayirboshlash(обмен) : {message.text}\n"        
        await state.update_data(msg = msg + exchange)    
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")    
        await message.answer("<b>Qo`shimcha ma`lumotlarini yozing</b>")
        await message.answer(f"Misol uchun\n\n<b>🔋Batareyka darajasi : 85%\n\nYoki\n\nPul kerekligi uchun arzon sotayapman</b>")   
        await PersonalDataLatin.addInfo.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.addInfo)
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
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Narxini yozing</b>")
        await message.answer(f"Misol uchun\n\n<b>500$\n\nyoki\n\n3500000 So`m</b>")
        await PersonalDataLatin.price.set()    
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.price)
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
        price = f"\n💰Narxi : {message.text}\n"        
        await state.update_data(msg = msg + price)
        await state.update_data(step = "stepPrice")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await message.answer(f"<b>Telefon raqamingizni(yoki Telegram profil) quyidagi ko`rinishda yozing</b>")
        await message.answer(f"Misol uchun\n\n<b>+998990000000\n\nYoki\n\n@telegram_profil\n\nYoki ikkalasi\n\n+998990000000, @telegram_profil</b>")
        await PersonalDataLatin.phoneNumber.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.phoneNumber)
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
        phoneNumber = f"📞Aloqa uchun : <i>{message.text}</i>\n"        
        await state.update_data(msg = msg + phoneNumber)
        await state.update_data(step = "stepPhoneNumber")
        data = await state.get_data()
        msg = data.get("msg")
        await message.answer(f"Quyidagi ma`lumotlar qabul qilindi!:\n\n<b>{msg}</b>")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>9 ta gacha Foto va 1 dona Video (video majburiy emas) jo`nating</b>")
        await PersonalDataLatin.photoVideo.set()
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.PHOTO, state=PersonalDataLatin.photoVideo)
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
            await message.answer(f"<b>Foto qabul qilindi!</b>", reply_markup = lookMenuLatin)
        if number != 1:
            try:
                await bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message_id-1, text=f"<b>Foto qabul qilindi!</b>", reply_markup = lookMenuLatin)
            except:
                pass
    else:
        await message.answer(f"<b>Foto 9 tadan oshmasligi kerak!</b>")
    await message.delete()
#################################################################################################################################
@dp.message_handler(content_types=types.ContentType.VIDEO, state=PersonalDataLatin.photoVideo)
async def get_file_id_v(message: types.Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f"<b>Video qabul qilindi!</b>")    
    idVideo = message.video.file_id
    await state.update_data(videoId = idVideo)
#################################################################################################################################
@dp.callback_query_handler(look_callback.filter(), state=PersonalDataLatin.photoVideo)
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
    await call.message.answer(f"<b>_______________________________________</b>", reply_markup = userConfirmationMenuLatin)
    await call.answer(cache_time = 60)
    await PersonalDataLatin.finished.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.photoVideo)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.callback_query_handler(user_confirmation_callback.filter(), state=PersonalDataLatin.finished)
async def finished(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data["item_name"] == "post":
        data = await state.get_data()
        album = data.get("media")
        await call.message.edit_reply_markup()
        await call.answer("E`lon Adminga yuborildi! Tez orada kanalga joylanadi", show_alert=True)
        data = await state.get_data()
        album = data.get("media")
        await dp.bot.send_media_group(ADMINS[0], media=album)
        await bot.send_message(ADMINS[0], f"First name: {call.message.chat.first_name}\nUser name: @{call.message.chat.username}\nUser ID: {call.message.chat.id}\nFoydalanuvchi tepadagi postni chop etmoqchi:")
        await bot.send_message(ADMINS[0], f"<b>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</b>")
        await call.message.answer(f"<b>Yangi e`lon berish</b>", reply_markup = newAdsMenuLatin)
    elif callback_data["item_name"] == "cancel":
        await call.message.delete()
        try:
            for x in range(1, 11):                
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-x)
        except:
            pass
        await call.message.answer(f"Yangi e`lon berish", reply_markup = newAdsMenuLatin)
    await call.answer(cache_time = 60)
    await PersonalDataLatin.new_ads.set()
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.finished)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.callback_query_handler(new_ads_callback.filter(), state=PersonalDataLatin.new_ads)
async def new_ads(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    if callback_data["item_name"] == "newAds":
        await call.message.answer(f"<b>_______________________________________</b>")
        await call.message.answer(f"<b>E`lonni qanday ko`rinishda bermoqchisiz?</b>", reply_markup = writeFormsMenuLatin)
        await PersonalDataLatin.writeForms.set()
    elif callback_data["item_name"] == "deletePost":
        await call.message.answer(f"<b>Kanaldan olib tashlanadigan e`lon ID raqamini yozing</b>")        
        await PersonalDataLatin.deletePost.set()
    await call.answer(cache_time = 60)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.new_ads)
async def post_unknown(message: Message, state: FSMContext):    
    try:                
        await message.delete()
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
#################################################################################################################################
@dp.message_handler(state=PersonalDataLatin.deletePost)
async def answer_modelName(message: types.Message, state: FSMContext):
    try:                
        await message.delete()    
        await bot.delete_message(message.from_user.id, message.message_id-1)
    except:
        pass
    if f"{message.text}" == "/start":
        await state.reset_state(with_data=False)
    else:
        await bot.send_message(ADMINS[0], f"First name: {message.chat.first_name}\nUser name: @{message.chat.username}\nUser ID: {message.chat.id}\nFoydalanuvchi {message.text} raqamli postni kanaldan olib tashlanishini so`ramoqda")
        await message.answer(f"ElonID: {message.text} raqamli e`lon olib tashlanishi xaqidagi habar adminga yuborildi\n\nE`lon kanaldan tez orada olib tashlanadi")
        await state.reset_state(with_data=False)
        await message.answer(f"<b>Yangi e`lon berish</b>", reply_markup = newAdsMenuLatin)
        await PersonalDataLatin.new_ads.set()
#################################################################################################################################