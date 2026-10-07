import sqlite3
import os

os.makedirs('password_manager_db', exist_ok=True)
try:
    db = sqlite3.connect('password_manager_db/database.db')
    cursor = db.cursor()


    cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
        id integer primary key,
        website text,
        username text,
        password text
        )
        """)
    cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_website_username ON passwords(website, username)""")

    def add_password(website, username, password):
        try:
            cursor.execute("INSERT INTO passwords(website, username, password) VALUES(?, ?, ?)", (website, username, password))
            db.commit()
            return True
        except sqlite3.IntegrityError:
            return False


    def get_passwords():
        cursor.execute("SELECT * FROM passwords")
        passwords = cursor.fetchall()
        return passwords

    def search_password(website, username):
        cursor.execute("SELECT * FROM passwords WHERE website=? and username=?", (website, username))
        password = cursor.fetchall()
        return password
    def update_password(website, username, password):
        cursor.execute("UPDATE passwords SET password=? WHERE website=? AND username=?", (password, website, username))
        affected_rows = cursor.rowcount
        db.commit()
        return affected_rows

    def delete_password(website, username):
        cursor.execute("DELETE FROM passwords WHERE website=? and username = ? ", (website, username))
        affected_rows = cursor.rowcount
        db.commit()
        return affected_rows

    def close_database():
        db.close()

except sqlite3.Error as e:
    print(f"❌Помилка бази даних: {e}")
    exit()


