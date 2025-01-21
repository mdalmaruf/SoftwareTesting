# This is about Lab 0. We are trying to learn about advanced python functionalites like dictionary, set, exception, class

## About Dictionary
A dictionary is collection of elements where we see the key value pairs.

```python

import random
import string

def generate_random_numbers():
    numbers = []
    for _ in range(3):
        number = random.randint(0, 10)
        numbers.append(number)
    return numbers

if __name__ == "__main__":
    random_numbers = generate_random_numbers()
    print(" random numbers:", random_numbers)


```
