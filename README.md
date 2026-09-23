# Multi-Utility Toolkit

**Author:** Shrey Shah

## Introduction

Multi-Utility Toolkit is a Python project that combines different useful operations into one menu-driven program.

The project uses multiple Python modules to perform date and time operations, mathematical calculations, random operations, UUID generation, file operations, and module attribute exploration using the `dir()` function.

## Features

The project provides the following options:

1. **Date and Time Operations**

   * Display current date and time
   * Calculate difference between two dates
   * Format dates into custom formats
   * Stopwatch
   * Countdown timer

2. **Mathematical Operations**

   * Factorial calculation
   * Compound interest
   * Trigonometric operations
   * Area of geometric shapes

3. **Random Operations**

   * Generate random numbers
   * Generate random lists
   * Create random passwords
   * Generate random OTPs

4. **Unique ID Operations**

   * Generate UUIDs for different modules
   * Uses `uuid.uuid3()` with `uuid.NAMESPACE_DNS`

5. **File Operations**

   * Create a new file
   * Write data to a file
   * Read a file
   * Append data to a file

6. **Explore Module Attributes**

   * Uses Python's `dir()` function
   * Displays the available attributes of different modules

7. **Logging**

   * Stores the module name
   * Stores the generated UUID
   * Stores the output produced by the selected operation
   * Saves the information in `save_logs_outputs.txt`

## Project Structure

```text
Multi-Utility Toolkit/
│
├── main.py
├── date_time_operations.py
├── mathematical_operations.py
├── random_operations.py
├── uuididentifier.py
├── customfile.py
├── explore_module_attributes.py
├── __init__.py
├── save_logs_outputs.txt
└── README.md
```

## Modules

### main.py

This is the main file of the project. It displays the main menu and allows the user to select different operations.

### date_time_operations.py

This module performs different date and time related operations such as date difference, formatting, stopwatch and countdown timer.

### mathematical_operations.py

This module performs mathematical calculations including factorial, compound interest, trigonometric operations and area calculations.

### random_operations.py

This module generates random numbers, random lists, random passwords and OTPs.

### uuididentifier.py

This module generates unique identifiers using Python's `uuid` module.

### customfile.py

This module performs file operations such as creating, reading, writing and appending files. It also saves the outputs and UUIDs into the log file.

### explore_module_attributes.py

This module uses the `dir()` function to explore the attributes available in different Python modules.

### **init**.py

This file is used to identify the project directory as a Python package.

## Technologies Used

* Python
* `datetime` module
* `time` module
* `math` module
* `random` module
* `uuid` module
* File handling
* Functions
* Modules
* `dir()` function

## How to Run

1. Make sure Python is installed on your computer.
2. Keep all the Python files in the same folder.
3. Open the folder in a Python editor or terminal.
4. Run:

```bash
python main.py
```

5. Select an option from the main menu.
6. Follow the instructions displayed by the program.

## Logging System

The project uses a logging function in `customfile.py`.

The log file is:

```text
save_logs_outputs.txt
```

The log contains information such as:

```text
File name: mathematical_operations
Output: Factorial = 120
Unique ID: example-uuid
--------------------------------
```

This helps keep a record of the operations performed by the toolkit.

## Learning Objectives

Through this project, I learned:

* How to create and use Python modules
* How to import modules
* How to create and call functions
* How to use `return` statements
* How to work with loops and conditional statements
* How to handle files in Python
* How to generate UUIDs
* How to use Python's `dir()` function
* How to create a menu-driven program
* How different modules can work together in one project

## Author

**Shrey Shah**

This project was created as a Python learning project to understand modular programming, functions, file handling and the use of built-in Python modules.
