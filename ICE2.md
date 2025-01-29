# ICE2: Temperature Sensor Processing

## Objective
Implement a Python program to process temperature sensor readings, ensuring validation and correct calculations using Boundary Value Analysis (BVA) and Robustness Testing.

## Instructions
- Complete the `validate_temperature` function to filter valid temperatures.
- Modify `process_temperatures` to ensure only valid values are considered.
- Implement exception handling where necessary.
- Test the program using different cases, including boundary and out-of-range values.

## Given Code
Students need to complete the missing parts.

```python
import statistics


def validate_temperature(value):
    # You have to complete this function
    return None


def process_temperatures(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    valid_temps = [float(temp) for temp in temp_list]
    # valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]

    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [-50],  # Lower boundary
    [150],  # Upper boundary
    [-49, 149],  # Values inside range
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)
```

## Expected Learning Outcomes
- Understand boundary value analysis and robustness testing.
- Learn how to validate user inputs effectively.
- Gain experience handling numerical data in Python.
- Apply debugging techniques to refine code functionality.

# Optional: Do you want to use GUI for user inputs?

```python
import PySimpleGUI as sg # You need to install this library
import statistics


def validate_temperature(value):
    # Students must complete this function
    return None


def process_temperatures(temp_list):
    valid_temps = [float(temp) for temp in temp_list]

    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# GUI Layout
sg.theme("DarkTeal6")

layout = [
    [sg.Text("Enter Temperature Readings (°C):")],
    [sg.InputText(key="-TEMP1-"), sg.InputText(key="-TEMP2-"), sg.InputText(key="-TEMP3-")],
    [sg.Button("Process"), sg.Button("Clear"), sg.Button("Exit")],
    [sg.Text("", size=(40, 1), key="-OUTPUT-")]
]

window = sg.Window("Temperature Sensor Processor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Process":
        temp_inputs = [values["-TEMP1-"], values["-TEMP2-"], values["-TEMP3-"]]
        result = process_temperatures(temp_inputs)
        window["-OUTPUT-"].update(result)

    if event == "Clear":
        window["-TEMP1-"].update("")
        window["-TEMP2-"].update("")
        window["-TEMP3-"].update("")
        window["-OUTPUT-"].update("")

window.close()

```

# Explanation of the Given Code

This code creates a **Graphical User Interface (GUI)** using the **PySimpleGUI** library to take three user inputs (temperature readings) and process them. The program calculates the **minimum, maximum, and average** temperatures based on the user’s input.

---

## Libraries Used

- **PySimpleGUI**: A lightweight and easy-to-use Python GUI library used to create the interface.
- **Other GUI libraries** such as **Tkinter, PyQt, and Kivy** could be used, but **PySimpleGUI** simplifies the process.
---

## How the GUI Works

### Creating the Window
```python
window = sg.Window("Temperature Sensor Processor", layout)
```
- This initializes a GUI window named "Temperature Sensor Processor".
- The layout variable defines the structure of the window (input fields, buttons, output text).

```python
if event == "Process":
    temp_inputs = [values["-TEMP1-"], values["-TEMP2-"], values["-TEMP3-"]]
    result = process_temperatures(temp_inputs)
    window["-OUTPUT-"].update(result)
```
- When the "Process" button is clicked:
    - The program retrieves values from the three input fields (-TEMP1-, -TEMP2-, -TEMP3-).
    - It processes the temperatures using the process_temperatures() function.
    - The result (Min, Max, Avg) is displayed in the output text area.
