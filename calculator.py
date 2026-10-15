import tkinter as tk

root = tk.Tk()



root.title("Calculator")
root.configure(background = 'cyan')
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("390x400")


def click(value):
    screen.insert(tk.END, value)

def clear():
    screen.delete(0, tk.END)

def calculate():
    try:
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, result)
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

def make_button(text, r, c):
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda: click(text)
    tk.Button(root, 
    text = text, 
    font=("Arial", 16),
     width = 4, 
     height = 2, 
     bg = ("yellow"),
     fg=("purple"),
     command = action).grid(row = r, column=c)

screen = tk.Entry(root, font=("Arial", 20), justify="right")
screen.grid(row=0, column=0, columnspan = 4, padx=15, pady=15)

rows = [
    ["7", "8", "9",  "/"],
    ["4", "5", "6",  "*"],
    ["1", "2", "3",  "-"],
    [ "0", "=",  "+", "C"],
    
]


for r in range(len(rows)):
    for c in range(len(rows[r])):
        make_button(rows[r][c], r+1, c)

root.mainloop()  
