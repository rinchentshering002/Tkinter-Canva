import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=400, bg="skyblue")
canvas.pack()

# House
canvas.create_rectangle(150, 180, 350, 330, fill="yellow")

# Roof
canvas.create_polygon(130, 180, 250, 100, 370, 180, fill="red")

# Door
canvas.create_rectangle(220, 250, 280, 330, fill="brown")

# Window
canvas.create_rectangle(170, 210, 210, 250, fill="lightblue")

# Sun
canvas.create_oval(380, 50, 440, 110, fill="orange")

# Title
canvas.create_text(
    250, 40,
    text="MY HOME",
    font=("Arial", 24, "bold"),
    fill="darkblue"
)

root.mainloop()