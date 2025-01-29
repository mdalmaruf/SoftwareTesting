```python
import statistics

def process_temperatures(temp_list):
    """Calculate min, max, and avg temperatures."""
    valid_temps = [float(temp) for temp in temp_list]

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

```
