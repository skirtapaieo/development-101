def positive_even_squares(*args):
    # Combine all lists into one list using list comprehension
    combined = [item for sublist in args for item in sublist]
    # Filter out only even and positive numbers and then square them using map and lambda functions
    result = list(map(lambda x: x**2, filter(lambda x: x > 0 and x % 2 == 0, combined)))
    return result

# Testing the function
print(positive_even_squares([-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]))
