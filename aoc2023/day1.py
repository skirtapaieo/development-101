# Advent of Code 2023, Day 1: Trebuchet


def calculate_calibration_value(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) < 2:
        return 0
    calibration_value = int(digits[0] + digits[-1])
    print(f"Line: {line.strip()}, Digits: {digits}, Value: {calibration_value}")

    return calibration_value


# Read the puzzle input from the file provided by Advent of Code
with open("day1-puzzle-input.txt", "r") as file:
    lines = file.readlines()

# Calculate the calibration value for each line and sum the results
total_calibration_value = sum(calculate_calibration_value(line) for line in lines)

# Print the total calibration value
print(total_calibration_value)
