import tkinter as tk

height = 640
width = 800
dimensions = f"{width}x{height}"


def create_root():
    window = tk.Tk()
    window.title("GUI shop")
    window.geometry(dimensions)

    return window


def create_frame(wdw):
    fr = tk.Canvas(root, width=width, height=height)
    fr.grid(row=0, column=0)

    return fr


root = create_root()
frame = create_frame(root)
