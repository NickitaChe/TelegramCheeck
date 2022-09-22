import sqlite3


def createSubs():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(f'CREATE TABLE subs('
                f'sub_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                f'user_id INTEGER,'
                f'isSubscribed BOOL'
                f')')


