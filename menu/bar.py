from tkinter import Menu
from .files import MyFileMenu
from .preferences import MyPreferencesMenu


class MyMenuBar(Menu):
    """_summary_

    Args:
        tk (_type_): _description_
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.add_cascade(label="File", menu=MyFileMenu(master))
        self.add_cascade(label="Preferences", menu=MyPreferencesMenu(master))