from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Smartfonlar"),
            KeyboardButton(text="Notebooklar"),
            KeyboardButton(text="Maishiy texnika"),
        ]
    ],
    resize_keyboard=True
)
menuNotebook = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="HP"),
             KeyboardButton(text="Mackbook"),
             KeyboardButton(text="Asus"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuPhone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Samsung"),
            KeyboardButton(text="Apple"),
            KeyboardButton(text="Redmi"),
            KeyboardButton(text="OPPO"),
        ],
        [
            KeyboardButton(text="VIVO"),
            KeyboardButton(text="Realmi"),
            KeyboardButton(text="Huawei"),
            KeyboardButton(text="Pocco"),
                ],
            ],



    resize_keyboard=True
)
menuZakazBerish2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact",request_contact=True),
            KeyboardButton(text="Location",request_location=True),
            KeyboardButton(text="Bosh Menu🏠")
        ],
    ],
    resize_keyboard=True
)
menuZakazBerish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact",request_contact=True),
        ],
    ],
    resize_keyboard=True
)
menuZakazBerish1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location",request_location=True)
        ],
    ],
    resize_keyboard=True
)
menuzakaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakaz",callback_data="Zakaz"),
            InlineKeyboardButton(text="Orqaga👈",callback_data="Orqaga👈"),
            InlineKeyboardButton(text="Bosh Menu🏠",callback_data="Bosh Menu🏠")
        ]
    ]
)

