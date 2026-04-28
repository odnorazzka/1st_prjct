import logging
import requests
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart

import photos as pts

from shoes import shoes_data
from weather import weather_data

import keyboards as kb

user = Router()

WEATHER_API_KEY = '377af60e0f6537715e8191a54a8b251b'
WEATHER_URL = 'http://api.openweathermap.org/'

logging.basicConfig(level=logging.INFO)


@user.message(CommandStart())
async def cmd_start(message: Message,):
    await message.answer('Привет чювак',
                         reply_markup = kb.menu)


@user.callback_query(F.data.startswith('comp_'))
async def check_shoes(callback: CallbackQuery):
    comp_name = callback.data.split('_')[1]
    await callback.answer(f'Ты выбрал категорию «{comp_name.capitalize()}».\nРекомендации комплектующих пока в разработке, но первые делати совсем скоро появяится!', show_alert = True)
    await callback.message.answer(f'Ты выбрал категорию «{comp_name.capitalize()}»')


@user.message(F.text == 'Споты и парки')
async def msg_spots(message: Message):
    await message.answer('Выбери город',
                         reply_markup = kb.citys)
    

@user.message(F.text == 'Кроссовки')
async def msg_shoes(message: Message):
    await message.answer('Выбери категорию кроссовок',
                         reply_markup = kb.shoes)
    

@user.message(F.text == 'Трюки')
async def msg_tricks(message: Message ):
    #await message.answer(f'<b>Что-то</b>\n<strong>Что-то</strong>\n<i>Что-то</i>\n<em>Что-то</em>\n<u>Что-то</u>', parse_mode = 'HTML')
    await message.answer("Привет! Вот ссылка на <a href='https://www.google.com'>Google</a>", parse_mode='HTML')


@user.message(F.text == 'Комплектующие')
async def msg_comp(message: Message):
    await message.answer('Выбери категорию комплектующих',
                         reply_markup = kb.comp)
    

@user.message(F.text == '=>')
async def msg_next(message: Message):
    await message.answer('2 страница',
                         reply_markup = kb.menu_2)


# Выбор бодборки [
@user.callback_query(F.data == 'shoes_подешевле')
async def msg_Obn_SP_cyal(callback: CallbackQuery):
    await callback.answer(f'Подешевле',
                          reply_markup = ReplyKeyboardRemove())
    await callback.message.answer(f'Кроссовки с низким прайсом',
                                  reply_markup = kb.menu_shoes_low)

@user.callback_query(F.data == 'shoes_покрасивее')
async def cb_steps(callback: CallbackQuery):
    await callback.answer(f'Покрасивее',
                          reply_markup = ReplyKeyboardRemove())
    await callback.message.answer(f"Кроссовки lookin' fresh lookin' good type",
                                  reply_markup = kb.menu_shoes_nice)

@user.callback_query(F.data == 'shoes_поживучее')
async def cb_cosmos(callback: CallbackQuery):
    await callback.answer(f'Поживучее',
                          replu_markup = ReplyKeyboardRemove())
    await callback.message.answer(f'Прочные на износ кроссовки',
                                 reply_markup = kb.menu_shoes_strng)
# ] 


# Описание кроссовок [
@user.message(F.text.in_({'Vans SK8 HI', 'DS Manteca 4', 'Vans SKATE HALF CAB', 'Lakai BRIGHTON'}))
async def brends_shoes(message: Message):
    model_name = message.text
    data = shoes_data.get(model_name)
    if not data:
        await message.answer("Информация о модели не найдена.")
        return
    
    shoe_name = model_name
    shoe_description = data.get("description", "Описание отсутствует.")
    shoe_prices = data.get("prices", {})
    shoe_photo = data.get("photo", None)

    lines = [f"<b>{shoe_name}</b>", shoe_description, "", "<b>Цены:</b>"]
    for shop, price in shoe_prices.items():
        lines.append(f"{shop}: {price}")
    shoe_caption = "\n".join(lines)
    await message.answer_photo(photo = shoe_photo, caption = shoe_caption, parse_mode="HTML")
