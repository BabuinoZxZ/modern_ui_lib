# modern_ui_lib/widgets.py
from .base import BaseWidget

class ModernButton(BaseWidget):
    def __init__(self, master=None, text='', **kwargs):
        super().__init__(master, **kwargs)
        self.config(text=text)
