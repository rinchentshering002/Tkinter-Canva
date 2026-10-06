import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ==========================================
# CREATE WINDOW
# ==========================================

root = tk.Tk()
root.title("Travel Booking Form")
root.geometry("500x750")

# ==========================================
# VARIABLES
# ==========================================

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
date_var = tk.StringVar()
travellers_var = tk.StringVar()
travel_type = tk.StringVar()

# ==========================================
# VALIDATION FUNCTIONS
# ==========================================

def validate_name(*args):

    name = name_var.get().strip()

    if name == "":
        name_message.config(
            text="Please enter your full name (at least 2 characters)."
        )

    elif len(name) < 2:
        name_message.config(
            text="Name should contain at least 2 characters."
        )

    elif not name.replace(" ", "").isalpha():
        name_message.config(
            text="Name should contain letters only."
        )

    else:
        name_message.config(
            text="✓ Name looks good."
        )

def validate_email(*args):

    email = email_var.get().strip()

    if email == "":
        email_message.config(
            text="Please enter your email address."
        )

    elif "@" not in email:
        email_message.config(
            text="Please include @ in your email."
        )

    elif "." not in email:
        email_message.config(
            text="Please enter a valid email address."
        )

    else:
        email_message.config(
            text="✓ Email looks good."
        )

def validate_phone(*args):

    phone = phone_var.get().strip()

    if phone == "":
        phone_message.config(
            text="Please enter your 8-digit phone number."
        )

    elif not phone.isdigit():
        phone_message.config(
            text="Please use numbers only."
        )

    elif len(phone) < 8:
        phone_message.config(
            text="Please enter 8 digits."
        )

    elif len(phone) > 8:
        phone_message.config(
            text="Phone number cannot exceed 8 digits."
        )

    else:
        phone_message.config(
            text="✓ Phone number looks good."
        )

def validate_date(*args):

    date = date_var.get().strip()

    if date == "":
        date_message.config(
            text="Please enter the date as DD/MM/YYYY."
        )
        return

    try:

        travel_date = datetime.strptime(
            date,
            "%d/%m/%Y"
        )

        if travel_date.date() < datetime.now().date():

            date_message.config(
                text="Please choose a future travel date."
            )

        else:

            date_message.config(
                text="✓ Date looks good."
            )

    except ValueError:

        date_message.config(
            text="Please use DD/MM/YYYY format."
        )

def validate_travellers(*args):

    travellers = travellers_var.get().strip()

    if travellers == "":
        travellers_message.config(
            text="Please enter the number of travellers (1–10)."
        )

    elif not travellers.isdigit():
        travellers_message.config(
            text="Please enter numbers only."
        )

    elif int(travellers) < 1:
        travellers_message.config(
            text="Please enter at least 1 traveller."
        )

    elif int(travellers) > 10:
        travellers_message.config(
            text="Please enter a maximum of 10 travellers."
        )

    else:
        travellers_message.config(
            text="✓ Number of travellers looks good."
        )

# ==========================================
# BOOK BUTTON VALIDATION
# ==========================================

def book_now():

    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()
    destination = destination_combo.get()
    date = date_var.get().strip()
    travellers = travellers_var.get().strip()
    travel = travel_type.get()

    # Check name
    if name == "" or len(name) < 2 or not name.replace(" ", "").isalpha():
        messagebox.showerror(
            "Error",
            "Please correct your full name."
        )
        name_entry.focus()
        return

    # Check email
    if email == "" or "@" not in email or "." not in email:
        messagebox.showerror(
            "Error",
            "Please enter a valid email address."
        )
        email_entry.focus()
        return

    # Check phone
    if phone == "" or not phone.isdigit() or len(phone) != 8:
        messagebox.showerror(
            "Error",
            "Please enter a valid 8-digit phone number."
        )
        phone_entry.focus()
        return

    # Check destination
    if destination == "":
        messagebox.showerror(
            "Error",
            "Please select a destination."
        )
        destination_combo.focus()
        return

    # Check date
    try:
        travel_date = datetime.strptime(
            date,
            "%d/%m/%Y"
        )

        if travel_date.date() < datetime.now().date():
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid future date."
        )
        date_entry.focus()
        return

    # Check travellers
    if not travellers.isdigit():
        messagebox.showerror(
            "Error",
            "Please enter the number of travellers."
        )
        travellers_entry.focus()
        return

    if int(travellers) < 1 or int(travellers) > 10:
        messagebox.showerror(
            "Error",
            "Number of travellers must be between 1 and 10."
        )
        travellers_entry.focus()
        return

    # Check travel type
    if travel == "":
        messagebox.showerror(
            "Error",
            "Please select a travel type."
        )
        return

    # Successful booking
    messagebox.showinfo(
        "Success",
        "Your travel booking has been confirmed!"
    )

