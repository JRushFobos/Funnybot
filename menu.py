from telegram import InlineKeyboardButton


main_menu_buttons = [
    [
        InlineKeyboardButton("🖼️ Картинки", callback_data="pictures"),
    ],
    [
        InlineKeyboardButton("😂 Приколы", callback_data="jokes"),
    ],
    [
        InlineKeyboardButton("✍️ Стихи", callback_data="poems"),
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
        InlineKeyboardButton("🔙 Назад", callback_data="return"),
    ],
]

jokes_buttons = [
    [
        InlineKeyboardButton("🤣 Анекдоты", callback_data="new_anek"),
        InlineKeyboardButton("🔙 Назад", callback_data="return"),
    ],
]

poems_buttons = [
    [
        InlineKeyboardButton("🧓 Александр Пушкин", callback_data="Pushkin"),
        InlineKeyboardButton("🧓 Михаил Лермонтов", callback_data="Lermontov"),
    ],
    [
        InlineKeyboardButton("🧓 Иван Крылов", callback_data="Krilov"),
        InlineKeyboardButton("👵 Анна Ахматова", callback_data="Ahmatova"),

    ],
    [
        InlineKeyboardButton("🧓 Николай Заболоцкий", callback_data="Zabolockiy"),
        InlineKeyboardButton("👵 Агния Барто", callback_data="Barto"),],
    [
        InlineKeyboardButton("🧓 Корней Чуковский", callback_data="Chukovskiy"),
        InlineKeyboardButton("🧓 Алексей К. Толстой", callback_data="Tolstoy"),

    ],
    [
        InlineKeyboardButton("🧓 Василий Жуковский", callback_data="Zhukovskiy"),
        InlineKeyboardButton("🧓 Корней Чуковский", callback_data="Chukovskiy"),
    ],
    [
        InlineKeyboardButton("🧓 Алексей К. Толстой", callback_data="Tolstoy"),
        InlineKeyboardButton("🧓 Василий Жуковский", callback_data="Zhukovskiy"),
    ],
    [
        InlineKeyboardButton("🔙 Назад", callback_data="return"),
    ]
]

video_buttons = [
    [
        InlineKeyboardButton("🤣 YouTube видео", callback_data="youtube"),
        InlineKeyboardButton("🔙 Назад", callback_data="return"),
    ],
]
