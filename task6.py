import tkinter as tk
from tkinter import PhotoImage, Label, Button
from PIL import Image, ImageTk
from pathlib import Path

class PhotoViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer")

        self.image_folder = Path("images")
        self.image_list = list(self.image_folder.glob("*.jpg"))
        self.current_image_index = 0

        self.photo_images = [ImageTk.PhotoImage(Image.open(img)) for img in self.image_list]

        self.label = Label(root, image=self.photo_images[self.current_image_index])
        self.label.grid(row=0, column=0, columnspan=3)

        self.info_label = Label(root, text=f"Image {self.current_image_index + 1}/{len(self.photo_images)}", bd=1, relief=tk.SUNKEN, anchor=tk.E)
        self.info_label.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

        self.button_back = Button(root, text="Previous", command=self.back, state=tk.DISABLED)
        self.button_back.grid(row=2, column=0)

        self.button_forward = Button(root, text="Next", command=lambda: self.forward(1))
        self.button_forward.grid(row=2, column=2)

    def back(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.update_image()

    def forward(self, step):
        if self.current_image_index < len(self.photo_images) - 1:
            self.current_image_index += step
            self.update_image()

    def update_image(self):
        self.label.grid_forget()
        self.label = Label(self.root, image=self.photo_images[self.current_image_index])
        self.label.grid(row=0, column=0, columnspan=3)

        self.info_label.config(text=f"Image {self.current_image_index + 1}/{len(self.photo_images)}")

        if self.current_image_index == 0:
            self.button_back.config(state=tk.DISABLED)
        else:
            self.button_back.config(state=tk.NORMAL)

        if self.current_image_index == len(self.photo_images) - 1:
            self.button_forward.config(state=tk.DISABLED)
        else:
            self.button_forward.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()

    file = Path(__file__).resolve().parent.joinpath("test_axe.ico")
    root.iconbitmap(file)

    app = PhotoViewerApp(root)
    root.mainloop()
