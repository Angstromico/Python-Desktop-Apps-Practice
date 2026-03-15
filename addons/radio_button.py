import tkinter as tk
from addons.generals import generate_window

def radio_button_app(): 
    windows = generate_window(tk, "Theme Selector Pro")

    selected_theme = tk.IntVar(value=1)

    main_label = tk.Label(windows, text="Select a System Theme", font=("Arial", 20), pady=20)
    main_label.grid(column=0, row=0, columnspan=3)

    def apply_theme():
        choice = selected_theme.get()
        
        if choice == 1: # Theme Dark
            windows.configure(bg="#2d2d2d")
            main_label.configure(bg="#2d2d2d", fg="#61afef", text="Hacker Mode On")
        elif choice == 2: # Theme Valencia (warming)
            windows.configure(bg="#ff9900")
            main_label.configure(bg="#ff9900", fg="white", text="Valencia Sunrise")
        elif choice == 3: # (Silent Hill vibe)
            windows.configure(bg="#555555")
            main_label.configure(bg="#555555", fg="#ff4444", text="Survival Horror")

    rad1 = tk.Radiobutton(windows, text='Dark Mode', value=1, variable=selected_theme, command=apply_theme)
    rad2 = tk.Radiobutton(windows, text='Orange Theme', value=2, variable=selected_theme, command=apply_theme)
    rad3 = tk.Radiobutton(windows, text='Retro Horror', value=3, variable=selected_theme, command=apply_theme)

    rad1.grid(column=0, row=2, padx=5, pady=5)
    rad2.grid(column=1, row=2, padx=5, pady=5)
    rad3.grid(column=2, row=2, padx=5, pady=5)

    apply_theme()

    windows.mainloop()


if __name__ == "__main__":
    radio_button_app()
