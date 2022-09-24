from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_dataKiril import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, admin_confirmation_callback, new_ads_callback, write_forms_callback
import json

##################################################################################################################################
writeFormsMenuKiril = InlineKeyboardMarkup(row_width = 1)
write = InlineKeyboardButton(text="Эълонни ёзиб жўнатиш", callback_data = write_forms_callback.new(item_name="write"))
writeFormsMenuKiril.insert(write)

forms = InlineKeyboardButton(text="Эълонни форма шаклида тўлдириш", callback_data = write_forms_callback.new(item_name="forms"))
writeFormsMenuKiril.insert(forms)

deletePost = InlineKeyboardButton(text="Эълонни каналдан олиб ташлаш", callback_data = write_forms_callback.new(item_name="deletePost"))
writeFormsMenuKiril.insert(deletePost)
##################################################################################################################################
newSecondMenuKiril = InlineKeyboardMarkup(row_width = 1)
newPhone = InlineKeyboardButton(text="Телефон: Янги", callback_data = new_second_callback.new(item_name="newPhone"))
newSecondMenuKiril.insert(newPhone)

secondHand = InlineKeyboardButton(text="Телефон: Ишлатилган", callback_data = new_second_callback.new(item_name="secondHand"))
newSecondMenuKiril.insert(secondHand)
##################################################################################################################################
statePhoneMenuKiril = InlineKeyboardMarkup(row_width = 1)
statePhoneIdeal = InlineKeyboardButton(text="Телефон ҳолати: Аъло(Идеал)", callback_data = state_phone_callback.new(item_name="Аъло(Идеал)"))
statePhoneMenuKiril.insert(statePhoneIdeal)

statePhoneNice = InlineKeyboardButton(text="Телефон ҳолати: Яхши", callback_data = state_phone_callback.new(item_name="Яхши"))
statePhoneMenuKiril.insert(statePhoneNice)

statePhoneAverage = InlineKeyboardButton(text="Телефон ҳолати: Ўрта", callback_data = state_phone_callback.new(item_name="Ўрта"))
statePhoneMenuKiril.insert(statePhoneAverage)

statePhoneBelowAverage = InlineKeyboardButton(text="Телефон ҳолати: Ўртадан паст", callback_data = state_phone_callback.new(item_name="Ўртадан паст"))
statePhoneMenuKiril.insert(statePhoneBelowAverage)
##################################################################################################################################
boxPassPhoneMenuKiril = InlineKeyboardMarkup(row_width = 1)
boxYes = InlineKeyboardButton(text="Коробкаси, хужжати бор", callback_data = box_pass_callback.new(item_name="бор"))
boxPassPhoneMenuKiril.insert(boxYes)

boxNo = InlineKeyboardButton(text="Йўқ, Паспорт нусха берилади", callback_data = box_pass_callback.new(item_name="йўқ, Паспорт нусха берилади"))
boxPassPhoneMenuKiril.insert(boxNo)
##################################################################################################################################
exchangePhoneMenuKiril = InlineKeyboardMarkup(row_width = 1)
exchangeYes = InlineKeyboardButton(text="Айирбошлаш(обмен) бор", callback_data = exchange_callback.new(item_name="yes"))
exchangePhoneMenuKiril.insert(exchangeYes)

exchangeNo = InlineKeyboardButton(text="Айирбошлаш(обмен) йўқ", callback_data = exchange_callback.new(item_name="no"))
exchangePhoneMenuKiril.insert(exchangeNo)

##################################################################################################################################
lookMenuKiril = InlineKeyboardMarkup(row_width = 1)
cancel = InlineKeyboardButton(text="Эълонни кўриш", callback_data = look_callback.new(item_name="cancel"))
lookMenuKiril.insert(cancel)
##################################################################################################################################
userConfirmationMenuKiril = InlineKeyboardMarkup(row_width = 1)
userConfirmationPost = InlineKeyboardButton(text="🆗 Эълонни Админга юбориш", callback_data = user_confirmation_callback.new(item_name="post"))
userConfirmationMenuKiril.insert(userConfirmationPost)

userConfirmationCancel = InlineKeyboardButton(text="❌ Бекор қилиш", callback_data = user_confirmation_callback.new(item_name="cancel"))
userConfirmationMenuKiril.insert(userConfirmationCancel)
##################################################################################################################################
adminConfirmationMenuKiril = InlineKeyboardMarkup(row_width = 1)
adminConfirmationPost = InlineKeyboardButton(text="🆗 Эълонни каналга жойлаш", callback_data = admin_confirmation_callback.new(item_name="post"))
adminConfirmationMenuKiril.insert(adminConfirmationPost)

adminConfirmationCancel = InlineKeyboardButton(text="❌ Бекор қилиш", callback_data = admin_confirmation_callback.new(item_name="cancel"))
adminConfirmationMenuKiril.insert(adminConfirmationCancel)
##################################################################################################################################
newAdsMenuKiril = InlineKeyboardMarkup(row_width = 1)
newAds = InlineKeyboardButton(text="Яна эълон бериш", callback_data = new_ads_callback.new(item_name="newAds"))
newAdsMenuKiril.insert(newAds)

deletePost = InlineKeyboardButton(text="Эълонни каналдан олиб ташлаш", callback_data = new_ads_callback.new(item_name="deletePost"))
newAdsMenuKiril.insert(deletePost)