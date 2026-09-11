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

    def add_password(website, username, password):
        cursor.execute("INSERT INTO passwords(website, username, password) VALUES(?, ?, ?)", (website, username, password))
        db.commit()

    def get_passwords():
        cursor.execute("SELECT * FROM passwords")
        passwords = cursor.fetchall()
        return passwords
  
    def search_password(site, user):
        cursor.execute("SELECT * FROM passwords WHERE website=? and username=?", (site, user))
        password = cursor.fetchall()
        return password
    def update_password(website, username, password):
        cursor.execute("UPDATE passwords SET password=? WHERE website=? AND username=?", (password, website, username))
        rowc = cursor.rowcount
        db.commit()
        return rowc

    def delete_password(site, user):
        cursor.execute("DELETE FROM passwords WHERE website=? and username = ? ", (site, user))
        rowc = cursor.rowcount
        db.commit()
        return rowc

    def close_database():
        db.close()
    
except sqlite3.Error:
    print(f"❌Помилка підключення")
    exit()

                
            