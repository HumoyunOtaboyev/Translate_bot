from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="πΊπΏ Uzb - π¬π§ Eng"), KeyboardButton(text="π¬π§ Eng - πΊπΏ Uzb")],
        [KeyboardButton(text="πΊπΏ Uzb - π·πΊ Rus"), KeyboardButton(text="π·πΊ Rus - πΊπΏ Uzb")],
        [KeyboardButton(text="πΊπΏ Uzb - de German"), KeyboardButton(text="de German - πΊπΏ Uzb")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)