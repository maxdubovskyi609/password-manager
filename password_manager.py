from customtkinter import *
from PIL import Image
from database import add_password, close_database, get_passwords, update_password, search_password, delete_password

# СТВОРЕННЯ ВІКНА
root = CTk()
root.title('Password Manager')
root.geometry('500x600')
root.resizable(False, False)
root.configure(fg_color='#121A27')
set_appearance_mode('dark')
root.grid_columnconfigure(0, weight=1)


BTN_COLOR = '#1E2736'
BTN_BORDER = "#364051"
DANGER_COLOR = "#660917"
DANGER_BORDER = "#9C0017"

FONT_TITLE = ('Segoe UI', 25, 'bold' )
FONT_BTN = ("Segoe UI", 15, "bold")
FONT = ("Arial", 16)


# ЗОБРАЖЕННЯ
image = CTkImage(light_image=Image.open('images/image.png'),
                 dark_image=Image.open('images/image.png'),
                 size=(100, 70)
                 )
add_img = CTkImage(light_image=Image.open('images/add.png'),
                 dark_image=Image.open('images/add.png'),
                 size=(40, 40)
                 )

watch_img = CTkImage(light_image=Image.open('images/watch.png'),
                 dark_image=Image.open('images/watch.png'),
                 size=(40, 40)
                 )
find_img = CTkImage(light_image=Image.open('images/find.png'),
                 dark_image=Image.open('images/find.png'),
                 size=(40, 40)
                 )

change_img = CTkImage(light_image=Image.open('images/change.png'),
                 dark_image=Image.open('images/change.png'),
                 size=(40, 40)
                 )

delete_img = CTkImage(light_image=Image.open('images/delete.png'),
                 dark_image=Image.open('images/delete.png'),
                 size=(40, 40)
                 )

leave_img = CTkImage(light_image=Image.open('images/leave.png'),
                 dark_image=Image.open('images/leave.png'),
                 size=(40, 40)
                 )

def entry(window, placeholder, row):
    entry = CTkEntry(window, width=310, height=55, placeholder_text=placeholder, font=FONT)
    entry.grid(row=row, column=0, pady=5)
    return entry
def main_button(text, image, command, row):
    btn = CTkButton(root,
                    text=text,
                    anchor='w',
                    font=FONT_BTN,
                    width=400, height=60,
                    fg_color=BTN_COLOR,
                    border_width=1, border_color=BTN_BORDER,
                    image=image,
                    command=command
                    )
    btn.grid(row=row, column=0, pady=3)
    return btn
def second_button(master, text, command, row, pady):
    btn = CTkButton(master=master, text=text, width=210, height=55, font=FONT, command=command)
    btn.grid(row=row, column=0, pady=pady)
    return btn

def create_window(title, width, height, ):
    window = CTkToplevel(root)
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.resizable(False, False)
    window.grid_columnconfigure(0, weight=1)
    return window

# ФУНКЦІЇ
def add_window():
    window = create_window('Add Password', width=370, height=380)
    
    title = CTkLabel(window, text = 'Add Password', font=FONT_TITLE )
    title.grid(row=0, column=0, pady=(15, 15))
 
    website_entry = entry(window, 'Website', row=1 )
    login_entry = entry(window, 'Login', row=2)
    password_entry = entry(window, 'Password', row=3)
    
    message_label = CTkLabel(window, text='', font=FONT)
    message_label.grid(row=5, column=0, pady=(10, 0))
    
    def save_password():
        website = website_entry.get().strip()
        login = login_entry.get().strip()
        password = password_entry.get().strip()
        if not website or not login or not password:
            message_label.configure(text='Please fill in all fields!')
        else:
            add_password(website, login, password)
            website_entry.delete(0, 'end')
            login_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            message_label.configure(text='Password added successfully!✅')
        
    second_button(master=window, text='Add', command=save_password, row=4, pady=(30, 0))
 
 
def view_passwords():
    FG_COLOR = '#242424'
    window = create_window('View Passwords', width=350, height=400)
    window.configure(fg_color=FG_COLOR)

    title = CTkLabel(window, text='Passwords', font=FONT_TITLE)
    title.grid(row=0, column=0)
    
    line = CTkLabel(window, text='_____________________________________________________________', anchor='n' )
    line.grid(row=1, column=0, sticky='n')
    
    scroll_frame = CTkScrollableFrame(window, width=350, height=350, fg_color=FG_COLOR)
    scroll_frame.grid(row=2, column=0)
    scroll_frame.grid_columnconfigure(0, weight=1)
    
    passwords = get_passwords()
    if passwords:
        for password in passwords:
            password_label = CTkLabel(scroll_frame, text=f"Website: {password[1]} \nLogin: {password[2]}\nPassword: {password[3]}\n", font=('San Francisco', 21), anchor='w', justify='left')
            password_label.grid(row=password[0], column=0, sticky='w')
            
    else:
        pass_lbl = CTkLabel(scroll_frame, text='No passwords found')
        pass_lbl.grid(row=0, column=0)
        
        
