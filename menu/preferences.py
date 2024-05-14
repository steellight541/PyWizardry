from tkinter import Menu


class MyPreferencesMenu(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.add_cascade(label="Styles", menu=MyStylesMenu(master))
        self.add_cascade(label="Zen Mode", menu=MyZenModeMenu(master))


class MyZenModeMenu(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.iszen = False
        self.add_command(label="Toggle Vim Mode", command=self.toggle_zen_mode)

    def toggle_zen_mode(self):
        self.iszen = not self.iszen
        self.master.attributes("-fullscreen", self.iszen)  # type: ignore


class MyStylesMenu(Menu):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.add_cascade(label="Themes", menu=MyThemesMenu(master))
        self.add_cascade(label="Font", menu=MyFontMenu(master))


class MyThemesMenu(Menu):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.add_command(label="Light Theme", command=self.set_light_theme)
        self.add_command(label="Dark Theme", command=self.set_dark_theme)

    def set_line_numbers(self, fg, bg):
        self.master.text_block.lines_counter.config(fg=fg, bg=bg)  # type: ignore

    def set_text_block(self, fg, bg):
        self.master.text_block.config(fg=fg, bg=bg)  # type: ignore

    def set_cursor_color(self, color):
        self.master.text_block.config(insertbackground=color)

    def set_light_theme(self):
        self.set_cursor_color("black")
        self.set_line_numbers("black", "lightgrey")
        self.set_text_block("black", "white")

    def set_dark_theme(self):
        self.set_cursor_color("lightgrey")
        self.set_line_numbers("lightgrey", "black")
        self.set_text_block("white", "black")


class MyFontMenu(Menu):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.add_command(label="Consolas", command=self.set_consolas)
        self.add_command(label="Arial", command=self.set_arial)

    def set_font(self, font):
        self.master.text_block.config(font=font)  # type: ignore

    def set_consolas(self):
        self.set_font(("Consolas", 12))

    def set_arial(self):
        self.set_font(("Arial", 12))