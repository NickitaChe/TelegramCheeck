import sqlite3

from bot.database.methods.get import getSubscriber


def insertUser(message):
    """
    Создает нового юзера в БД
    :param message:
    :return:
    """
    try:
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}", "@{message.from_user.username}")')
        conn.commit()
    except Exception as e:
        print(e)
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}")')
        conn.commit()


def newSubscriber(message):
    if not getSubscriber(message):





        try:
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            cur.execute(f'INSERT INTO subs (user_id) VALUES("{message.from_user.id}")')
            conn.commit()
        except Exception as e:
            print(e)
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            cur.execute(f'INSERT INTO subs (user_id) VALUES("{message.from_user.id}")')
            conn.commit()