from tkinter import Tk


class Dwindow(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(width=600, height=400)
        self.title('Disappearing Text Writing')