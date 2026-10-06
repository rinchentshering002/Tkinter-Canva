import tkinter as tk
from PIL import Image, ImageTk


def create_home_page(home_page, show_about):

    # =====================================================
    # WINDOW / PAGE SETTINGS
    # =====================================================

    home_page.configure(bg="#f5f5f5")

    # =====================================================
    # BACKGROUND IMAGE
    # =====================================================

    image = Image.open("background.jpg")
    image = image.resize((1000, 650))

    background_image = ImageTk.PhotoImage(image)

    background = tk.Label(
        home_page,
        image=background_image
    )

    background.image = background_image

    background.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    # =====================================================
    # TOP NAVIGATION BAR
    # =====================================================

    navbar = tk.Frame(
        home_page,
        bg="#111827",
        height=70
    )

    navbar.pack(
        side="top",
        fill="x"
    )

    logo = tk.Label(
        navbar,
        text="My Application",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#111827"
    )

    logo.pack(
        side="left",
        padx=30
    )

    about_button = tk.Button(
        navbar,
        text="About",
        font=("Arial", 11),
        fg="white",
        bg="#111827",
        activebackground="#374151",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=show_about
    )

    about_button.pack(
        side="right",
        padx=30
    )

    # =====================================================
    # SEARCH AREA
    # =====================================================

    search_frame = tk.Frame(
        home_page,
        bg="black"
    )

    search_frame.place(
        relx=0.5,
        rely=0.25,
        anchor="center",
        width=600,
        height=55
    )

    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 13),
        bd=0
    )

    search_entry.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(20, 10)
    )

    def search():
        text = search_entry.get()

        if text:
            result_label.config(
                text=f"Searching for: {text}"
            )
        else:
            result_label.config(
                text="Please enter something to search."
            )

    search_button = tk.Button(
        search_frame,
        text="🔍 Search",
        font=("Arial", 11, "bold"),
        bg="black",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        bd=0,
        padx=20,
        cursor="hand2",
        command=search
    )

    search_button.pack(
        side="right",
        fill="y",
        padx=5,
        pady=5
    )

    # =====================================================
    # MAIN CONTENT
    # =====================================================

    content_frame = tk.Frame(
        home_page,
        bg="white"
    )

    content_frame.place(
        relx=0.5,
        rely=0.55,
        anchor="center",
        width=650,
        height=230
    )

    title = tk.Label(
        content_frame,
        text="Welcome to My Application",
        font=("Arial", 26, "bold"),
        fg="#111827",
        bg="white"
    )

    # FIXED INDENTATION
    title.pack(
        pady=(30, 10)
    )

    description = tk.Label(
        content_frame,
        text="A clean and simple Tkinter application.",
        font=("Arial", 12),
        fg="#6B7280",
        bg="white"
    )

    description.pack(
        pady=5
    )

    content = tk.Label(
        content_frame,
        text="Search for information or explore the application\n"
             "using the navigation above.",
        font=("Arial", 11),
        fg="#4B5563",
        bg="white",
        justify="center"
    )

    content.pack(
        pady=15
    )

    result_label = tk.Label(
        content_frame,
        text="",
        font=("Arial", 11, "bold"),
        fg="#2563EB",
        bg="white"
    )

    result_label.pack(
        pady=5
    )