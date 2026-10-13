'''import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(root, width=600, height=350, bg="skyblue")
canvas.pack()

ball = canvas.create_oval(40, 40, 90, 90, fill="red")

def move_ball():
    canvas.move(ball, 100, 40)
    root.after(70, move_ball)

move_ball()

root.mainloop()'''

import tkinter as tk

# --- 1. Setup the Window and Canvas ---
root = tk.Tk()
root.title("Smart Traffic Light System")
canvas = tk.Canvas(root, width=600, height=400, bg="#87CEEB") # Sky blue background
canvas.pack()

# --- 2. Global Variables (State & Position) ---
light_state = "red"
car_x = 50
car_y = 320
car_speed = 4
stop_line_x = 260 # The X coordinate where the car must stop

# --- 3. Draw Scenery ---
canvas.create_oval(80, 40, 150, 110, fill="yellow", outline="") # Sun
canvas.create_rectangle(0, 350, 600, 400, fill="#555555", outline="") # Road
# Crosswalk lines
for i in range(0, 600, 40):
    canvas.create_rectangle(i, 350, i+20, 400, fill="yellow", outline="")

# --- 4. Draw Traffic Light ---
canvas.create_rectangle(310, 150, 330, 350, fill="gray", outline="") # Pole
canvas.create_rectangle(280, 50, 360, 230, fill="#222222", outline="") # Light Housing

# Draw the lights (Store their IDs so we can change their colors later)
red_light = canvas.create_oval(295, 65, 345, 115, fill="darkred", outline="")
yellow_light = canvas.create_oval(295, 120, 345, 170, fill="darkgoldenrod", outline="")
green_light = canvas.create_oval(295, 175, 345, 225, fill="darkgreen", outline="")

# --- 5. Draw Car ---
# We use the tag "car" for all parts so we can move them together
canvas.create_rectangle(car_x, car_y, car_x+100, car_y+40, fill="green", outline="", tags="car") # Body
canvas.create_rectangle(car_x+20, car_y-25, car_x+80, car_y, fill="green", outline="", tags="car") # Roof
canvas.create_rectangle(car_x+25, car_y-20, car_x+45, car_y, fill="white", outline="", tags="car") # Window 1
canvas.create_rectangle(car_x+55, car_y-20, car_x+75, car_y, fill="white", outline="", tags="car") # Window 2
canvas.create_oval(car_x+15, car_y+30, car_x+35, car_y+50, fill="black", outline="", tags="car") # Wheel 1
canvas.create_oval(car_x+65, car_y+30, car_x+85, car_y+50, fill="black", outline="", tags="car") # Wheel 2

# --- 6. Logic Functions ---

def change_light():
    """State machine to cycle the traffic lights using root.after() for timing."""
    global light_state
    
    if light_state == "red":
        light_state = "green"
        canvas.itemconfig(red_light, fill="darkred")
        canvas.itemconfig(green_light, fill="lime green")
        # Green light lasts for 3 seconds
        root.after(3000, change_light) 
        
    elif light_state == "green":
        light_state = "yellow"
        canvas.itemconfig(green_light, fill="darkgreen")
        canvas.itemconfig(yellow_light, fill="yellow")
        # Yellow light lasts for 1 second
        root.after(1000, change_light) 
        
    elif light_state == "yellow":
        light_state = "red"
        canvas.itemconfig(yellow_light, fill="darkgoldenrod")
        canvas.itemconfig(red_light, fill="red")
        # Red light lasts for 3 seconds
        root.after(3000, change_light) 

def move_car():
    """Animation loop to move the car based on the light_state."""
    global car_x
    
    # Check if the car has already passed the intersection line
    car_passed_line = (car_x > stop_line_x)
    
    # Movement logic
    if light_state == "green" or car_passed_line:
        # Car moves forward
        car_x += car_speed
        canvas.move("car", car_speed, 0)
        
    elif (light_state == "red" or light_state == "yellow") and not car_passed_line:
        # Car stops at the line. 
        # Check if the front of the car is approaching the line
        if car_x + 100 + car_speed > stop_line_x:
            # Snap the car exactly to the stop line
            snap_distance = stop_line_x - (car_x + 100)
            car_x += snap_distance
            canvas.move("car", snap_distance, 0)

    # Reset car to the left side if it drives off the right screen
    if car_x > 600:
        car_x = -150
        # Move all parts of the car back to the start using coords
        canvas.coords("car", 
                      car_x, car_y, car_x+100, car_y+40,          # body
                      car_x+20, car_y-25, car_x+80, car_y,        # roof
                      car_x+25, car_y-20, car_x+45, car_y,        # window 1
                      car_x+55, car_y-20, car_x+75, car_y,        # window 2
                      car_x+15, car_y+30, car_x+35, car_y+50,     # wheel 1
                      car_x+65, car_y+30, car_x+85, car_y+50)     # wheel 2

    # Run this move_car function again in 20 milliseconds (approx 50 FPS)
    root.after(20, move_car)

# --- 7. Start the Program ---
# Turn the initial red light on
canvas.itemconfig(red_light, fill="red")

# Start the timers
root.after(3000, change_light) # Begin the traffic light cycle
root.after(20, move_car)       # Begin the car animation loop

# Start the Tkinter event loop
root.mainloop()