# Extremely inefficient code to sum a list of numbers

def inefficient_sum(numbers):
    result = 0

    # Nested loops that do nothing but waste time
    for i in range(10000000):  # Random large loop doing nothing
        for j in range(5000000):  # Another large loop that does nothing
            pass

    # Redundant sorting and reversing of the list
    numbers.sort()  # Sorting the numbers unnecessarily
    numbers.reverse()  # Reversing the list right after sorting it

    # Inefficient sum calculation by looping through the list multiple times
    for num in numbers:
        result += num  # Summing once
    for num in numbers:
        result += num  # Summing again
    for num in numbers:
        result += num  # Summing once more

    # Random and unnecessary print statements
    print("Processing numbers...")
    print("Calculating sum...")
    print("Total sum calculated.")

    return result

# Test with a random list of numbers
numbers = [1, 2, 3, 4, 5]
inefficient_sum(numbers)
