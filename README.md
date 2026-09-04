# PyBrowser

A custom browser wrapper using Python and PyQt6 that natively renders HTML and CSS while replacing standard JavaScript execution with a custom native Python execution engine.

## Features
- **No JavaScript**: Standard `<script>` tags are completely stripped and ignored.
- **Python Scripts**: `<script type="text/python">` tags are parsed and executed natively in Python when the page loads.
- **Python Bridge**: Use `onclick="python:my_function()"` in your HTML to directly invoke native Python functions without any JS intermediaries in your code.

## Prerequisites

- Python 3.10+
- PyQt6
- PyQt6-WebEngine

## Installation

Install the required dependencies using pip:

```bash
pip install PyQt6 PyQt6-WebEngine
```

## Running the Prototype

To start the browser and load the test page:

```bash
python browser_engine.py
```

The browser will open `test_page.html`. 
1. Check your terminal to see the `print()` statement from the embedded Python script during page load.
2. Click the "Fetch System Data" button in the browser to execute the `fetch_system_data()` Python function and see its output in your terminal.
