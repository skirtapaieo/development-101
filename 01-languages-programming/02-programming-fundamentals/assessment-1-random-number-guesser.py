import random

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_range():
    while True:
        start = get_input("Enter the start of the range: ")
        end = get_input("Enter the end of the range: ")
        if end < start:
            print("The end of the range must be greater than the start. Please try again.")
        else:
            return start, end

def guess_number():
    start, end = get_range()
    target = random.randint(start, end)
    guess_count = 0

    while True:
        guess = get_input("Guess a number: ")
        guess_count += 1
        '''
        if guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
        '''
        if guess == target:
            suffix = ""
            if guess_count > 1:
                suffix = "s"
            print(f"You guessed the number in {guess_count} attempt{suffix}")
            break

guess_number()
