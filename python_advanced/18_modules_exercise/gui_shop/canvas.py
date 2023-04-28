import tkinter as tk

height = 640
width = 800
dimensions = f"{width}x{height}"


def create_root():
    root = tk.Tk()
    root.title("GUI shop")
    root.geometry(dimensions)
    create_frame(root)

    return root


def create_frame(root):
    frame = tk.Canvas(root, width=width, height=height)
    frame.grid(row=0, column=0)

    return frame


def get_frame_height(): return height


def get_frame_width(): return width


root = create_root()
frame = create_frame(root)
