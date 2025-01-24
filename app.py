import streamlit as st
import math

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Function to calculate the factorial of a number
def factorial(number):
    if number < 0:
        return "Undefined (negative numbers)"
    return math.factorial(number)

# Streamlit UI
st.title("Prime Number and Factorial Checker")

# User input for number
number = st.number_input("Enter a number:", min_value=-10000, max_value=10000, step=1)

# Button to check if the number is prime
if st.button("Check Prime"):
    if is_prime(number):
        st.success(f"{number} is a Prime Number.")
    else:
        st.error(f"{number} is NOT a Prime Number.")

# Button to calculate the factorial of the number
if st.button("Find Factorial"):
    result = factorial(number)
    st.info(f"The Factorial of {number} is {result}.")
