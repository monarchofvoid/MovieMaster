import tkinter as tk
from tkinter import messagebox
from auth import login_user, register_user
import admin_panel
import user_panel


def open_admin_panel():
    admin_panel.run_admin_panel()

def open_user_panel():
    user_panel.run_user_panel()

def attempt_login():
    username = username_entry.get()
    password = password_entry.get()
    role = login_user(username, password)
    if role == 'admin':
        messagebox.showinfo("Login", "Admin login successful")
        root.destroy()
        open_admin_panel()
    elif role == 'user':
        messagebox.showinfo("Login", "User login successful")
        root.destroy()
        open_user_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_register():
    def register():
        new_username = reg_username.get()
        new_email = reg_email.get()
        new_password = reg_password.get()
        register_user(new_username, new_email, new_password)
        messagebox.showinfo("Register", "Registration successful")
        reg_window.destroy()

    reg_window = tk.Toplevel(root)
    reg_window.title("Register")

    tk.Label(reg_window, text="Username:").grid(row=0, column=0)
    reg_username = tk.Entry(reg_window)
    reg_username.grid(row=0, column=1)

    tk.Label(reg_window, text="Email:").grid(row=1, column=0)
    reg_email = tk.Entry(reg_window)
    reg_email.grid(row=1, column=1)

    tk.Label(reg_window, text="Password:").grid(row=2, column=0)
    reg_password = tk.Entry(reg_window, show='*')
    reg_password.grid(row=2, column=1)

    tk.Button(reg_window, text="Register", command=register).grid(row=3, columnspan=2)


# Main window
root = tk.Tk()
root.title("Movie Database Login")

# Username
tk.Label(root, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Password
tk.Label(root, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)

# Buttons
tk.Button(root, text="Login", command=attempt_login).grid(row=2, columnspan=2)
tk.Button(root, text="Register", command=open_register).grid(row=3, columnspan=2)

root.mainloop()
