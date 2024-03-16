import tkinter as tk

def myClick():
    label.config(text="Нажата кнопка!")

root = tk.Tk()
root.title("Снизу кнопка")

button = tk.Button(root, text="Я кнопка, нажми меня!", bg="white", fg="blue", command=myClick)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()