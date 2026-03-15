window_width_height = "600x400"

def generate_window(tk, name = "My App", other_size = None): 
 window = tk.Tk()
 window.title(name)
 window.geometry(other_size if other_size else window_width_height)
 return window