def find_window():
    window = create_window('Find Password', width=370, height=380)
    
    title = CTkLabel(window, text = 'Find Password', font=FONT_TITLE )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = entry(window, 'Website', row=1)
    login_entry = entry(window, 'Login', row=2)
    
    
    password_textbox = CTkTextbox(window, width=200, height=40, font=('Arial', 25), )
    
    def find_password():
        website = website_entry.get().strip()
        user = login_entry.get().strip()
        
        password = search_password(website, user)

        if password:
            password_textbox.configure(state='normal')
            password_textbox.delete('0.0', 'end')
            password_textbox.insert('0.0', password[0][3])
            password_textbox.configure(state='disabled')
        else:
            password_textbox.configure(state='normal')
            password_textbox.delete('0.0', 'end')
            password_textbox.insert('0.0', 'Not found')
            password_textbox.configure(state='disabled')
            
    second_button(master=window, text='Search', command=find_password, row=3, pady=20)

    password_textbox.configure(state='disabled')
    password_textbox.grid(row=4, column=0)
    
    
def change_window():
    window = create_window('Change Password', width=370, height=380)
    
    title = CTkLabel(window, text = 'Change Password', font=FONT_TITLE )
    title.grid(row=0, column=0, pady=(15, 15))

    website_entry = entry(window, 'Website', row=1)
    login_entry = entry(window, 'Login', row=2)
    new_password_entry = entry(window, 'New Password', row=3)
    
    message_label = CTkLabel(window, text='', font=FONT)
    message_label.grid(row=5, column=0)
    
    def change_password():
        website = website_entry.get().strip()
        login = login_entry.get().strip()
        password = new_password_entry.get().strip()
        rowc = update_password(website, login, password)
        if rowc > 0:
            message_label.configure(text='Password changed✅')
            
        else:
            message_label.configure(text='Account not found❌')
            
            
        website_entry.delete(0, 'end')
        login_entry.delete(0, 'end')
        new_password_entry.delete(0, 'end')
        
    second_button(master=window, text='Change', command=change_password, row=4, pady=20)
    
    
def delete_window():
    window = create_window('Delete Password', width=370, height=320)
    
    title = CTkLabel(window, text = 'Delete Password', font=FONT_TITLE )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = entry(window, 'Website', row=1)
    login_entry = entry(window, 'Login', row=2)
    
    message_label = CTkLabel(window, text='', font=FONT)
    message_label.grid(row=4, column=0)

    def delete_password1():
        website = website_entry.get().strip()
        login = login_entry.get().strip()
        rowc = delete_password(website, login)
        if rowc > 0:
            message_label.configure(text='Password deleted✅')
        else:
            message_label.configure(text='Password not found❌')
            
        website_entry.delete(0, 'end')
        login_entry.delete(0, 'end')
    
    second_button(master=window, text='Delete', command=delete_password1, row=3, pady=20)

def exit():
    close_database()
    root.destroy()
        
   
    
    

image_label = CTkLabel(root, image=image, text='')
image_label.grid(row=0, column=0, pady=(13, 7))

title = CTkLabel(root, text='PASSWORD MANAGER ', font=('Segoe UI', 20, 'bold'))
title.grid(row=1, column=0, pady=(0, 12))



# КНОПКИ
add_btn = main_button('Add Password', image=add_img, command=add_window, row=2)
watch_btn = main_button('View Passwords', image=watch_img, command=view_passwords, row=3)
find_btn = main_button('Find Password', image=find_img, command=find_window, row=4)
change_btn = main_button('Change Password', image=change_img, command=change_window, row=5)
delete_btn = main_button('Delete Password', image=delete_img, command=delete_window, row=6)

leave_btn = CTkButton(root, text='Exit', font=FONT_BTN, width=400, height=60, fg_color=DANGER_COLOR, border_width=1, border_color=DANGER_BORDER, hover_color="#850B1C", image=leave_img, command=exit)
leave_btn.grid(row=7, column=0, pady=40)


root.mainloop()