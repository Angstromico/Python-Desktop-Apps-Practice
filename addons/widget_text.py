import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def widget_text_app(): 
    root = tk.Tk()
    root.title("Weyland-Yutani Confidential Terminal")
    root.geometry("600x500")
    root.configure(bg="#1a1a1a")

    st = ScrolledText(
        root, 
        width=50, 
        height=15, 
        bg="#000000", 
        fg="#00ff00", 
        insertbackground="white",
        font=("Courier", 12)
    )
    st.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)

    st.tag_config("censored", background="black", foreground="black")

    def redact_content():
        keywords = ["Xenomorph", "Pyramid Head", "Alchemilla", "Confidential", "Incident"]
        
        for word in keywords:
            start_pos = "1.0"
            while True:
                start_pos = st.search(word, start_pos, stopindex=tk.END, nocase=True)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                st.tag_add("censored", start_pos, end_pos)
                start_pos = end_pos

    def clear_redaction():
        st.tag_remove("censored", "1.0", tk.END)

    btn_frame = tk.Frame(root, bg="#1a1a1a")
    btn_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)

    redact_btn = tk.Button(
        btn_frame, 
        text="REDACT CLASSIFIED INFO", 
        command=redact_content,
        bg="#cc0000", 
        fg="white", 
        font=("Arial", 10, "bold")
    )
    redact_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(
        btn_frame, 
        text="DECRYPT", 
        command=clear_redaction,
        bg="#444444", 
        fg="white"
    )
    clear_btn.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    widget_text_app()