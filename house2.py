import tkinter as tk

# Create window
window = tk.Tk()
window.title("House 2")
window.geometry("700x500")

# Create canvas
canvas = tk.Canvas(window, width=700, height=500, bg="lightblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 380, 700, 500, fill="green")

# House body
canvas.create_rectangle(
    200, 220, 500, 380,
    fill="lightyellow",
    outline="black"
)

# Roof
canvas.create_polygon(
    170, 220,
    350, 90,
    530, 220,
    fill="darkred",
    outline="black"
)

# Door
canvas.create_rectangle(
    325, 290, 375, 380,
    fill="brown",
    outline="black"
)

# Door knob
canvas.create_oval(
    360, 333, 366, 339,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    230, 250, 290, 300,
    fill="lightblue",
    outline="black"
)

# Left window cross
canvas.create_line(260, 250, 260, 300, fill="black")
canvas.create_line(230, 275, 290, 275, fill="black")

# Right window
canvas.create_rectangle(
    410, 250, 470, 300,
    fill="lightblue",
    outline="black"
)

# Right window cross
canvas.create_line(440, 250, 440, 300, fill="black")
canvas.create_line(410, 275, 470, 275, fill="black")

# Tree trunk
canvas.create_rectangle(
    80, 300, 110, 380,
    fill="brown",
    outline="black"
)

# Tree leaves
canvas.create_oval(
    40, 230, 150, 330,
    fill="darkgreen",
    outline="black"
)

# Sun
canvas.create_oval(
    570, 50, 630, 110,
    fill="yellow",
    outline="orange"
)

# Clouds
canvas.create_oval(80, 70, 140, 110, fill="white", outline="white")
canvas.create_oval(120, 55, 190, 110, fill="white", outline="white")
canvas.create_oval(165, 70, 220, 110, fill="white", outline="white")

# Start program
window.mainloop()
