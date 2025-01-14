def display():
    print("Hello INFT-1207 Classs")

def factorial(n):
    if n <= 0:
        print("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":

    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}.")
    display()





