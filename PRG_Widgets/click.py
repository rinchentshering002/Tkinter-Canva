import tkinter as tk
root= tk.Tk()
agree= tk.BooleanVar()
check= tk.Checkbutton(
    root,
    text="I agree",
    variable=agree
)

check.pack()

def check_value():
    print(agree.get())
    
tk.Button(root, text="Check", command=check_value).pack()

root.mainloop()