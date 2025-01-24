def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
data = []
average = calculate_average(data)