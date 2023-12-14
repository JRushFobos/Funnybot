from telegram import InlineKeyboardButton


main_menu_buttons = [
    [
        InlineKeyboardButton("🖼️ Картинки", callback_data="pictures"),
    ],
    [
        InlineKeyboardButton("😂 Приколы", callback_data="jokes"),
    ],
    [
        InlineKeyboardButton("✍️ Стихи", callback_data="verse"),
    ],
    [
        InlineKeyboardButton("📺 Видео", callback_data="video"),
    ],
]

pictures_buttons = [
    [
        InlineKeyboardButton("🐈 Кошки", callback_data="new_cat"),
        InlineKeyboardButton("🐕 Собаки", callback_data="new_dog"),
        InlineKeyboardButton("🎮 Игры", callback_data="new_game"),
    ],
    [
        InlineKeyboardButton("🌳 Природа", callback_data="new_nature"),
        InlineKeyboardButton("😱 Случайная", callback_data="random"),
        InlineKeyboardButton("Назад", callback_data="return")
    ],
]
