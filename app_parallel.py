import threading
import time

def main():
    from addons.checkbox import checkbox_app
    from addons.combobox import combobox_app
    from addons.basic_app import run_app
    from addons.radio_button import radio_button_app

    print("Running all apps at the same time...")
    
    # Create threads for each app
    threads = []

    # Start radio button app in separate thread
    t1 = threading.Thread(target=radio_button_app)
    t1.daemon = True  # Allow main program to exit even if thread is running
    threads.append(t1)
    t1.start()
    time.sleep(0.1)
    
    # Start checkbox app in separate thread
    t2 = threading.Thread(target=checkbox_app)
    t2.daemon = True  # Allow main program to exit even if thread is running
    threads.append(t2)
    t2.start()
    time.sleep(0.1)  # Small delay to ensure first window appears
    
    # Start combobox app in separate thread
    t3 = threading.Thread(target=combobox_app)
    t3.daemon = True
    threads.append(t3)
    t3.start()
    time.sleep(0.1)
    
    # Start basic app in separate thread
    t4 = threading.Thread(target=run_app)
    t4.daemon = True
    threads.append(t4)
    t4.start()
    
    print("All apps started! Close windows to exit.")
    
    # Wait for all threads to complete (when windows are closed)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
