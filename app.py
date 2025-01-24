import streamlit as st
import math

# Function to check if a number is prime
def is_prime(number):
    # Return False for numbers less than or equal to 1
    if number <= 1:
        return False
    # Check if the number is divisible by 2 (optimization to skip even numbers)
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # Check for divisibility from 3 to the square root of the number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# Function to calculate the factorial of a number
def factorial(number):
    # Factorial is not defined for negative numbers, so return a message for negative inputs
    if number < 0:
        return "Undefined (negative numbers)"
    # Use the math.factorial function to calculate the factorial
    return math.factorial(number)

# Streamlit UI
st.title("Prime Number and Factorial Checker")

# User input for number
number = st.number_input("Enter a number:", min_value=-10000, max_value=10000, step=1)

# Button to check if the number is prime
if st.button("Check Prime"):
    # Check if the number is prime and display the result
    if is_prime(number):
        st.success(f"{number} is a Prime Number.")
    else:
        st.error(f"{number} is NOT a Prime Number.")

# Button to calculate the factorial of the number
if st.button("Find Factorial"):
    # Calculate and display the factorial
    result = factorial(number)
    st.info(f"The Factorial of {number} is {result}.")
