from aiogram import Dispatcher, types, md
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

commandsList = ['start', 'check_language', "remove_keyboard"]
"""
Список всех команд
"""


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers0
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(check_language, commands=['check_language'])
    dp.register_message_handler(remove_keybord, commands=['remove_keyboard'])
    pass


async def send_welcome(message: types.Message):
    """
    Функция вызывается при команде /start
    Даёт пользователю информацию о всех командах
    """

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)

    for item in commandsList:
        button = KeyboardButton(str(f"/{item}"))
        greet_kb.add(button)

    await message.reply("Привет", reply_markup=greet_kb)

async def remove_keybord(message: types.Message):
    """
    Функция вызывается при команде /start
    Даёт пользователю информацию о всех командах
    """

    await message.reply("Убираю", reply_markup=ReplyKeyboardRemove())


async def check_language(message: types.Message):
    """
    Функция вызывается при команде /check_language
    Показывает информацию о локализации пользователя
    :param message:
    :return:
    """
    locale = message.from_user.locale

    await message.reply(md.text(
        md.bold('Info about your language:'),
        md.text('🔸', md.bold('Code:'), md.code(locale.language)),
        md.text('🔸', md.bold('Territory:'), md.code(locale.territory or 'Unknown')),
        md.text('🔸', md.bold('Language name:'), md.code(locale.language_name)),
        md.text('🔸', md.bold('English language name:'), md.code(locale.english_name)),
        sep='\n',
))