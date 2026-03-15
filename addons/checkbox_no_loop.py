import tkinter as tk
from addons.generals import generate_window

def checkbox_app_no_loop(): 
    window = generate_window(tk, 'Checkbox App', "800x600")

    label = tk.Label(window, text="Check the boxes below...", font=("Arial Bold", 30))
    label.grid(column=0, row=0, padx=5, pady=5)
    label.pack()

    def show_code_lang_selection():
        languages = []
        
        if num1.get() == 1:
            languages.append("Python")
        if num2.get() == 1:
            languages.append("Java")
            
        if not languages:
            selection = "None of them"
        else:
            selection = " & ".join(languages)
            
        label.configure(text=f"You love to code in: {selection}")

    num1 = tk.IntVar()
    num2 = tk.IntVar()
    chk1 = tk.Checkbutton(window, text='Python', var=num1, onvalue=1, offvalue=0, command=show_code_lang_selection)
    chk1.pack()
    chk2 = tk.Checkbutton(window, text='Java', var=num2, onvalue=1, offvalue=0, command=show_code_lang_selection)
    chk2.pack()

    return window  # Return window instead of calling mainloop
