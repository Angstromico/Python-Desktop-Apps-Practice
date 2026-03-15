def main():
    from addons.checkbox import checkbox_app
    from addons.combobox import combobox_app
    from addons.basic_app import run_app

    print("Running apps one by one...")
    print("1. Checkbox app (close it to continue)")
    checkbox_app()
    
    print("2. Combobox app (close it to continue)")
    combobox_app()
    
    print("3. Basic app (close it to continue)")
    run_app()
    
    print("All apps completed!")


if __name__ == "__main__":
    main()
