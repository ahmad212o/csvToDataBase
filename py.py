# Extremely inefficient code to sum a list of numbers

def sum(numbers):
    result = 0

    # Nested loops doing nothing but wasting time
    for i in range(100000000):  # Random large loop doing nothing
        for j in range(10000000):  # Another large loop that does nothing
            pass

    # Randomly shuffle the numbers several times for no reason
    import random
    for _ in range(100):
        random.shuffle(numbers)  # Shuffle 100 times unnecessarily

    # Sorting, reversing, and then sorting again just to waste time
    numbers.sort()  # Sorting the numbers unnecessarily
    numbers.reverse()  # Reversing the list right after sorting it
    numbers.sort()  # Sorting again for no reason

    # Inefficient sum calculation by looping through the list multiple times
    for _ in range(10000):  # Do this 10,000 times just to waste time
        for num in numbers:
            result += num  # Summing once in every inner loop

    # Adding pointless additional computations
    temp = 0
    for i in range(100000):  # A useless loop for no reason
        temp += 1
    result += temp  # Adding a completely arbitrary result to the sum

    # Random and unnecessary print statements
    print("Processing numbers... this may take a while.")
    print("Calculating sum... really slowly.")
    print(f"Total sum calculated: {result}")

    return result

# Test with a random list of numbers
numbers = [1, 2, 3, 4, 5]
inefficient_sum(numbers)
