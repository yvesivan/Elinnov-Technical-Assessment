import streamlit as st
import math

# Set the page configuration for dark theme
st.set_page_config(page_title="Prime Number and Factorial Checker", layout="wide", initial_sidebar_state="collapsed", theme="dark")

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
