from tkinter.scrolledtext import ScrolledText
from tkinter import Text
from time import sleep


class MyTextBlock(ScrolledText):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(
            font=("Consolas", 12),
            width=1,
            wrap="none",
            endline="",
            undo=True,
        )
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
        self.bind("<Shift-Tab>", self.redo_tab)

        # ctrl + back to delete the previous word
        self.bind("<Control-BackSpace>", self.delete_previous_word)

    def redo_tab(self, event):
        self.delete_tab_at_front()
        return "break"

    def delete_tab_at_front(self):
        cursor_position = self.index("insert")
        line, column = map(int, cursor_position.split("."))
        line_text = self.get(f"{line}.0", f"{line}.end")
        if line_text.startswith(" " * 4):
            self.delete(f"{line}.0", f"{line}.4")

    def delete_previous_word(self, event):
        self.delete_previous_word_at_cursor()
        return "break"

    def delete_previous_word_at_cursor(self):
        cursor_position = self.index("insert")
        line, column = map(int, cursor_position.split("."))
        line_text = self.get(f"{line}.0", f"{line}.end")
        prev_word_start = self.find_previous_word_start(line_text, column)
        self.delete(f"{line}.{prev_word_start}", f"{line}.{column}")

    def find_previous_word_start(self, line_text, column):
        if column == 0:
            return 0
        for i in range(column - 1, -1, -1):
            if line_text[i] == " ":
                return i + 1
        return 0

    def tab(self, event):
        self.insert("insert", " " * 4)
        return "break"

    def undo(self, event):
        # MAKE IT SO THAT WHEN HOLDING IT DOWN IT KEEPS UNDOING BUT WITH A DELAY
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
