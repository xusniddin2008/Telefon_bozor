from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_dataRu import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, admin_confirmation_callback, new_ads_callback, write_forms_callback
import json

##################################################################################################################################
writeFormsMenuRu = InlineKeyboardMarkup(row_width = 1)
write = InlineKeyboardButton(text="Написать объявление в ручном режиме", callback_data = write_forms_callback.new(item_name="write"))
writeFormsMenuRu.insert(write)

forms = InlineKeyboardButton(text="Заполнение объявления в виде формы", callback_data = write_forms_callback.new(item_name="forms"))
writeFormsMenuRu.insert(forms)

deletePost = InlineKeyboardButton(text="Убрать объявления с канала", callback_data = write_forms_callback.new(item_name="deletePost"))
writeFormsMenuRu.insert(deletePost)
##################################################################################################################################
newSecondMenuRu = InlineKeyboardMarkup(row_width = 1)
newPhone = InlineKeyboardButton(text="Телефон: Новый", callback_data = new_second_callback.new(item_name="newPhone"))
newSecondMenuRu.insert(newPhone)

secondHand = InlineKeyboardButton(text="Телефон: Бывший в Употреблении", callback_data = new_second_callback.new(item_name="secondHand"))
newSecondMenuRu.insert(secondHand)
##################################################################################################################################
statePhoneMenuRu = InlineKeyboardMarkup(row_width = 1)
statePhoneIdeal = InlineKeyboardButton(text="Состояния телефона: В идеальном состоянии", callback_data = state_phone_callback.new(item_name="Alo(Ideal)"))
statePhoneMenuRu.insert(statePhoneIdeal)

statePhoneNice = InlineKeyboardButton(text="Состояния телефона: В хорошим состоянии", callback_data = state_phone_callback.new(item_name="Yahshi"))
statePhoneMenuRu.insert(statePhoneNice)

statePhoneAverage = InlineKeyboardButton(text="Состояния телефона: Средний", callback_data = state_phone_callback.new(item_name="O`rta"))
statePhoneMenuRu.insert(statePhoneAverage)

statePhoneBelowAverage = InlineKeyboardButton(text="Состояния телефона: Ниже среднего", callback_data = state_phone_callback.new(item_name="O`rtadan past"))
statePhoneMenuRu.insert(statePhoneBelowAverage)
##################################################################################################################################
boxPassPhoneMenuRu = InlineKeyboardMarkup(row_width = 1)
boxYes = InlineKeyboardButton(text="Коробка, Документ есть", callback_data = box_pass_callback.new(item_name="bor"))
boxPassPhoneMenuRu.insert(boxYes)

boxNo = InlineKeyboardButton(text="Нет, Даю копию паспорта", callback_data = box_pass_callback.new(item_name="yo`q, Pasport nusha beriladi"))
boxPassPhoneMenuRu.insert(boxNo)
##################################################################################################################################
exchangePhoneMenuRu = InlineKeyboardMarkup(row_width = 1)
exchangeYes = InlineKeyboardButton(text="Обмен есть", callback_data = exchange_callback.new(item_name="yes"))
exchangePhoneMenuRu.insert(exchangeYes)

exchangeNo = InlineKeyboardButton(text="Обмен нет", callback_data = exchange_callback.new(item_name="no"))
exchangePhoneMenuRu.insert(exchangeNo)

##################################################################################################################################
lookMenuRu = InlineKeyboardMarkup(row_width = 1)
cancel = InlineKeyboardButton(text="Посмотреть объявление", callback_data = look_callback.new(item_name="cancel"))
lookMenuRu.insert(cancel)
##################################################################################################################################
userConfirmationMenuRu = InlineKeyboardMarkup(row_width = 1)
userConfirmationPost = InlineKeyboardButton(text="🆗 Отправить объявление администратору", callback_data = user_confirmation_callback.new(item_name="post"))
userConfirmationMenuRu.insert(userConfirmationPost)

userConfirmationCancel = InlineKeyboardButton(text="❌ Отмена", callback_data = user_confirmation_callback.new(item_name="cancel"))
userConfirmationMenuRu.insert(userConfirmationCancel)
##################################################################################################################################
adminConfirmationMenuRu = InlineKeyboardMarkup(row_width = 1)
adminConfirmationPost = InlineKeyboardButton(text="🆗 Размещение объявления на канал", callback_data = admin_confirmation_callback.new(item_name="post"))
adminConfirmationMenuRu.insert(adminConfirmationPost)

adminConfirmationCancel = InlineKeyboardButton(text="❌ Отмена", callback_data = admin_confirmation_callback.new(item_name="cancel"))
adminConfirmationMenuRu.insert(adminConfirmationCancel)
##################################################################################################################################
newAdsMenuRu = InlineKeyboardMarkup(row_width = 1)
newAds = InlineKeyboardButton(text="Подать новий объявления", callback_data = new_ads_callback.new(item_name="newAds"))
newAdsMenuRu.insert(newAds)

deletePost = InlineKeyboardButton(text="Убрать объявления с канала", callback_data = new_ads_callback.new(item_name="deletePost"))
newAdsMenuRu.insert(deletePost)