import threading
import time

def main():
    from addons.checkbox import checkbox_app
    from addons.combobox import combobox_app
    from addons.widget_text import widget_text_app
    from addons.radio_button import radio_button_app

    print("Running all apps at the same time...")
    
    # List of apps to run
    apps = [
        ("Radio Button", radio_button_app),
        ("Checkbox", checkbox_app),
        ("Combobox", combobox_app),
        ("Widget Text", widget_text_app)
    ]
    
    # Create and start threads for each app
    threads = []
    for name, app_func in apps:
        thread = threading.Thread(target=app_func, daemon=True)
        threads.append(thread)
        thread.start()
        time.sleep(0.1)  # Small delay between window appearances
        print(f"Started {name} app")
    
    print("All apps started! Close windows to exit.")
    
    # Wait for all threads to complete (when windows are closed)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
