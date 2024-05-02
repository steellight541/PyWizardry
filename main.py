from tkinter import Tk  # importing the master widget
from menu import MyMenuBar  # importing the custom menu bar
from text import MyTextBlock  # importing the custom text block


class MyEditor(Tk):
    def __init__(self):
        super().__init__()
        self.title("My Text Editor")
        self.geometry("400x400")
        self.option_add("*tearOff", False)
        self.config(menu=MyMenuBar(self))
        self.text_block = MyTextBlock(self)




if __name__ == "__main__":
    app = MyEditor()
    app.mainloop()
