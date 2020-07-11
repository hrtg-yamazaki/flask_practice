import os
from pathlib import Path
import sqlite3


PROJECT_ROOT = Path("__file__").resolve().parents[0]
APP_ROOT = str(PROJECT_ROOT) + "/app/"
DB_PATH = APP_ROOT + "db/sample.sqlite"


os.chdir(PROJECT_ROOT)


def set_db():
    """
    データベースのセッティング
    """
    with open(DB_PATH, "a", encoding="utf-8"):
        pass


def set_table():
    """
    テーブルのセッティング
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("""\
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY, content TEXT
            )\
        """)
        conn.commit()
    except sqlite3.Error as e:
        print("Error occured." + str(e))
        exit()
    else:
        print("Table created.")
    finally:
        conn.close()


def main():
    """
    実行関数
    """
    set_db()
    set_table()


if __name__ == "__main__":
    main()