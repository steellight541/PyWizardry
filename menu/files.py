from tkinter import Menu, filedialog

class MyFileMenu(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.add_command(label="Open File", command=self.open_file)
        self.add_command(label="Save File", command=self.save_file)
        self.add_command(label="Exit", command=self.master.quit)

    def open_file(self):
        TXT = filedialog.askopenfile().read() # type: ignore
        if TXT:
            # Perform actions with the selected folder path
            print("Selected folder:", TXT)
            self.master.text_block.delete("1.0", "end") # type: ignore
            self.master.text_block.insert("1.0", TXT) # type: ignore
            self.master.text_block.check_words()

    def save_file(self):
        folder_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("python files", "*.py"), ("Text files", "*.txt")],
        )
        if folder_path:
            # Perform actions with the selected folder path
            print("Selected folder:", folder_path)
            with open(folder_path, "w", encoding="utf-8") as file:
                file.write(self.master.text_block.get("1.0", "end").removesuffix("\n")) # type: ignore