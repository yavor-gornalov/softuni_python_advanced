import tkinter as tk


def render_home(root, frame):
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
        command=lambda: print(f"register {frame.winfo_width() // 2}"),
    )

    login_btn = tk.Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=lambda: print(f"login {frame.winfo_height() // 2}"),
    )
    frame.create_window(400, 260, window=register_btn)
    frame.create_window(400, 320, window=login_btn)
