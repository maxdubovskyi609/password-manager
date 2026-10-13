
from customtkinter import *
from PIL import Image
from database import PasswordDatabase


class PasswordManagerApp(CTk):
    BTN_COLOR = '#1E2736'
    BTN_BORDER = "#364051"
    DANGER_COLOR = "#660917"
    DANGER_BORDER = "#9C0017"
    FONT_TITLE = ('Segoe UI', 25, 'bold' )
    FONT_BTN = ("Segoe UI", 15, "bold")
    FONT = ("Arial", 16)
    

    def __init__(self):
        super().__init__()
        self.title('Password Manager')
        self.geometry('500x600')
        self.resizable(False, False)
        self.configure(fg_color='#121A27')
        set_appearance_mode('dark')
        self.grid_columnconfigure(0, weight=1)
        self.logo_img = CTkImage(light_image=Image.open('images/image.png'),
                         dark_image=Image.open('images/image.png'),
                         size=(100, 70)
                         )
        self.add_img = CTkImage(light_image=Image.open('images/add.png'),
                 dark_image=Image.open('images/add.png'),
                 size=(40, 40)
                 )

        self.watch_img = CTkImage(light_image=Image.open('images/watch.png'),
                         dark_image=Image.open('images/watch.png'),
                         size=(40, 40)
                         )
        self.find_img = CTkImage(light_image=Image.open('images/find.png'),
                        dark_image=Image.open('images/find.png'),
                         size=(40, 40)
                         )
        
        self.change_img = CTkImage(light_image=Image.open('images/change.png'),
                         dark_image=Image.open('images/change.png'),
                         size=(40, 40)
                         )
        
        self.delete_img = CTkImage(light_image=Image.open('images/delete.png'),
                         dark_image=Image.open('images/delete.png'),
                         size=(40, 40)
                         )
        
        self.leave_img = CTkImage(light_image=Image.open('images/leave.png'),
                         dark_image=Image.open('images/leave.png'),
                         size=(40, 40)
                         )
        self.db = PasswordDatabase()

        
        image_label = CTkLabel(self, image=self.logo_img, text='')
        image_label.grid(row=0, column=0, pady=(13, 7))
        title = CTkLabel(self, text='PASSWORD MANAGER ', font=('Segoe UI', 20, 'bold'))
        title.grid(row=1, column=0, pady=(0, 12))

    def main_button(self, text, image, command, row):
        btn = CTkButton(self,
                text=text,
                anchor='w',
                font=self.FONT_BTN,
                width=400, height=60,
                fg_color=self.BTN_COLOR,
                border_width=1, border_color=self.BTN_BORDER,
                image=image,
                command=command
                )
        btn.grid(row=row, column=0, pady=3)
        return btn

    def exit_app(self):
        self.db.close_database()
        self.destroy()

        
app = PasswordManagerApp()


class BaseWindow(CTkToplevel):
    def __init__(self, app, title, width, height):
        super().__init__(app)
        self.app = app
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)


def entry(window, placeholder, row):
    entry_field = CTkEntry(window, width=310, height=55, placeholder_text=placeholder, font=PasswordManagerApp.FONT)
    entry_field.grid(row=row, column=0, pady=5)
    return entry_field

def second_button(master, text, command, row, pady):
    btn = CTkButton(master=master, text=text, width=210, height=55, font=PasswordManagerApp.FONT, command=command)
    btn.grid(row=row, column=0, pady=pady)
    return btn

# ФУНКЦІЇ

class AddWindow(BaseWindow):
    def __init__(self, app, title, width, height):
        super().__init__(app, title, width, height)

        self.title_label = CTkLabel(self, text = 'Add Password', font=PasswordManagerApp.FONT_TITLE )
        self.title_label.grid(row=0, column=0, pady=(15, 15))

        self.website_entry = entry(self, 'Website', row=1 )
        self.login_entry = entry(self, 'Login', row=2)
        self.password_entry = entry(self, 'Password', row=3)
    
        self.message_label = CTkLabel(self, text='', font=PasswordManagerApp.FONT)
        self.message_label.grid(row=5, column=0, pady=(10, 0))

        second_button(master=self, text='Add', command=self.on_add_click, row=4, pady=(30, 0))
        

    def on_add_click(self):
        website = self.website_entry.get().strip()
        login = self.login_entry.get().strip()
        password = self.password_entry.get().strip()
        if not website or not login or not password:
            self.message_label.configure(text='Please fill in all fields!')

        else:
            added = self.app.db.add_password(website, login, password)
            if added:
                self.website_entry.delete(0, 'end')
                self.login_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.message_label.configure(text='Password added successfully!✅')
            else:
                self.message_label.configure(text='This account already exists❌')



class ViewWindow(BaseWindow):
    FG_COLOR = '#242424'
    def __init__(self, app, title, width, height):
        super().__init__(app, title, width, height)
        self.configure(fg_color=self.FG_COLOR)
        self.title_label = CTkLabel(self, text='Passwords', font=PasswordManagerApp.FONT_TITLE)
        self.title_label.grid(row=0, column=0)
    
        self.line = CTkLabel(self, text='_____________________________________________________________', anchor='n' )
        self.line.grid(row=1, column=0, sticky='n')
    
        self.scroll_frame = CTkScrollableFrame(self, width=350, height=350, fg_color=self.FG_COLOR)
        self.scroll_frame.grid(row=2, column=0)
        self.scroll_frame.grid_columnconfigure(0, weight=1)


        self.passwords = self.app.db.get_passwords()
        if self.passwords:
            for index, row in enumerate(self.passwords):
                password_label = CTkLabel(self.scroll_frame, text=f"Website: {row[1]} \nLogin: {row[2]}\nPassword: {row[3]}\n", font=('San Francisco', 21), anchor='w', justify='left')
                password_label.grid(row=index, column=0, sticky='w')
        
        else:
            no_passwords_label = CTkLabel(self.scroll_frame, text='No passwords found')
            no_passwords_label.grid(row=0, column=0)


