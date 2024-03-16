import tkinter as tk
from mainWindow import MainWindow

def show_popup():
    popup = tk.Toplevel()
    popup.geometry("250x350+200+100")
    popup.title("Действие успешно выполнено")
    label=tk.Label(popup,text="Действие успешно выполнено")
    label.pack()
    button = tk.Button(popup,command=popup.destroy)
    button.pack()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("integerst")

    file = "interest.ico"
    root.iconbitmap(file)

    app = MainWindow(root)

    root.bind("<Escape>", app.quit)
    root.mainloop()
