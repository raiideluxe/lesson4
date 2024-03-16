import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)

def button_add():
    global f_num
    global math
    math = "+"
    f_num = float(display.get())
    display.delete(0, tk.END)

def button_subtract():
    global f_num
    global math
    math = "-"
    f_num = float(display.get())
    display.delete(0, tk.END)

def button_multiply():
    global f_num
    global math
    math = "*"
    f_num = float(display.get())
    display.delete(0, tk.END)

def button_divide():
    global f_num
    global math
    math = "/"
    f_num = float(display.get())
    display.delete(0, tk.END)

def button_equal():
    second_number = float(display.get())
    display.delete(0, tk.END)

    if math == "+":
        result = f_num + second_number
    elif math == "-":
        result = f_num - second_number
    elif math == "*":
        result = f_num * second_number
    elif math == "/":
        result = f_num / second_number

    display.insert(0, result)

def button_clear():
    display.delete(0, tk.END)

# Создание графического интерфейса
root = tk.Tk()
root.title("Простой калькулятор")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '+', '-',
    '*', '/', '=', 'C'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=button_equal).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, command=button_clear).grid(row=row, column=col)
    elif button == '/':
        tk.Button(root, text=button, command=button_divide).grid(row=row, column=col)
    elif button == '*':
        tk.Button(root, text=button, command=button_multiply).grid(row=row, column=col)
    elif button == '+':
        tk.Button(root, text=button, command=button_add).grid(row=row, column=col)
    elif button == '-':
        tk.Button(root, text=button, command=button_subtract).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda x=button: button_click(x)).grid(row=row, column=col)

    col += 1
    if col > 2:
        col = 0
        row += 1

f_num = 0
math = ""

root.mainloop()
