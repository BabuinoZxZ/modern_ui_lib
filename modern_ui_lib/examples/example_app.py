# examples/example_app.py
import tkinter as tk
from modern_ui_lib.widgets import ModernButton
from modern_ui_lib.styles import ModernStyle

def main():
    root = tk.Tk()
    style = ModernStyle()
    button = ModernButton(root, text='Clique Aqui')
    button.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
