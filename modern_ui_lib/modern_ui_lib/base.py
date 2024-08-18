# modern_ui_lib/base.py
import tkinter as tk

class BaseWidget(tk.Widget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(style='Modern.TButton')

    def set_style(self, style):
        self.configure(style=style)
