from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_dataLatin import new_second_callback, state_phone_callback, box_pass_callback, exchange_callback, look_callback, user_confirmation_callback, admin_confirmation_callback, new_ads_callback, write_forms_callback
import json

##################################################################################################################################
writeFormsMenuLatin = InlineKeyboardMarkup(row_width = 1)
write = InlineKeyboardButton(text="E`lonni yozib jo`natish", callback_data = write_forms_callback.new(item_name="write"))
writeFormsMenuLatin.insert(write)

forms = InlineKeyboardButton(text="E`lonni forma shaklida to`ldirish", callback_data = write_forms_callback.new(item_name="forms"))
writeFormsMenuLatin.insert(forms)

deletePost = InlineKeyboardButton(text="E`lonni kanaldan olib tashlash", callback_data = write_forms_callback.new(item_name="deletePost"))
writeFormsMenuLatin.insert(deletePost)
##################################################################################################################################
newSecondMenuLatin = InlineKeyboardMarkup(row_width = 1)
newPhone = InlineKeyboardButton(text="Telefon: Yangi", callback_data = new_second_callback.new(item_name="newPhone"))
newSecondMenuLatin.insert(newPhone)

secondHand = InlineKeyboardButton(text="Telefon: Ishlatilgan", callback_data = new_second_callback.new(item_name="secondHand"))
newSecondMenuLatin.insert(secondHand)
##################################################################################################################################
statePhoneMenuLatin = InlineKeyboardMarkup(row_width = 1)
statePhoneIdeal = InlineKeyboardButton(text="Telefon holati: A`lo(Ideal)", callback_data = state_phone_callback.new(item_name="A`lo(Ideal)"))
statePhoneMenuLatin.insert(statePhoneIdeal)

statePhoneNice = InlineKeyboardButton(text="Telefon holati: Yaxshi", callback_data = state_phone_callback.new(item_name="Yaxshi"))
statePhoneMenuLatin.insert(statePhoneNice)

statePhoneAverage = InlineKeyboardButton(text="Telefon holati: O`rta", callback_data = state_phone_callback.new(item_name="O`rta"))
statePhoneMenuLatin.insert(statePhoneAverage)

statePhoneBelowAverage = InlineKeyboardButton(text="Telefon holati: O`rtadan past", callback_data = state_phone_callback.new(item_name="O`rtadan past"))
statePhoneMenuLatin.insert(statePhoneBelowAverage)
##################################################################################################################################
boxPassPhoneMenuLatin = InlineKeyboardMarkup(row_width = 1)
boxYes = InlineKeyboardButton(text="Korobkasi, xujjati bor", callback_data = box_pass_callback.new(item_name="bor"))
boxPassPhoneMenuLatin.insert(boxYes)

boxNo = InlineKeyboardButton(text="yo`q, Pasport nusxa beriladi", callback_data = box_pass_callback.new(item_name="yo`q, Pasport nusxa beriladi"))
boxPassPhoneMenuLatin.insert(boxNo)
##################################################################################################################################
exchangePhoneMenuLatin = InlineKeyboardMarkup(row_width = 1)
exchangeYes = InlineKeyboardButton(text="Ayirboshlash(обмен) bor", callback_data = exchange_callback.new(item_name="yes"))
exchangePhoneMenuLatin.insert(exchangeYes)

exchangeNo = InlineKeyboardButton(text="Ayirboshlash(обмен) yo`q", callback_data = exchange_callback.new(item_name="no"))
exchangePhoneMenuLatin.insert(exchangeNo)

##################################################################################################################################
lookMenuLatin = InlineKeyboardMarkup(row_width = 1)
cancel = InlineKeyboardButton(text="E`lonni ko`rish", callback_data = look_callback.new(item_name="cancel"))
lookMenuLatin.insert(cancel)
##################################################################################################################################
userConfirmationMenuLatin = InlineKeyboardMarkup(row_width = 1)
userConfirmationPost = InlineKeyboardButton(text="🆗 E`lonni Adminga yuborish", callback_data = user_confirmation_callback.new(item_name="post"))
userConfirmationMenuLatin.insert(userConfirmationPost)

userConfirmationCancel = InlineKeyboardButton(text="❌ Bekor qilish", callback_data = user_confirmation_callback.new(item_name="cancel"))
userConfirmationMenuLatin.insert(userConfirmationCancel)
##################################################################################################################################
adminConfirmationMenuLatin = InlineKeyboardMarkup(row_width = 1)
adminConfirmationPost = InlineKeyboardButton(text="🆗 E`lonni kanalga joylash", callback_data = admin_confirmation_callback.new(item_name="post"))
adminConfirmationMenuLatin.insert(adminConfirmationPost)

adminConfirmationCancel = InlineKeyboardButton(text="❌ Bekor qilish", callback_data = admin_confirmation_callback.new(item_name="cancel"))
adminConfirmationMenuLatin.insert(adminConfirmationCancel)
##################################################################################################################################
newAdsMenuLatin = InlineKeyboardMarkup(row_width = 1)
newAds = InlineKeyboardButton(text="Yana e`lon berish", callback_data = new_ads_callback.new(item_name="newAds"))
newAdsMenuLatin.insert(newAds)

deletePost = InlineKeyboardButton(text="E`lonni kanaldan olib tashlash", callback_data = new_ads_callback.new(item_name="deletePost"))
newAdsMenuLatin.insert(deletePost)