import tkinter as tk
import tkinter.ttk as ttk
from IEntity import IEntity


class Node(IEntity):
    def set_title_gui(self, title: str) -> bool:
        root = tk.Tk()
        root.title(title)
        root.geometry("1000x420+200+200")
        root.resizable(False, False)
        root.config(background="#F5F5F5")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#FFFFFF", foreground="#000000")

        label = ttk.Label(root, text=title, font=("Segoe UI", 18), wraplength=350)
        label.config(borderwidth=2, relief="groove", padding=10)
        label.pack(pady=10)

        def on_button_click(answ):
            root.answer = answ
            root.destroy()

        yes_img = tk.PhotoImage(file='yes.png')
        yes_button = ttk.Button(root, image=yes_img, command=lambda: on_button_click(1))
        yes_button.pack(side='left', padx=10)

        no_img = tk.PhotoImage(file='no.png')
        no_button = ttk.Button(root, image=no_img, command=lambda: on_button_click(0))
        no_button.pack(side='right', padx=10)

        root.wait_window()
        return root.answer