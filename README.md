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
