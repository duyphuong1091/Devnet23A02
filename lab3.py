import tkinter as tk

root = tk.Tk()
root.withdraw()
data_from_clipboard = root.clipboard_get()
print(data_from_clipboard)