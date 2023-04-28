import tkinter as tk
from canvas import root, frame
from register_screen import render_registration


def render_home():
    """
    This func rendering initial looks of gui app.
    """
    register_btn = tk.Button(
        root,
        text="Register",
        bg="green",  # background color
        fg="white",  # font color
        borderwidth=0,
        width=20,
        height=3,
        command=render_registration,
    )

    login_btn = tk.Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=lambda: print(f"register {frame.winfo_width()}")
    )

    frame.create_window(400, 260, window=register_btn)
    frame.create_window(400, 320, window=login_btn)
