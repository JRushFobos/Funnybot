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
        InlineKeyboardButton("🐈 Новая кошка", callback_data="new_cat"),
        InlineKeyboardButton("🐕 Новая собака", callback_data="new_dog"),
    ],
    [InlineKeyboardButton("Назад", callback_data="return")],
]
