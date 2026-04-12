from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Споты и парки')],
        [KeyboardButton(text = 'Кроссовки'),
         KeyboardButton(text = 'Трюки')],
        [KeyboardButton(text = 'Комплектующие'),
         KeyboardButton(text = '=>')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Выбери пункт меню'
)

citys = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Обнинск', callback_data = 'city_обнинск')],
        [InlineKeyboardButton(text = 'Москва', callback_data = 'city_москва')],
        [InlineKeyboardButton(text = 'Сочи', callback_data = 'city_сочи')]
    ]
)

shoes = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Подешевле', callback_data = 'shoes_подешевле')],
        [InlineKeyboardButton(text = 'Покрасивее', callback_data = 'shoes_покрасивее')],
        [InlineKeyboardButton(text = 'Поживучее', callback_data = 'shoes_поживучее')]
    ]
)

comp = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Доски', callback_data = 'comp_доски')],
        [InlineKeyboardButton(text = 'Подвески', callback_data = 'comp_подвески')],
        [InlineKeyboardButton(text = 'Колеса', callback_data = 'comp_колеса')],
        [InlineKeyboardButton(text = 'Подшипники', callback_data = 'comp_подшипники')],
        [InlineKeyboardButton(text = 'Прочее', callback_data = 'comp_прочее')]
    ]
)

menu_shoes_low = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Lakai BRIGHTON')],
        [KeyboardButton(text = 'Назад')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Выбери бренд'
)

menu_shoes_nice = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'DS Manteca 4'),
        KeyboardButton(text = 'Vans SKATE HALF CAB')],
        [KeyboardButton(text = 'Назад')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Выбери бренд'
)

menu_shoes_strng = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Vans SK8 HI')],
        [KeyboardButton(text = 'Назад')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Выбери бренд'
)

menu_obn_spots = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Центральный парк'),
        KeyboardButton(text = 'Ступени на Сбере')],
        [KeyboardButton(text = 'Космос парк'),
         KeyboardButton(text = 'Назад')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Выбери бренд'
)

menu_2 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Погода сегодня')],
        [KeyboardButton(text = '<=')]
    ],
    resize_keyboard = True,
    input_field_placeholder = 'Выбери пункт меню'
)

weather_citys = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'В Обнинске', callback_data = 'weather_обнинск')],
        [InlineKeyboardButton(text = 'В Москве', callback_data = 'weather_москва')], 
        [InlineKeyboardButton(text = 'В Сочи', callback_data = 'weather_сочи')]
    ]
)