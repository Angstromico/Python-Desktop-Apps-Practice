# Sales Data Analyzer (addons/sales_data.py)

This app reads `SalesData.xlsx` from the repository root and computes top/worst rankings by sales.

## Features

- Group by: `Sales Representative`, `Customer`, `Location`, `Product`
- Measure: `Total Sale Amount`, `Quantity`, `Price`
- Order: `Top` (highest sums) or `Worst` (lowest sums)
- Custom result count: `N` rows (e.g., 10)
- Optional region filter (substring match)
- Export analysis result to `sales_summary.csv`

## How to run

From project root:

```bash
python app.py           # run all widgets + sales data app
python app_sequential.py
python app_parallel.py
python app_controlled.py

# Run only sales data app directly
python -c "from addons.sales_data import sales_data_app; sales_data_app()"
```

## Notes

- Requires `SalesData.xlsx` in the same folder as the scripts (`PyExel/SalesData.xlsx`).
- No third-party package required; uses pure Python XLSX XML parsing.
- If the workbook is missing or malformed, an error dialog appears.
