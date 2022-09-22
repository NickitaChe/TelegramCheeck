import sqlite3

from bot.database.methods.get import getSubscriber


def userUnSubscribe(message):
    if getSubscriber(message):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        cur.execute(f'DELETE FROM subs '
                    f'WHERE user_id = "{message.from_user.id}"')
        conn.commit()