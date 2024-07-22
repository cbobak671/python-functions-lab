
# Exercise 9: Basic Calculator

# Create a function named basicCalculator that takes three arguments:

# two numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, ‘divide’).

# Perform the provided operation on the two numbers. In operations where the order of numbers is important,

# treat the first parameter as the first operand and the second parameter as the second operand.

# Examples:

#basicCalculator(10, 5, ‘subtract’) should return 5.

#basicCalculator(10, 5, ‘add’) should return 15.

#basicCalculator(10, 5, ‘multiply’) should return 50.

#basicCalculator(10, 5, ‘divide’) should return 2.

# Define the function and then call it below.

def basic_calculator(num1, num2, operation):
    if operation == 'add': 
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return('Invalid. Enter a number greater than 0')
        else:
            return num1/num2
    else: 
        return('Enter a valid operation.')


print("Exercise 9 Result:", basic_calculator(10, 5, 'multiply')) #prints: "Exercise 9 Result: 50"
print("Exercise 9 Result:", basic_calculator(30, 100, 'exponent')) #prints: "Exercise 9 Result: Enter a valid operation."
print("Exercise 9 Result:", basic_calculator(30, 0, 'divide')) #prints: "Exercise 9 Result: Invalid. Enter a number greater than 0."