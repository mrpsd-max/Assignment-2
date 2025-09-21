# Task 2: Sum of Integers from 1 to 50 Using a Loop

# Initialize sum
total_sum = 0

# 1. Uses a for loop to iterate over numbers from 1 to 50.
for number in range(1, 51): # range(1, 51) includes 1 and goes up to (but not including) 51
    # 2. Calculates the sum of all integers in this range.
    total_sum += number

# 3. Displays the final sum.
print(f"The sum of numbers from 1 to 50 is: {total_sum}")