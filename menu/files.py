from tkinter import Menu, filedialog
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