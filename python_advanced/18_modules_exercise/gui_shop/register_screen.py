import os
from json import loads, dump
import tkinter as tk
from canvas import root, frame
from helpers import clear_screen

USERS_PATH = "./db/users.txt"


def render_registration():
    clear_screen()

    frame.create_text(80, 50, text="Username:", width=80)
    frame.create_window(200, 50, window=username, width=160)

    frame.create_text(80, 100, text="E-mail:", width=80)
    frame.create_window(200, 100, window=email, width=160)

    frame.create_text(80, 150, text="Password:", width=80)
    frame.create_window(200, 150, window=password, width=160)

    frame.create_text(80, 200, text="Confirm:", width=80)
    frame.create_window(200, 200, window=confirm_password, width=160)

    frame.create_window(160, 250, window=register_button, width=80)
    frame.create_window(240, 250, window=back_button, width=80)


def get_form_data():
    form_data = {
        "username": username.get(),
        "email": email.get(),
        "password": password.get(),
        "confirm_password": confirm_password.get()
    }
    return form_data


def get_users_data():
    users = []
    if os.path.exists(USERS_PATH):
        with open(USERS_PATH, "r") as file:
            for user in file:
                users.append(loads(user))
    return users


def put_user_data(user):
    with open(USERS_PATH, "a") as file:
        dump(user, file)
        file.write("\n")


def register():
    new_user = get_form_data()
    users = get_users_data()
    if new_user["username"] not in users:
        put_user_data(new_user)


username = tk.Entry(root)
email = tk.Entry(root)
password = tk.Entry(root, show="*")
confirm_password = tk.Entry(root, show="*")

register_button = tk.Button(
    root,
    text="Register",
    bg="green",
    fg="white",
    command=register,
)

back_button = tk.Button(
    root,
    text="Back",
    bg="grey",
    fg="white",
    command=lambda: print("BACK button"),
)
