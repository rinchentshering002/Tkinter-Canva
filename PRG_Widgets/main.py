
import tkinter as tk
root = tk.Tk()

root.title("Widget State Demo")
root.geometry("400x300")

# Counter variable
count = 0

def click_button():
    global count
    count += 1
    button.config(text=f"Clicked {count} times")

def disable_button():
    button.config(state="disabled")

def enable_button():
    button.config(state="normal")

# Main button
button = tk.Button(
    root,
    text="Click Me!", 
    command=click_button
)

button.pack(pady=30)

# Disable button
disable_control = tk.Button(
    root,
    text="Disable",
    command=disable_button
)
disable_control.pack(pady=5)

# Enable button
enable_control = tk.Button(
    root,
    text="Enable",
    command=enable_button
)
enable_control.pack(pady=5)

root.mainloop()