from tkinter import *
from mainWindow import MainWindow

def circle():
    c.create_oval(x, y, x + 30, y + 30)


def square():
    c.create_rectangle(x, y, x + 30, y + 30)


def triangle():
    c.create_polygon(x, y, x - 15, y + 30, x + 15, y + 30,
                     fill='white', outline='black')


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


x = 0
y = 0

root = Tk()
root.title("integerst")

file = "interest.ico"
root.iconbitmap(file)


c = Canvas(width=300, height=300, bg='white')
c.grid(row=0,column=0)
c.bind("<Button-3>", popup)
app = MainWindow(root)
root.bind("<Escape>", app.quit)
menu = Menu(tearoff=0)
menu.add_command(label="Круг", command=circle)
menu.add_command(label="Квадрат", command=square)
menu.add_command(label="Треугольник", command=triangle)
root.mainloop()
