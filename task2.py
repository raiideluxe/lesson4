import tkinter as tk

root = tk.Tk()
root.title()

label1 = tk.Label(root,text="Hello World!").grid(row=0,column=0)
label2 = tk.Label(root,text="Меня зовут Святогор").grid(row=1,column=1)

root.mainloop()