def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return "Please enter a positive integer."
    fibonacci_series = [0, 1]
    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[:n]

# Ask the user for input
try:
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    result = generate_fibonacci(num)
    print("Fibonacci Series:", result)
except ValueError:
    print("Please enter a valid integer.")