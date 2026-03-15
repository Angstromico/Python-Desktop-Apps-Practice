def main():
    from addons.checkbox_no_loop import checkbox_app_no_loop
    from addons.combobox import combobox_app
    from addons.widget_text import widget_text_app
    from addons.radio_button import radio_button_app

    print("Running apps with manual control...")
    
    # Create windows without mainloop
    window1 = checkbox_app_no_loop()
    
    # For apps that still have mainloop, run them in separate threads
    import threading
    
    def run_combobox():
        combobox_app()
    
    def run_widget_text():
        widget_text_app()
    
    t1 = threading.Thread(target=radio_button_app, daemon=True)
    t2 = threading.Thread(target=run_combobox, daemon=True)
    t3 = threading.Thread(target=run_widget_text, daemon=True)
    
    t1.start()
    t2.start()
    t3.start()
    
    # Start main loop for the first window
    window1.mainloop()
    
    print("All apps running!")


if __name__ == "__main__":
    main()
