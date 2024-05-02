from tkinter import Tk  # importing the master widget
from menu import MyMenuBar  # importing the custom menu bar
from text import MyTextBlock  # importing the custom text block


class MyEditor(Tk):
    """A custom application class for My App.

    This class inherits from the `tk.Tk` class and provides a custom application window for My App.

    Args:
        tk (type): The tkinter module.

    Attributes:
        title (str): The title of the application window.
        geometry (str): The size of the application window.

    """

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
