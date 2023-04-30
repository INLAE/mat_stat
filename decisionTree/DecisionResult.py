import tkinter as tk
from PIL import Image, ImageTk
from Decision import Decision
from IEntity import IEntity

class DecisionResult(Decision):
    def __init__(self, res: str):
        self.res = res

    def evaluate(self, entity: IEntity):
        root = tk.Tk()
        root.title("Result")

        # Загрузка изображения
        image = Image.open("shrek.png")
        photo = ImageTk.PhotoImage(image)

        # Создание виджета Label с изображением
        image_label = tk.Label(root, image=photo)
        image_label.image = photo
        image_label.pack(side="left")

        # Создание виджета Label с текстом
        text_label = tk.Label(root, text=self.res, font=("Helvetica", 30))
        text_label.pack(side="left", padx=20)

        root.mainloop()
