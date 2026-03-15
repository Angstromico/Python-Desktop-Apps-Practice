import os
import zipfile
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk, messagebox


def _load_sales_data(xlsx_path="SalesData.xlsx"):
    if not os.path.exists(xlsx_path):
        raise FileNotFoundError(f"Could not find '{xlsx_path}'. Put it in the working folder.")

    with zipfile.ZipFile(xlsx_path, 'r') as z:
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            root = ET.fromstring(z.read('xl/sharedStrings.xml'))
            ns = {'a': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            for si in root.findall('a:si', ns):
                text_pieces = [t.text or '' for t in si.findall('.//a:t', ns)]
                shared_strings.append(''.join(text_pieces))

        sheet_file = None
        for candidate in ['xl/worksheets/sheet1.xml', 'xl/worksheets/sheet.xml']:  # safe fallback
            if candidate in z.namelist():
                sheet_file = z.read(candidate)
                break

        if sheet_file is None:
            raise ValueError('No worksheet found in the workbook.')

        root = ET.fromstring(sheet_file)
        ns = {'a': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

        rows = []
        for row in root.findall('a:sheetData/a:row', ns):
            row_values = []
            for c in row.findall('a:c', ns):
                cell_type = c.get('t')
                cell_value = c.find('a:v', ns)
                if cell_value is None:
                    row_values.append('')
                    continue
                v = cell_value.text
                if cell_type == 's':
                    try:
                        row_values.append(shared_strings[int(v)])
                    except Exception:
                        row_values.append(v)
                else:
                    row_values.append(v)
            rows.append(row_values)

        if not rows:
            return []

        header = [str(cell).strip() for cell in rows[0]]

        data = []
        for row in rows[1:]:
            if all((cell == '' or cell is None) for cell in row):
                continue
            row_dict = {}
            for i, col in enumerate(header):
                if i < len(row):
                    value = row[i]
                else:
                    value = ''
                row_dict[col] = value
            data.append(row_dict)

        return data


def _to_float(value):
    if value is None or value == '':
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace('$', '').replace(',', '').strip())
    except Exception:
        return 0.0


def _build_summary(data, group_by, value_field='Total Sale Amount'):
    summary = {}
    for row in data:
        key = row.get(group_by)
        if key is None or str(key).strip() == '':
            continue
        amount = _to_float(row.get(value_field, 0))
        summary[key] = summary.get(key, 0.0) + amount
    return summary


def _format_results(sorted_items, top_n):
    lines = [f"Rank\tName\tTotal Sale Amount"]
    for idx, (group, amount) in enumerate(sorted_items[:top_n], start=1):
        lines.append(f"{idx}\t{group}\t{amount:,.2f}")
    return '\n'.join(lines)


def sales_data_app():
    window = tk.Tk()
    window.title('Sales Data Top/Worst Analyzer')
    window.geometry('900x700')

    frame = ttk.Frame(window, padding=10)
    frame.pack(fill='both', expand=True)

    try:
        sales_data = _load_sales_data('SalesData.xlsx')
    except Exception as e:
        messagebox.showerror('SalesData Load Error', str(e))
        sales_data = []

    columns = ['Sales Representative', 'Customer', 'Location', 'Product']
    for c in columns:
        if not any(c == k for k in (sales_data[0].keys() if sales_data else [])):
            pass

    row_opts = [('Top', 'desc'), ('Worst', 'asc')]

    ttk.Label(frame, text='SalesData.xlsx file loaded:').grid(column=0, row=0, sticky='w')
    ttk.Label(frame, text=f'{len(sales_data)} rows').grid(column=1, row=0, sticky='w')

    ttk.Label(frame, text='Group by:').grid(column=0, row=1, sticky='w', pady=(10, 0))
    group_var = tk.StringVar(value='Sales Representative')
    group_cb = ttk.Combobox(frame, values=columns, textvariable=group_var, state='readonly', width=30)
    group_cb.grid(column=1, row=1, sticky='w', pady=(10, 0))

    ttk.Label(frame, text='Choose measure:').grid(column=0, row=2, sticky='w')
    measure_var = tk.StringVar(value='Total Sale Amount')
    measure_cb = ttk.Combobox(frame, values=['Total Sale Amount', 'Quantity', 'Price'], textvariable=measure_var, state='readonly', width=30)
    measure_cb.grid(column=1, row=2, sticky='w')

    ttk.Label(frame, text='Order:').grid(column=0, row=3, sticky='w')
    order_var = tk.StringVar(value='Top')
    order_cb = ttk.Combobox(frame, values=[o[0] for o in row_opts], textvariable=order_var, state='readonly', width=30)
    order_cb.grid(column=1, row=3, sticky='w')

    ttk.Label(frame, text='Show N results:').grid(column=0, row=4, sticky='w')
    n_var = tk.StringVar(value='10')
    n_entry = ttk.Entry(frame, textvariable=n_var, width=10)
    n_entry.grid(column=1, row=4, sticky='w')

    ttk.Label(frame, text='Optional filter by Region (substring):').grid(column=0, row=5, sticky='w', pady=(10,0))
    filter_var = tk.StringVar()
    filter_entry = ttk.Entry(frame, textvariable=filter_var, width=50)
    filter_entry.grid(column=1, row=5, sticky='w', pady=(10,0))

    results_text = tk.Text(frame, wrap='none', height=24)
    results_text.grid(column=0, row=7, columnspan=3, sticky='nsew', pady=(12, 0))

    scrollbar_y = ttk.Scrollbar(frame, orient='vertical', command=results_text.yview)
    scrollbar_y.grid(column=3, row=7, sticky='ns')
    results_text.configure(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(frame, orient='horizontal', command=results_text.xview)
    scrollbar_x.grid(column=0, row=8, columnspan=3, sticky='ew')
    results_text.configure(xscrollcommand=scrollbar_x.set)

    frame.rowconfigure(7, weight=1)
    frame.columnconfigure(2, weight=1)

    def generate_table():
        if not sales_data:
            messagebox.showwarning('No Data', 'Sales data not loaded or invalid.')
            return
        try:
            n = int(n_var.get())
            n = max(1, min(n, 1000))
        except ValueError:
            messagebox.showerror('Input Error', 'N must be a valid positive number.')
            return

        group_by = group_var.get() or 'Sales Representative'
        value_field = measure_var.get() or 'Total Sale Amount'
        order = order_var.get() or 'Top'
        region_filter = filter_var.get().strip().lower()

        filtered_data = []
        for row in sales_data:
            if region_filter:
                region_value = str(row.get('Region', '')).lower()
                if region_filter not in region_value:
                    continue
            filtered_data.append(row)

        if not filtered_data:
            results_text.delete('1.0', tk.END)
            results_text.insert(tk.END, 'No rows match filter criteria.')
            return

        summary = {}
        for row in filtered_data:
            key = str(row.get(group_by, 'Undefined'))
            value = _to_float(row.get(value_field, 0))
            summary[key] = summary.get(key, 0.0) + value

        if not summary:
            results_text.delete('1.0', tk.END)
            results_text.insert(tk.END, 'No summary generated (check headers).')
            return

        items = sorted(summary.items(), key=lambda x: x[1], reverse=(order == 'Top'))
        if order == 'Worst':
            items = sorted(summary.items(), key=lambda x: x[1])

        table = _format_results(items, n)

        results_text.delete('1.0', tk.END)
        results_text.insert(tk.END, f"Grouping: {group_by}\nAggregator: {value_field}\nOrder: {order} {n}\nRows considered: {len(filtered_data)}\n\n")
        results_text.insert(tk.END, table)

    btn_generate = ttk.Button(frame, text='Generate Table', command=generate_table)
    btn_generate.grid(column=0, row=6, pady=10, sticky='w')

    def save_csv():
        try:
            filepath = os.path.join(os.getcwd(), 'sales_summary.csv')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(results_text.get('1.0', tk.END))
            messagebox.showinfo('Saved', f'Results exported to {filepath}')
        except Exception as e:
            messagebox.showerror('Save Error', str(e))

    btn_save = ttk.Button(frame, text='Export to sales_summary.csv', command=save_csv)
    btn_save.grid(column=1, row=6, pady=10, sticky='w')

    window.mainloop()


def run_sales_data_app():
    return sales_data_app()


if __name__ == '__main__':
    sales_data_app()
