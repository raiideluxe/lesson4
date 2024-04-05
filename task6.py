import tkinter as tk
from tkinter import PhotoImage, Label, Button
from PIL import Image, ImageTk
from pathlib import Path

"""
class PhotoViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer")

        self.image_folder = Path("images")
        self.image_list = list(self.image_folder.glob("*.jpg"))
        self.current_image_index = 0

        self.photo_images = [ImageTk.PhotoImage(Image.open(img)) for img in self.image_list]
"""

if __name__ == "__main__":
    root = tk.Tk()

    file = Path(__file__).resolve().parent.joinpath("test_axe.ico")
    root.iconbitmap(file)

    app = PhotoViewerApp(root)
    root.mainloop()
