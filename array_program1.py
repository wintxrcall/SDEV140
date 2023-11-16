# Author - Renee Guldi
# SDEV140 - MJovanovich
# 11/13/2023-
"""
arrays_program1.py

This Python program allows the user to enter a series of numbers and then calculates and displays the sum and average of those numbers. The user can enter as many numbers as they want and stop entering numbers by typing 'q'.
"""
def calculate_average(numbers: list[float]) -> float:
    # Return the average of the provided list.
    if not numbers:
        return 0.0
    average = sum(numbers)/len(numbers)
    return average
    pass
    
def calculate_sum(numbers: list[float]) -> float:
    # Return the sum of the provided list.
    return sum(numbers)
    pass

def get_user_input() -> str:
    # Prompt the user for a number or 'q'.
    user_inputs = input("Enter a number (or 'q' to quit): ")
    return user_inputs
    pass

def print_average(average: float) -> None:
    # Print the average.
    print(f"The average is: {average}")
    pass
    
def print_sum(sum: float) -> None:
    # Print the sum.
    print(f"The sum is: {sum}")
    pass

def get_list_of_numbers() -> list[float]:
    numbers: list[float] = []

    while True:
        # TODO: Loop to get numbers from the user until quit.
        # Store numbers in array and return.
        user_inputs = get_user_input()
        if user_inputs == 'q':
            break
        try:
            number = float(user_inputs)
            numbers.append(number)
        except ValueError:
            print("Enter a valid number (or 'q' to quit): ")
    return numbers

def main():
    # TODO: uncomment one at a time to get working.
    numbers: list[float] = get_list_of_numbers()
    sum: float = calculate_sum(numbers)
    average: float = calculate_average(numbers)
    print_sum(sum)
    print_average(average)
    pass


if __name__ == "__main__":
    main()