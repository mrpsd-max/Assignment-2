# 🐍 Python Basics – Two Tasks in One Script  

This repository contains two beginner-friendly Python tasks that demonstrate **input handling, conditionals, loops, and error handling**.  

---

## 📌 Task 1: Check if a Number is Even or Odd  

### 📝 Description  
This task takes an integer input from the user and determines if it is **even** or **odd**.  

### 💻 Code Snippet  
```python
try:
    number = int(input("Enter an integer: "))
    
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")
```

## 📌 Task 2: Calculate the Sum of Integers from 1 to 50
### 📝 Description

- This task calculates the sum of all integers from 1 to 50 using a for loop.

### 💻 Code Snippet
```bash
total_sum = 0

for number in range(1, 51):
    total_sum += number

print(f"The sum of numbers from 1 to 50 is: {total_sum}")
```

## 🚀 How to Run

- Make sure you have Python 3 installed

- Save the code as tasks.py

- Open a terminal/command prompt in the same folder

### Author:
- Purusottam Dash
- Email: purusottamdash0@gmail.com