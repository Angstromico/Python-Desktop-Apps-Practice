# Python Desktop Apps Practice

This repository is dedicated to practicing and developing desktop applications using Python. It serves as a learning environment for exploring various GUI frameworks and desktop application development patterns.

## Purpose

The goal of this repository is to:

- Practice building desktop applications with Python
- Experiment with different GUI frameworks (Tkinter, PyQt, Kivy, etc.)
- Learn desktop application architecture and design patterns
- Develop a collection of small, focused applications and utilities

## Structure

```
PyExel/
├── README.md                 # This file
├── app.py                   # Main entry point - imports and runs selected apps
├── addons/                   # Desktop applications and utilities
│   ├── basic_app.py        # Basic Tkinter application (first example)
│   └── [future apps...]     # Additional desktop applications
└── [other files...]         # Data files, resources, etc.
```

## Getting Started

### Running Apps

To run applications, use the main entry point `app.py`:

```bash
python app.py
```

The main `app.py` file imports and runs the selected app from the `addons` folder. You can change which app runs by modifying the import statement in the `main()` function.

### Running Multiple Apps

When running multiple Tkinter apps, you have several options:

#### Sequential Running

Apps run one after another (close one to see the next):

```bash
python app_sequential.py
```

#### Parallel Running

All apps open simultaneously using threading:

```bash
python app_parallel.py
```

#### Controlled Running

Mixed approach with manual window control:

```bash
python app_controlled.py
```

**Note**: Tkinter's `window.mainloop()` is a blocking call. This means apps will run sequentially by default. Use threading to run multiple apps simultaneously.

### Running Individual Apps

You can also run individual apps directly from the addons folder:

```bash
python addons/basic_app.py
```

This basic application demonstrates:

- Window creation and configuration
- Widget placement (labels, entry fields, buttons)
- Event handling and user interaction
- Input validation and dynamic UI updates

### Sales Data Analyzer

The repository now includes a dedicated Sales Data interface:

- `addons/sales_data.py`
- `addons/README_sales_data.md`

It reads `SalesData.xlsx` and allows interactive queries for top/worst values by group with customizable N, filtering, and export.

```bash
python app.py  # also runs the existing examples and then the sales data app
```

Detailed usage and options are available in `addons/README_sales_data.md`.

## Future Development

As you progress through desktop application development, this repository will grow with:

- More complex applications
- Different GUI frameworks
- Database integration
- File handling utilities
- System integration tools

## Requirements

- Python 3.x
- Standard library modules (tkinter comes pre-installed with most Python distributions)

## Contributing

This is a personal practice repository. Feel free to use it as inspiration for your own desktop application learning journey.
