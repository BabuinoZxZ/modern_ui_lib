# modern_ui_lib/styles.py
import tkinter as tk
from tkinter import ttk

class ModernStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure('Modern.TButton',
                       background='#4CAF50',
                       foreground='white',
                       font=('Helvetica', 12, 'bold'),
                       padding=10)
