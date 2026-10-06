import tkinter as tk

from home import create_home_page
from about import create_about_page


root = tk.Tk()
root.title("My Application")
root.geometry("650x550")
root.resizable(False, False)


# ---------- Pages ----------
home_page = tk.Frame(root)
about_page = tk.Frame(root)


# ---------- Navigation ----------
def show_home():
    about_page.pack_forget()
    home_page.pack(fill="both", expand=True)


def show_about():
    home_page.pack_forget()
    about_page.pack(fill="both", expand=True)


# ---------- Create Pages ----------
create_home_page(home_page, show_about)
create_about_page(about_page, show_home)


# ---------- Start ----------
show_home()

root.mainloop()