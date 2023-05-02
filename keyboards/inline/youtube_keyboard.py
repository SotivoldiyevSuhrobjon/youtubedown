from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def choose_size(data):
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        *[InlineKeyboardButton(f"{item[0]} / {item[-1]}  | {item[1]}", callback_data=f"size:{item[0]}") for item in data]
        # InlineKeyboardButton(f"360   |  {past}", callback_data="size:past"),
    )
    return btn
