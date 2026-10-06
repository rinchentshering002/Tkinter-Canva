import tkinter as tk


def create_about_page(about_page, show_home):

    about_page.configure(bg="#F4F7FB")

    # ---------- Header ----------
    header = tk.Frame(
        about_page,
        bg="#2563EB",
        height=80
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    title = tk.Label(
        header,
        text="About Me",
        font=("Arial", 22, "bold"),
        bg="#2563EB",
        fg="white"
    )
    title.pack(side="left", padx=30, pady=20)

    # ---------- Profile Card ----------
    profile = tk.Frame(
        about_page,
        bg="white",
        highlightbackground="#E2E8F0",
        highlightthickness=1
    )
    profile.pack(padx=60, pady=40, fill="x")

    tk.Label(
        profile,
        text="👨‍💻",
        font=("Arial", 40),
        bg="white"
    ).pack(pady=(20, 5))

    tk.Label(
        profile,
        text="Khan",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#1E293B"
    ).pack()

    tk.Label(
        profile,
        text="My hobby is coding",
        font=("Arial", 12),
        bg="white",
        fg="#64748B"
    ).pack(pady=5)

    tk.Label(
        profile,
        text="Pursuing B.Ed ICT",
        font=("Arial", 12),
        bg="white",
        fg="#64748B"
    ).pack(pady=(0, 25))

    # ---------- Back Button ----------
    home_button = tk.Button(
        about_page,
        text="←  Back to Home",
        font=("Arial", 11, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=10,
        command=show_home
    )
    home_button.pack()