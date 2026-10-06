import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("File Dialog Example")
root.geometry("400x250")

def open_file():
    file_path = filedialog.askopenfilename()

    if file_path:
        print(f"Selected file: {file_path}")

button = tk.Button(
    root,
    text="Open File",
    command=open_file
)
button.pack(pady=20)

root.mainloop()