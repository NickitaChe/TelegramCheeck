import sqlite3

from aiogram import Dispatcher, types, md
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types.sticker import Sticker

from bot.database.methods.create import *
from bot.database.methods.get import *
from bot.database.methods.insert import *
from bot.database.methods.update import *

commandsList = ['start', 'check_language', "remove_keyboard", 'db_check', 'subscribe']
"""
Список всех команд
"""


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers0
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(check_language, commands=['check_language'])
    dp.register_message_handler(remove_keyboard, commands=['remove_keyboard'])
    dp.register_message_handler(db_check, commands=['db_check'])
    dp.register_message_handler(subscribe, commands=['subscribe'])
    dp.register_message_handler(unsubscribe, commands=['unsubscribe'])

    pass


def setupReplyKeyboardMarkup(message):
    '''
    Функция для стандартной настройки списка команд
    :param message:
    :return:
    '''
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in commandsList:
        button = KeyboardButton(str(f"/{item}"))
        if item == "subscribe":
            if getSubscriber(message):
                button = KeyboardButton(str(f"/unsubscribe"))
                greet_kb.add(button)
            else:
                greet_kb.add(button)
        else:
            greet_kb.add(button)
    return greet_kb


async def send_welcome(message: types.Message):
    """
    Функция вызывается при команде /start
    Даёт пользователю информацию о всех командах
    """

    if not checkUserExistence(message):
        insertUser(message)
        await message.reply(f'Привет, {message.from_user.username}, я тебя запомнил')

    greet_kb = setupReplyKeyboardMarkup(message)

    await message.reply_sticker(sticker=r"CAACAgIAAxkBAAEF519jLJpsTdvCUzbFIVY8NExZ7Bi38gACLAADj44DGvVlqVDAjmsRKQQ", reply_markup=greet_kb)


async def remove_keyboard(message: types.Message):
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


async def db_check(message: types.Message):
    pass


async def subscribe(message: types.Message):
    if getSubscriber(message):
        await message.answer("Вы уже подписанны на рассылку")
    else:
        newSubscriber(message)
        greet_kb = setupReplyKeyboardMarkup(message)
        await message.reply("Вы успешно подписались!")
        await message.answer_sticker(sticker=r"CAACAgQAAxkBAAEF54ljLKP6muJfb8I6vzwdUxTOQTKBVAACnxEAAqbxcR57wYUDyflSISkE", reply_markup=greet_kb)
    pass


async def unsubscribe(message: types.Message):
    if getSubscriber(message):
        userUnSubscribe(message)
        await message.answer("Вы успешно отписались")
        greet_kb = setupReplyKeyboardMarkup(message)
        await message.answer_sticker(
            sticker=r"CAACAgQAAxkBAAEF54tjLKc_6c41jJDxzVA4Hq333ugdpQACWRIAAqbxcR5xRKqTi3F9aSkE", reply_markup=greet_kb)
    else:
        await message.reply("Вы и так не подписаны, а стоило бы")
    pass