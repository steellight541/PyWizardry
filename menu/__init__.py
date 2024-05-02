from tkinter import Menu, filedialog

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


class MyFileMenu(Menu):
    """__summary__:
        A custom file menu for the text editor application.

    This class inherits from the `tk.Menu` class and provides additional functionality
    specific to the file menu of the text editor.

    Args:
        master (tk.Tk): The master widget for the menu.

    Attributes:
        master (tk.Tk): The master widget for the menu.

    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.add_command(label="Open File", command=self.open_file)
        self.add_command(label="Save File", command=self.save_file)
        self.add_command(label="Exit", command=self.master.quit)

    def open_file(self):
        """Open an existing project.

        This method is called when the "Open Project" option is selected from the file menu.
        It performs the necessary actions to open an existing project in the text editor.

        """
        TXT = filedialog.askopenfile().read() # type: ignore
        if TXT:
            # Perform actions with the selected folder path
            print("Selected folder:", TXT)
            self.master.text_block.delete("1.0", "end") # type: ignore
            self.master.text_block.insert("1.0", TXT) # type: ignore

    def save_file(self):
        """Save the current project.

        This method is called when the "Save Project" option is selected from the file menu.
        It performs the necessary actions to save the current project in the text editor.

        """
        folder_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("python files", "*.py"), ("Text files", "*.txt")],
        )
        if folder_path:
            # Perform actions with the selected folder path
            print("Selected folder:", folder_path)
            with open(folder_path, "w", encoding="utf-8") as file:
                file.write(self.master.text_block.get("1.0", "end").removesuffix("\n")) # type: ignore


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

