import tkinter as tk

root = tk.Tk()

root.title("Menu Bar Demo")
root.geometry("500x300")

# Create a visible menu bar inside the window
menu_bar = tk.Frame(root, bg="#111827", height=40)
menu_bar.pack(side="top", fill="x")

file_button = tk.Menubutton(
    menu_bar,
    text="File",
    bg="#111827",
    fg="white",
    activebackground="#374151",
    activeforeground="white",
    relief="flat",
    padx=12,
    pady=6
)

file_menu = tk.Menu(file_button, tearoff=0)

file_menu.add_command(
    label="New",
    command=lambda: print("New clicked")
)

file_menu.add_command(
    label="Open",
    command=lambda: print("Open clicked")
)

file_menu.add_command(
    label="Save",
    command=lambda: print("Save clicked")
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)

file_button.config(menu=file_menu)
file_button.pack(side="left", padx=8, pady=4)

content = tk.Label(
    root,
    text="Menu is now visible inside the window.",
    font=("Arial", 14)
)

content.pack(expand=True)

root.mainloop()