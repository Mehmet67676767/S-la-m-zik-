from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ArchMusic import app

def help_pannel(_, START: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["H_B_1"],
                callback_data="help_callback hb1",
            ),
            InlineKeyboardButton(
                text=_["H_B_2"],
                callback_data="help_callback hb2",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["H_B_3"],
                callback_data="help_callback hb3",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["H_B_4"],
                callback_data="help_callback hb4",
            ),
            InlineKeyboardButton(
                text=_["H_B_7"],
                callback_data="help_callback hb7",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ],
    ]

    return InlineKeyboardMarkup(buttons)


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons