def main():
    from addons.exes import combobox_app, run_app, checkbox_app, radio_button_app, widget_text_app
    from addons.sales_data import sales_data_app

    widget_text_app()
    radio_button_app()
    checkbox_app()
    combobox_app()
    run_app()
    sales_data_app()


if __name__ == "__main__":
    main() 
