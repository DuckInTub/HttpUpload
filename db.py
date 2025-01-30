import sqlite3
import hashlib
import hmac

# def init():
#     with sqlite3.connect("database.db") as db, db.cursor() as cur:

def validate_login(username : str, password : str):
    with sqlite3.connect("db.db") as db:
        cur = db.cursor()
        res = cur.execute("SELECT username, password FROM users WHERE username = ?", (username,))
        row = res.fetchone()
        if row is None:
            return False

        db_password_hash = row[1]
        with open("salt.txt", "rb") as file:
            calc_password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), file.read(), 500_000)

        
        return hmac.compare_digest(db_password_hash, calc_password_hash)


def add_user(username : str, password : str):
    with sqlite3.connect("db.db") as db:
        cur = db.cursor()

        with open("salt.txt", "rb") as file:
            password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), file.read(), 500_000)
        res = cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
        print(res)


if __name__ == "__main__":
    print(validate_login("Isak", "test"))
