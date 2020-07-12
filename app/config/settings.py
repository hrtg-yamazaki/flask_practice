import os
from pathlib import Path
import sqlite3
import string
import secrets


PROJECT_ROOT = Path("__file__").resolve().parents[0]

APP_ROOT = str(PROJECT_ROOT) + "/app/"
DB_PATH = os.path.join(APP_ROOT, "db/sample.sqlite")

CONFIG_DIR = str(APP_ROOT) + "/config/"
LOCAL_SETTINGS_PATH = os.path.join(CONFIG_DIR, "local_settings.py")

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
        print("The database for this project is ready.")
    finally:
        conn.close()


def set_secret():
    """
    local_settings.pyを作成して、自動でシークレットキーを生成する
    """
    if not os.path.exists(LOCAL_SETTINGS_PATH):
        letters = string.ascii_letters + string.digits
        secret_string = "".join(secrets.choice(letters) for letter in range(16))
        with open(LOCAL_SETTINGS_PATH, "w", encoding="utf-8") as f:
            f.write("SECRET_KEY = \"" + secret_string + "\"\n")
        print("The file \"local_settings.py\" is released.")
    else:
        print("The file \"local_settings.py\" is already created.")


def get_secret():
    """
    シークレットキーを取得
    """
    try:
        from .local_settings import SECRET_KEY
        secret_key = SECRET_KEY
    except ModuleNotFoundError as e:
        print(str(e))
        print("SECRET KEY is not found.")
        return None
    else:
        return secret_key


def main():
    """
    実行関数
    """
    set_db()
    set_table()
    set_secret()


if __name__ == "__main__":
    main()
