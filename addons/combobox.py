import tkinter as tk
from tkinter import ttk
from addons.generals import window_width_height

def combobox_app(): 
    window = tk.Tk()
    window.title("Combobox App")
    window.geometry(window_width_height)
    lbl = tk.Label(window, text="Pick one option...", font=("Arial Bold", 30))
    lbl.grid(column=0, row=0, padx=5, pady=5)
    combo = ttk.Combobox(window, values=["Item 1", "Item 2", "Item 3", 4])
    combo_value = combo.get()
    combo.current(1)
    combo.grid(column=0, row=3, padx=5, pady=5)

    def clicked():
        lbl.configure(text="You picked: " + combo.get())

    btn = tk.Button(window, text="Click Me", command=clicked, bg="orange", fg="red")
    btn.grid(column=0, row=5, padx=5, pady=5)

    window.mainloop()


if __name__ == "__main__":
    combobox_app()
