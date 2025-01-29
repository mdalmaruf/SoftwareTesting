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
    [-60, 20, 160],  # Out-of-bound values (should be ignored)
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


