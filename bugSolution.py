def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Correct Usage
data = [10, 20, 30]
average = calculate_average(data)
print(f"Average: {average}")
data = []
average = calculate_average(data)
print(f"Average of empty list: {average}")

#Alternative solution using try-except block
def calculate_average_try_except(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0