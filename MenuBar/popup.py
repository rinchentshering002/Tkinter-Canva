import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Popup Example")
root.geometry("400x250")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=10)

# Function
def show_popup():
    name = entry.get()

    if name == "":
        messagebox.showwarning("Warning", "Please enter your name!")
    else:
        messagebox.showinfo("Welcome", f"Hello, {name}!")

# Button
button = tk.Button(
    root,
    text="Submit",
    command=show_popup
)
button.pack(pady=20)

root.mainloop()