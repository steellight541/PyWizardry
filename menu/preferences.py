from tkinter import Menu 

class MyPreferencesMenu(Menu):
    """__summary__:
        A custom menu class for managing user preferences in the text editor.

    Args:
        master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
    """

    def __init__(self, master):
        """
        Initializes an instance of the MyPreferencesMenu class.

        Args:
            master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
        """
        super().__init__(master)
        self.master = master
        self.add_cascade(label="Styles", menu=MyStylesMenu(master))
        self.add_cascade(label="Zen Mode", menu=MyZenModeMenu(master))








class MyZenModeMenu(Menu):
    """__summary__:
        A custom menu class for managing Zen mode in the text editor.

    Args:
        master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
    """

    def __init__(self, master):
        """
        Initializes an instance of the MyVimModeMenu class.

        Args:
            master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
        """
        super().__init__(master)
        self.master = master
        self.iszen = False
        self.add_command(label="Toggle Vim Mode", command=self.toggle_zen_mode)

    def toggle_zen_mode(self):
        """
        Enables Vim mode in the text editor.
        """
        self.iszen = not self.iszen
        self.master.attributes("-fullscreen", self.iszen) # type: ignore


class MyStylesMenu(Menu):
    """
    A custom menu class for managing different styles/themes in the text editor.

    Args:
        master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
    """

    def __init__(self, master):
        """
        Initializes an instance of the MyStylesMenu class.

        Args:
            master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
        """
        super().__init__(master)

        self.master = master
        self.add_cascade(label="Themes", menu=MyThemesMenu(master))



class MyThemesMenu(Menu):
    """__summary__:
        A custom menu class for managing different themes in the text editor.
    Args:
        master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
    """

    def __init__(self, master):
        """
        Initializes an instance of the MyThemesMenu class.

        Args:
            master: The master widget (typically a Tkinter.Tk instance) that this menu is associated with.
        """
        super().__init__(master)

        self.master = master
        self.add_command(label="Light Theme", command=self.set_light_theme)
        self.add_command(label="Dark Theme", command=self.set_dark_theme)

    def set_line_numbers(self, fg, bg):
        """
        Sets the line numbers to the specified foreground and background colors.

        Args:
            fg (str): The foreground color.
            bg (str): The background color.

        """
        self.master.text_block.lines_counter.config(fg=fg, bg=bg) # type: ignore

    def set_text_block(self, fg, bg):
        """
        Sets the text block to the specified foreground and background colors.

        Args:
            fg (str): The foreground color.
            bg (str): The background color.

        """
        self.master.text_block.config(fg=fg, bg=bg) # type: ignore

    def set_light_theme(self):
        """
        Sets the text editor to use a light theme.
        """
        self.set_line_numbers("black", "lightgrey")
        self.set_text_block("black", "white")

    def set_dark_theme(self):
        """
        Sets the text editor to use a dark theme.
        """
        self.set_line_numbers("white", "black")
        self.set_text_block("white", "black")

