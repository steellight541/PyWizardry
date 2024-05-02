from tkinter.scrolledtext import ScrolledText
from tkinter import Text
from math import trunc, log10


class MyTextBlock(ScrolledText):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(font=("Consolas", 12), width=1, wrap="none", endline="", undo=True)
        self.pack(
            side="right",
            fill="both",
            expand=True,
        )
        # make it so the textblock has line numbers that dynamically update and scroll with the text
        self.lines_counter = MyLinesNumbers(master, self)
        # crtl + z and crtl + y
        self.bind("<Control-z>", self.undo)
        self.bind("<Control-Z>", self.undo)
        self.bind("<Control-y>", self.redo)
        self.bind("<Control-Y>", self.redo)

        # tab key
        self.bind("<Tab>", self.tab)

    def tab(self, event):
        self.insert("insert", " " * 4)
        return "break"
    
    def undo(self, event):
        print("undo")
        self.edit_undo()
        return "break"

    def redo(self, event):
        self.edit_redo()
        return "break"


class MyLinesNumbers(Text):
    def __init__(self, master, text_block):
        super().__init__(master)
        self.text = ""
        self.text_size = 0
        self.master = master
        self.text_block = text_block
        self.config(
            font=("Consolas", 12),
            width=4,
            height=20,
            bg="lightgrey",
            state="disabled",
            selectbackground="lightgrey",
            selectforeground="black",
            wrap="none",
        )
        self.pack(side="left", fill="y")
        self.update_lines()

    def update_lines(self):
        self.create_numbers()
        self.update_yview()
        self.config(state="disabled")
        self.after(100, self.update_lines)

    def create_numbers(self):
        lines_amt = len(self.text_block.get("1.0", "end").split("\n"))
        line_numbers = "\n".join(
            (str(i) + ".") for i in range(1, lines_amt)
        ).removesuffix("\n")

        if line_numbers != self.text:
            self.text = line_numbers
            self.config(state="normal")
            self.delete("1.0", "end")
            self.insert("1.0", line_numbers)
            self.config(state="disabled")

        if self.text_size != len(str(lines_amt)) + 1:
            self.text_size = len(str(lines_amt)) + 1
            self.config(width=self.text_size + 1 if self.text_size > 4 else 4)

    def update_yview(self):
        self.yview_moveto(self.text_block.yview()[0])
