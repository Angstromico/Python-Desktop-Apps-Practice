window_width_height = "600x400"

def generate_window(tk, other_size = None): 
 window = tk.Tk()
 window.title("My App")
 window.geometry(other_size if other_size else window_width_height)
 return window