# ]


# Выбор города [
@user.callback_query(F.data == 'city_обнинск')
async def msg_Obn_SP_cyal(callback: CallbackQuery):
    await callback.answer(f'Обнинск',
                          reply_markup = ReplyKeyboardRemove())
    await callback.message.answer(f'Споты в городе Обниск',
                                  reply_markup = kb.menu_obn_spots)

@user.callback_query(F.data == 'city_москва')
async def cb_steps(callback: CallbackQuery):
    await callback.answer(f'Споты для этого города еще в разработке', show_alert = True)

@user.callback_query(F.data == 'city_сочи')
async def cb_cosmos(callback: CallbackQuery):
    await callback.answer(f'Споты для этого города еще в разработке', show_alert = True)
# ]


# Споты в обне [
@user.message(F.text == 'Центральный парк')
async def msg_Obn_SP_cyal(message: Message):
    await message.answer_photo( photo = pts.photo_Obn_SP_cyal, caption = '<b>Скейт-парк на Циалковском</b>\n<i>Много самокатеров,</i> парк находится прямо <i>под солнцем,</i> поэтому в особенно жаркие дни сложно там находиться. '
                               'А сам по себе парк, судя по всему, проектировался в первую очередь <i>для самокатеров,</i> что может повлиять на скорость прогресса у начинающих скейтеров.\n\n'
    '<a href = "https://yandex.com/maps/org/skeytpark_pamptrek/171117802398?si=dmevhap4f6q5x3z0p80t123v04">Показать на карте</a>', parse_mode = 'HTML')

@user.message(F.text == 'Ступени на Сбере')
async def msg_Obn_strs_sber(message: Message):
    await message.answer_photo( photo = pts.photo_Obn_stairs_sber, caption = '<b>Сбер-ступы</b>\n7 и 8 ступеней на крыльце Сбера на проспекте Маркса. '
                               'Довольно <i>неприятный уезд</i> по плитке и, скорее всего, могут легко <i>прогнать.</i> Но в то же время это <i>единственные</i> ступени подобного рода в Обнинске\n\n'
    '<a href = "https://yandex.com/maps/org/sberbank/197847257602?si=dmevhap4f6q5x3z0p80t123v04">Показать на карте</a>', parse_mode = 'HTML')

@user.message(F.text == 'Космос парк')
async def msg_Obn_SP_kosm(message: Message):
    await message.answer_photo( photo = pts.photo_Obn_SP_kosm, caption = '<b>Скейт-парк в ЖК «Космос».</b>\n'
                               'Обычно, <i>охрана не впускает</i> туда простой люд, но если быть находчивым или ловким, то найдешь выход из любой ситуации.\n\n'
    '<a href = "https://yandex.com/maps/org/kosmos_2_0/102449106739?si=dmevhap4f6q5x3z0p80t123v04">Показать на карте</a>', parse_mode = 'HTML')
# ]


# Погода в городе ... [
@user.message(F.text == 'Погода сегодня')
async def msg_weather(message: Message):
    await message.answer('Где показать сегодняшнюю погоду?',
                         reply_markup = kb.weather_citys)

@user.callback_query(F.data.startwith('weather_'))
async def chek_weather_city(callback: CallbackQuery):
    weather_city_name = callback.data.split('_')[1]
    await callback.answer(f'Ты хочешь узнать какая сейчас погода в городе {weather_city_name.capitalize()}?\nПогоди немного, я все еще работаю над этой функции', show_alert = True)
    await callback.message.answer(f'Ты хочешь узнать погоду в городе {weather_city_name.capitalize()}')
# ]


@user.message(F.text.in_(['Назад', '<=']))
async def msg_shoes_bck(message: Message):
    await message.answer(f'Главное меню',
                  reply_markup = kb.menu)   


@user.message(F.voice)
async def msg_voice(message: Message):
    await message.answer("И как я по-твоему должен отвечать на гс?")    


@user.message()
async def echo(message: Message ):
    await message.send_copy(chat_id = message.from_user.id)