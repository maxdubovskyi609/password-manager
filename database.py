import sqlite3
import os

class PasswordDatabase:
    def __init__(self):
        os.makedirs('password_manager_db', exist_ok=True)
        try:
            self.db = sqlite3.connect('password_manager_db/database.db')
            self.cursor = self.db.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
                    id integer primary key,
                    website text,
                    username text,
                    password text
                    )
                    """)
            self.cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_website_username ON passwords(website, username)""")
        except sqlite3.Error as e:
            print(f"❌Помилка бази даних: {e}")
            exit()


   
    
    def add_password(self, website, username, password):
        try:
            self.cursor.execute("INSERT INTO passwords(website, username, password) VALUES(?, ?, ?)", (website, username, password))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False


    def get_passwords(self):
        self.cursor.execute("SELECT * FROM passwords")
        passwords = self.cursor.fetchall()
        return passwords

    def search_password(self, website, username):
        self.cursor.execute("SELECT * FROM passwords WHERE website=? and username=?", (website, username))
        password = self.cursor.fetchall()
        return password
    def update_password(self, website, username, password):
        self.cursor.execute("UPDATE passwords SET password=? WHERE website=? AND username=?", (password, website, username))
        affected_rows = self.cursor.rowcount
        self.db.commit()
        return affected_rows

    def delete_password(self, website, username):
        self.cursor.execute("DELETE FROM passwords WHERE website=? and username = ? ", (website, username))
        affected_rows = self.cursor.rowcount
        self.db.commit()
        return affected_rows

    def close_database(self):
        self.db.close()




