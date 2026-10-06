import tkinter as tk
from tkinter import messagebox

# Validate Name Function
def validate_name(*args):
    name = name_var.get()
    if name == "":
        name_label.config(text="Please enter your name")
    elif len(name) < 3:
        name_label.config(text="Name must be at least 3 characters")
    else:
        name_label.config(text="✓ Name looks good")

# Validate Email Function
def validate_email(*args):
    email = email_var.get()
    if email == "":
        email_label.config(text="Please enter your email")
    elif "@" not in email:
        email_label.config(text="Email must contain @")
    elif "." not in email:
        email_label.config(text="Email should contain a domain, e.g. .com")
    else:
        email_label.config(text="✓ Email looks good")

# Submit Form Function
def submit_form():
    name = name_var.get()
    email = email_var.get()

# Check Name
    if len(name) < 3:
        messagebox.showwarning(
            "Check your name",
            "Please enter at least 3 characters for your name.",
        )
        return

    if "@" not in email or "." not in email:
        messagebox.showwarning(
            "Check your email",
            "Please enter a valid email address.",
        )
        return

    messagebox.showinfo(
        "Success",
        f"Thank you, {name}!\nYour form was submitted successfully.",
    )

# Create the main application window
root = tk.Tk()
root.title("Instant Form Validation")
root.geometry("450x350")

# Create StringVar for Name and Email
name_var = tk.StringVar()
email_var = tk.StringVar()

# Create Labels, Entry Widgets, and Submit Button
tk.Label(root, text="Student Registration", font=("Arial", 18)).pack(pady=20)

# Name Entry
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, textvariable=name_var, width=40)
name_entry.pack(pady=5)
name_label = tk.Label(root, text="", fg="gray")
name_label.pack(pady=3)
name_var.trace_add("write", validate_name)

# Email Entry
tk.Label(root, text="Email").pack(pady=(10, 0))
email_entry = tk.Entry(root, textvariable=email_var, width=40)
email_entry.pack(pady=5)
email_label = tk.Label(root, text="", fg="gray")
email_label.pack(pady=3)
email_var.trace_add("write", validate_email)

# Submit Button
tk.Button(root, text="Submit", command=submit_form, width=15).pack(pady=25)

# Start the main event loop
root.mainloop()