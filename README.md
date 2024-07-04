

# convert_to_exe.py

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

## Overview
This Python script automates the conversion of a designated Python file into a standalone executable (.exe) using PyInstaller. It includes error handling to verify file existence and validity before initiating the conversion process.

## Features
- Converts a Python script into a self-contained `.exe` file for easy distribution.
- Verifies the existence and validity of the specified Python file path.
- Provides clear feedback on successful conversion or encountered errors.

## Usage
1. **Prerequisites:**
   - Ensure Python and PyInstaller are installed on your system.

2. **Setup:**
   - Update the `python_file_dir` variable in the script with the path to your Python file.

3. **Execution:**
   - Run the script in your command-line interface:
     ```bash
     python convert_to_exe.py
     ```

4. **Output:**
   - Upon successful conversion, a single `.exe` file will be generated in the same directory as the original Python script.

## Example
```bash
python convert_to_exe.py
```

## Requirements
- Python (version 3.6 or higher recommended)
- PyInstaller (install via `pip install pyinstaller`)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## Author
- ADITYA KUMAR JHA

