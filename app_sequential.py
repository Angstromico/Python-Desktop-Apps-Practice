def main():
    from addons.checkbox import checkbox_app
    from addons.combobox import combobox_app
    from addons.widget_text import widget_text_app
    from addons.radio_button import radio_button_app

    print("Running apps one by one...")
    print("1. Radio button app (close it to continue)")
    radio_button_app()

    print("2. Checkbox app (close it to continue)")
    checkbox_app()
    
    print("3. Combobox app (close it to continue)")
    combobox_app()
    
    print("4. Widget text app (close it to continue)")
    widget_text_app()

    print("5. Sales Data app (close it to continue)")
    from addons.sales_data import sales_data_app
    sales_data_app()
    
    print("All apps completed!")


if __name__ == "__main__":
    main()
