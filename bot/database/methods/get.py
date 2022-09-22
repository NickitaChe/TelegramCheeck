import sqlite3


def checkUserExistence(message):
    """
    Проверка на наличие пользователя в БД
    :param message:
    :return: True -Да, False -Нет
    """

    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"')
    result = cur.fetchall()

    if len(result) > 0:
        return True
    else:
        return False


def getAllUsers(message):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM users GROUP BY user_id')
    result = cur.fetchall()
    print(result)
    return result


def getSubscriber(message):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM subs WHERE user_id = "{message.from_user.id}"')
    result = cur.fetchall()

    if len(result) > 0 and result[0][2] == 1:
        return True
    else:
        return False

