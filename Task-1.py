# Task 1: Check if a Number is Even or Odd

# 1. Takes an integer input from the user.
try:
    number = int(input("Enter an integer: "))
    
    # 2. Checks whether the number is even or odd using an if-else statement.
    if number % 2 == 0:
        # 3. Displays the result accordingly.
        print(f"The number {number} is even.")
    else:
        # 3. Displays the result accordingly.
        print(f"The number {number} is odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")