class FindWindow(BaseWindow):
    def __init__(self, app, title, width, height):
        super().__init__(app, title, width, height)
        self.title_label = CTkLabel(self, text = 'Find Password', font=PasswordManagerApp.FONT_TITLE )
        self.title_label.grid(row=0, column=0, pady=(15, 15))
    
        self.website_entry = entry(self, 'Website', row=1)
        self.login_entry = entry(self, 'Login', row=2)

        self.password_textbox = CTkTextbox(self, width=200, height=40, font=('Arial', 25), )
        self.message_label = CTkLabel(self, text='', font=PasswordManagerApp.FONT)
        self.message_label.grid(row=5, column=0, pady=(10, 0))

        second_button(master=self, text='Search', command=self.on_find_click, row=3, pady=20)
        
        self.password_textbox.configure(state='disabled')
        self.password_textbox.grid(row=4, column=0)

    def on_find_click(self):
        website = self.website_entry.get().strip()
        login = self.login_entry.get().strip()

        if not website or not login:
            self.message_label.configure(text='Please fill in all fields!')
            return
        result = self.app.db.search_password(website, login)
        if result:
            self.website_entry.delete(0, 'end')
            self.login_entry.delete(0, 'end')
            self.password_textbox.configure(state='normal')
            self.password_textbox.delete('0.0', 'end')
            self.password_textbox.insert('0.0', result[0][3])
            self.password_textbox.configure(state='disabled')
            self.message_label.configure(text='')
        else:
            self.website_entry.delete(0, 'end')
            self.login_entry.delete(0, 'end')
            self.password_textbox.configure(state='normal')
            self.password_textbox.delete('0.0', 'end')
            self.password_textbox.insert('0.0', 'Not found')
            self.password_textbox.configure(state='disabled')
            self.message_label.configure(text='')


class ChangeWindow(BaseWindow):
    def __init__(self, app, title, width, height):
        super().__init__(app, title, width, height)
        self.title_label = CTkLabel(self, text = 'Change Password', font=PasswordManagerApp.FONT_TITLE )
        self.title_label.grid(row=0, column=0, pady=(15, 15))
    
        self.website_entry = entry(self, 'Website', row=1)
        self.login_entry = entry(self, 'Login', row=2)
        self.new_password_entry = entry(self, 'New Password', row=3)
    
        self.message_label = CTkLabel(self, text='', font=PasswordManagerApp.FONT)
        self.message_label.grid(row=5, column=0) 

        second_button(master=self, text='Change', command=self.on_change_click, row=4, pady=20)

    def on_change_click(self):
        website = self.website_entry.get().strip()
        login = self.login_entry.get().strip()
        password = self.new_password_entry.get().strip()
        if not website or not login or not password:
            self.message_label.configure(text='Please fill in all fields!')
            return
        affected_rows = self.app.db.update_password(website, login, password)
        if affected_rows > 0:
            self.message_label.configure(text='Password changed✅')
        else:
            self.message_label.configure(text='Account not found❌')
        self.website_entry.delete(0, 'end')
        self.login_entry.delete(0, 'end')
        self.new_password_entry.delete(0, 'end')   


class DeleteWindow(BaseWindow):
    def __init__(self, app, title, width, height):
        super().__init__(app, title, width, height)
        self.title_label = CTkLabel(self, text = 'Delete Password', font=PasswordManagerApp.FONT_TITLE )
        self.title_label.grid(row=0, column=0, pady=(15, 15))
    
        self.website_entry = entry(self, 'Website', row=1)
        self.login_entry = entry(self, 'Login', row=2)
    
        self.message_label = CTkLabel(self, text='', font=PasswordManagerApp.FONT)
        self.message_label.grid(row=4, column=0)

        second_button(master=self, text='Delete', command=self.on_delete_click, row=3, pady=20)

    def on_delete_click(self):
        website = self.website_entry.get().strip()
        login = self.login_entry.get().strip()
        if not website or not login:
            self.message_label.configure(text='Please fill in all fields!')
            return
        affected_rows = self.app.db.delete_password(website, login)
        if affected_rows > 0:
            self.message_label.configure(text='Password deleted✅')
        else:
            self.message_label.configure(text='Password not found❌')

        self.website_entry.delete(0, 'end')
        self.login_entry.delete(0, 'end')




# КНОПКИ
add_btn = app.main_button('Add Password', image=app.add_img, command=lambda: AddWindow(app, 'Add Password', width=370, height=380), row=2)
watch_btn = app.main_button('View Passwords', image=app.watch_img, command=lambda: ViewWindow(app, 'View Passwords', width=350, height=400 ), row=3)
find_btn = app.main_button('Find Password', image=app.find_img, command=lambda: FindWindow(app, 'Find Password', width=370, height=380 ), row=4)
change_btn = app.main_button('Change Password', image=app.change_img, command=lambda: ChangeWindow(app, 'Change Password', width=370, height=380), row=5)
delete_btn = app.main_button('Delete Password', image=app.delete_img, command=lambda: DeleteWindow(app, 'Delete Password', width=370, height=320), row=6)
leave_btn = CTkButton(app, text='Exit', font=PasswordManagerApp.FONT_BTN, width=400, height=60, fg_color=PasswordManagerApp.DANGER_COLOR, border_width=1, border_color=PasswordManagerApp.DANGER_BORDER, hover_color="#850B1C", image=app.leave_img, command=app.exit_app)
leave_btn.grid(row=7, column=0, pady=40)

app.mainloop()