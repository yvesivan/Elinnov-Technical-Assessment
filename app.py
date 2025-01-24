import streamlit as st
import math

# Cache the results of factorial calculations to avoid redundant work
# Using Streamlit's @st.cache_data decorator for memoization
@st.cache_data
def factorial(number):
    try:
        # Factorial is not defined for negative numbers, so return a message for negative inputs
        if number < 0:
            return "Undefined (negative numbers)"
        # If number is 0 or 1, return 1 as factorial of 0 and 1 is always 1
        if number == 0 or number == 1:
            return 1
        # Use an iterative approach to calculate factorial
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result
    except ValueError as e:
        return str(e)  # Return any error message as a string

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# Streamlit UI
st.title("Prime Number Checker and Optimized Factorial Calculator")

# User input for number
number = st.number_input("Enter a number:", min_value=0, max_value=10000, step=1)

# Button to check if the number is prime
if st.button("Check Prime"):
    if is_prime(number):
        st.success(f"{number} is a Prime Number.")
    else:
        st.error(f"{number} is not a Prime Number.")

# Button to calculate the factorial of the number
if st.button("Find Factorial"):
    # Call the factorial function, which is memoized
    result = factorial(number)
    st.info(f"The Factorial of {number} is {result}.")