# ==========================================
# CONNECT VALIDATION TO TYPING
# ==========================================

name_var.trace_add("write", validate_name)
email_var.trace_add("write", validate_email)
phone_var.trace_add("write", validate_phone)
date_var.trace_add("write", validate_date)
travellers_var.trace_add("write", validate_travellers)

# ==========================================
# TITLE
# ==========================================

tk.Label(
    root,
    text="Travel Booking Form",
    font=("Arial", 20, "bold")
).pack(pady=15)

# ==========================================
# FULL NAME
# ==========================================

tk.Label(
    root,
    text="Full Name:"
).pack()

name_entry = tk.Entry(
    root,
    textvariable=name_var,
    width=40
)
name_entry.pack(pady=3)

name_message = tk.Label(
    root,
    text="Please enter your full name (at least 2 characters).",
    fg="gray"
)
name_message.pack()

# ==========================================
# EMAIL
# ==========================================

tk.Label(
    root,
    text="Email:"
).pack(pady=(10, 0))

email_entry = tk.Entry(
    root,
    textvariable=email_var,
    width=40
)
email_entry.pack(pady=3)

email_message = tk.Label(
    root,
    text="Please enter your email address.",
    fg="gray"
)
email_message.pack()

# ==========================================
# PHONE
# ==========================================

tk.Label(
    root,
    text="Phone Number:"
).pack(pady=(10, 0))

phone_entry = tk.Entry(
    root,
    textvariable=phone_var,
    width=40
)
phone_entry.pack(pady=3)

phone_message = tk.Label(
    root,
    text="Please enter your 8-digit phone number.",
    fg="gray"
)
phone_message.pack()

# ==========================================
# DESTINATION
# ==========================================

tk.Label(
    root,
    text="Destination:"
).pack(pady=(10, 0))

destination_combo = ttk.Combobox(
    root,
    values=[
        "Thimphu",
        "Paro",
        "Punakha",
        "Phobjikha",
        "Bumthang"
    ],
    width=37,
    state="readonly"
)
destination_combo.pack(pady=3)

destination_message = tk.Label(
    root,
    text="Please choose your travel destination.",
    fg="gray"
)
destination_message.pack()

# ==========================================
# TRAVEL DATE
# ==========================================

tk.Label(
    root,
    text="Travel Date:"
).pack(pady=(10, 0))

date_entry = tk.Entry(
    root,
    textvariable=date_var,
    width=40
)
date_entry.pack(pady=3)

date_message = tk.Label(
    root,
    text="Please enter the date as DD/MM/YYYY.",
    fg="gray"
)
date_message.pack()

# ==========================================
# NUMBER OF TRAVELLERS
# ==========================================

tk.Label(
    root,
    text="Number of Travellers:"
).pack(pady=(10, 0))

travellers_entry = tk.Entry(
    root,
    textvariable=travellers_var,
    width=40
)
travellers_entry.pack(pady=3)

travellers_message = tk.Label(
    root,
    text="Please enter the number of travellers (1–10).",
    fg="gray"
)
travellers_message.pack()

# ==========================================
# TRAVEL TYPE
# ==========================================

tk.Label(
    root,
    text="Travel Type:"
).pack(pady=(10, 0))

tk.Radiobutton(
    root,
    text="Flight",
    variable=travel_type,
    value="Flight"
).pack()

tk.Radiobutton(
    root,
    text="Bus",
    variable=travel_type,
    value="Bus"
).pack()

tk.Radiobutton(
    root,
    text="Train",
    variable=travel_type,
    value="Train"
).pack()

travel_message = tk.Label(
    root,
    text="Please select your preferred travel type.",
    fg="gray"
)
travel_message.pack()

# ==========================================
# BOOK BUTTON
# ==========================================

tk.Button(
    root,
    text="Book Now",
    command=book_now,
    width=20
).pack(pady=20)

# ==========================================
# START PROGRAM
# ==========================================

root.mainloop()

