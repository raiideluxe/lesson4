import tkinter as tk
from mainWindow import MainWindow
if __name__ == "__main__":
    root = tk.Tk()
    root.title("integerst")

    file = "interest.ico"
    root.iconbitmap(file)

    app = MainWindow(root)

    root.bind("<Escape>", app.quit)
    root.mainloop()
