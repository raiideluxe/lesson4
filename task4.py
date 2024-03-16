import tkinter as tk

def show_message():
    name = entry.get()
    message = f"Привет, {name}!"
    popup = tk.Tk()
    popup.title("Приветствие")
    label = tk.Label(popup, text=message)
    label.pack(side="top", fill="x", pady=10)
    popup.mainloop()

root = tk.Tk()
root.title("Мне нужны твои глаза и имя")

entry = tk.Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
entry.pack(pady=10)
entry.insert(0, "Введите ваше имя")

button = tk.Button(root, text="Подтвердить", bg="white", fg="blue", command=show_message)
button.pack(pady=10)

root.mainloop()