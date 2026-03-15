import tkinter as tk
from addons.generals import generate_window

def radio_button_app(): 
    windows = generate_window(tk, "Radio Button")

    rad1 = tk.Radiobutton(windows, text='First', value=1)
    rad2 = tk.Radiobutton(windows, text='Second', value=2)
    rad3 = tk.Radiobutton(windows, text='Third', value=3)

    rad1.grid(column=0, row=0, padx=5, pady=5)
    rad2.grid(column=1, row=0, padx=5, pady=5)
    rad3.grid(column=2, row=0, padx=5, pady=5)

    windows.mainloop()


if __name__ == "__main__":
    radio_button_app()
