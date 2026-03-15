import tkinter as tk
from addons.generals import generate_window

def run_app():
    window = generate_window(tk)

    input_text = tk.StringVar()

    lbl = tk.Label(window, text="Change the Text...", font=("Arial Bold", 30))
    lbl.grid(column=0, row=0, padx=10, pady=10)

    txt = tk.Entry(window, width=50, textvariable=input_text)
    txt.grid(column=0, row=1, padx=10, pady=10)

    def clicked():
        lbl.configure(text=input_text.get())

    def check_input(*args):
        if input_text.get().strip():
            btn.config(state="normal")
        else:
            btn.config(state="disabled")

    input_text.trace_add("write", check_input)

    btn = tk.Button(window, text="Click Me", command=clicked, bg="orange", fg="red", state="disabled")
    btn.grid(column=0, row=2, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_app()