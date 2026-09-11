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

# ФУНКЦІЇ
def add_window():
    window  = CTkToplevel(root)
    window.title('Add Password')
    window.geometry('370x380')
    window.grid_columnconfigure(0, weight=1)
    
    title = CTkLabel(window, text = 'Add Password', font=( 'Sergoe UI', 25, 'bold' ) )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = CTkEntry(window, width=310, height=55, placeholder_text='Website', font=('Arial', 16))
    website_entry.grid(row=1, column=0, pady=5)

    login_entry = CTkEntry(window, width=310, height=55, placeholder_text='Login', font=('Arial', 16))
    login_entry.grid(row=2, column=0, pady=5)
        
    password_entry = CTkEntry(window, width=310, height=55, placeholder_text='Password', font=('Arial', 16))
    password_entry.grid(row=3, column=0, pady=5)
    
    message_label = CTkLabel(window, text='', font=('Sergoe UI', 14))
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
        
    add_btn = CTkButton(window, text='Add', width=210, height=55, font=('Sergoe UI', 16), command=save_password)
    add_btn.grid(row=4, column=0, pady=(30, 0))

def view_passwords():
    window = CTkToplevel(root)
    window.title('View Passwords')
    window.geometry('350x400')
    window.resizable(False, False)
    window.configure(fg_color='#182232')
    window.grid_columnconfigure(0, weight=1)
    
    title = CTkLabel(window, text='Passwords', font=('Segoe UI', 25, 'bold'))
    title.grid(row=0, column=0)
    
    line = CTkLabel(window, text='_____________________________________________________________', anchor='n' )
    line.grid(row=1, column=0, sticky='n')
    
    scroll_frame = CTkScrollableFrame(window, width=350, height=350, fg_color="#182232")
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
    window  = CTkToplevel(root)
    window.title('Find Password')
    window.geometry('370x380')
    window.grid_columnconfigure(0, weight=1)
    
    title = CTkLabel(window, text = 'Find Password', font=( 'Sergoe UI', 25, 'bold' ) )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = CTkEntry(window, width=310, height=55, placeholder_text='Website', font=('Arial', 16))
    website_entry.grid(row=1, column=0, pady=5)

    login_entry = CTkEntry(window, width=310, height=55, placeholder_text='Login', font=('Arial', 16))
    login_entry.grid(row=2, column=0, pady=5)
    
    
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
            
        
    add_btn = CTkButton(window, text='Search', width=210, height=55, font=('Sergoe UI', 16), command=find_password)
    add_btn.grid(row=3, column=0, pady=20)

    password_textbox.configure(state='disabled')
    password_textbox.grid(row=4, column=0)
    
    
def change_window():
    window  = CTkToplevel(root)
    window.title('Change Password')
    window.geometry('370x380')
    window.resizable(False, False)
    window.grid_columnconfigure(0, weight=1)
    
    title = CTkLabel(window, text = 'Change Password', font=( 'Sergoe UI', 25, 'bold' ) )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = CTkEntry(window, width=310, height=55, placeholder_text='Website', font=('Arial', 16))
    website_entry.grid(row=1, column=0, pady=5)

    login_entry = CTkEntry(window, width=310, height=55, placeholder_text='Login', font=('Arial', 16))
    login_entry.grid(row=2, column=0, pady=5)
    
    new_password__entry = CTkEntry(window, width=310, height=55, placeholder_text='New Password', font=('Arial', 16))
    new_password__entry.grid(row=3, column=0, pady=5)
    
    message_label = CTkLabel(window, text='', font=('Sergoe UI', 14))
    message_label.grid(row=5, column=0)
    
    def change_password():
        website = website_entry.get().strip()
        login = login_entry.get().strip()
        password = new_password__entry.get().strip()
        rowc = update_password(website, login, password)
        if rowc > 0:
            message_label.configure(text='Password changed✅')
            
        else:
            message_label.configure(text='Account not found❌')
            
            
        website_entry.delete(0, 'end')
        login_entry.delete(0, 'end')
        new_password__entry.delete(0, 'end')
        
        
    change_btn = CTkButton(window, text='Change',  width=210, height=55, font=('Sergoe UI', 16), command=change_password)
    change_btn.grid(row=4, column=0, pady=5)
    
    
def delete_window():
    window  = CTkToplevel(root)
    window.title('Delete Password')
    window.geometry('370x320')
    window.resizable(False, False)
    window.grid_columnconfigure(0, weight=1)
    
    title = CTkLabel(window, text = 'Delete Password', font=( 'Sergoe UI', 25, 'bold' ) )
    title.grid(row=0, column=0, pady=(15, 15))
    
    website_entry = CTkEntry(window, width=310, height=55, placeholder_text='Website', font=('Arial', 16))
    website_entry.grid(row=1, column=0, pady=5)

    login_entry = CTkEntry(window, width=310, height=55, placeholder_text='Login', font=('Arial', 16))
    login_entry.grid(row=2, column=0, pady=5)
    
    message_label = CTkLabel(window, text='', font=('Sergoe UI', 14))
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
    
    
        
        
    delete_btn = CTkButton(window, text='Delete',  width=210, height=55, font=('Sergoe UI', 16), command=delete_password1)
    delete_btn.grid(row=3, column=0, pady=20)

def quit():
    close_database()
    root.destroy()
        
   
    
    

image_label = CTkLabel(root, image=image, text='')
image_label.grid(row=0, column=0, pady=(13, 7))

title = CTkLabel(root, text='PASSWORD MANAGER ', font=('Segoe UI', 20, 'bold'))
title.grid(row=1, column=0, )



# КНОПКИ
add_btn = CTkButton(root, text='Add Password', anchor='w', font=('Segoe UI', 15, 'bold'), width=400, height=60, fg_color='#1E2736', border_width=1, border_color="#364051", image=add_img, command=add_window)
add_btn.grid(row=2, column=0, pady=(15, 3))

watch_btn = CTkButton(root, text='View Passwords', anchor='w', font=('Segoe UI', 15, 'bold'), width=400, height=60, fg_color='#1E2736', border_width=1, border_color="#364051", image=watch_img, command=view_passwords)
watch_btn.grid(row=3, column=0, pady=3)

find_btn = CTkButton(root, text='Find Password', anchor='w', font=('Segoe UI', 15, 'bold'), width=400, height=60, fg_color='#1E2736', border_width=1, border_color="#364051", image=find_img, command=find_window)
find_btn.grid(row=4, column=0, pady=3)

change_btn = CTkButton(root, text='Change Password', anchor='w', font=('Segoe UI', 15, 'bold'), width=400, height=60, fg_color='#1E2736', border_width=1, border_color="#364051", image=change_img, command=change_window)
change_btn.grid(row=5, column=0, pady=3)

delete_btn = CTkButton(root, text='Delete Password', anchor='w', font=('Segoe UI', 15, 'bold'), width=400, height=60, fg_color='#1E2736', border_width=1, border_color="#364051", image=delete_img, command=delete_window)
delete_btn.grid(row=6, column=0, pady=3)

leave_btn = CTkButton(root, text='Exit', font=('Arial', 16, 'bold'), width=400, height=60, fg_color="#660917", border_width=1, border_color="#9C0017", hover_color="#850B1C", image=leave_img, command=quit)
leave_btn.grid(row=7, column=0, pady=40)


root.mainloop()