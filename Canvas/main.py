import tkinter as tk

root = tk.Tk()
root.title("My First Canvas")

canvas = tk.Canvas(root, width=500, height=350, bg="white")

canvas.pack()

create_rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="blue")
create_oval = canvas.create_oval(200, 50, 300, 150, fill="red") 
create_line = canvas.create_line(50, 200, 300, 200, fill="green", width=3)  
create_text = canvas.create_text(200, 250, text="Hello, Canvas!", font=("Arial", 16), fill="purple")

# Animation function to move the rectangle
def animate_rectangle():
    canvas.move(create_rectangle, 5, 0)  # Move right by 5 pixels
    canvas.after(100, animate_rectangle)  # Repeat every 100 milliseconds
root.mainloop()