import os
import tkinter as tk
from canvas import root, frame
from helpers import clear_screen


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


def login():
    path = "./db/users.txt"
    if os.path.exists(path):
        with open(path, "r") as file:
            print(file.read())
    # with open(path, "a") as file:
    #     file.write("test")


username = tk.Entry(root)
email = tk.Entry(root)
password = tk.Entry(root, show="*")
confirm_password = tk.Entry(root, show="*")

register_button = tk.Button(
    root,
    text="Register",
    bg="green",
    fg="white",
    command=lambda: print("register button"),
)

back_button = tk.Button(
    root,
    text="Back",
    bg="grey",
    fg="white",
    command=lambda: print("back button"),
)
