# Import needed libraries
import streamlit as st  # For creating the graphical user interface
import math  # For mathematical operations like square root

# Cache the results of factorial calculations to optimize execution time
# The @st.cache_data decorator stores results to avoid recomputation
@st.cache_data
def factorial(number):
    """
    Calculates the factorial of a given number.
    Optimized using memoization to store previous results.

    Args:
        number (int): The input number for which factorial is computed.

    Returns:
        int or str: The factorial value, or an error message if the input is invalid.
    """
    # Factorial is undefined for negative numbers
    if number < 0:
        return "Undefined (negative numbers)"
    # The factorial of 0 and 1 is 1
    if number == 0 or number == 1:
        return 1
    # Use an iterative approach to calculate factorial
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def is_prime(number):
    """
    Determines if a given number is prime.
    Optimized to reduce the number of iterations using square root logic.

    Args:
        number (int): The input number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    # 2 is the only even prime number
    if number == 2:
        return True
    # Exclude other even numbers
    if number % 2 == 0:
        return False
    # Check divisors up to the square root of the number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


# Set up the graphical user interface with Streamlit
st.title("Prime Number Checker and Factorial Calculator")  # App title

# Allow the user to input a number using a numeric input field
number = st.number_input("Enter a number:", min_value=0, max_value=10000, step=1)

# Button to check if the number is prime
if st.button("Check Prime"):
    # Call the is_prime function and display the result
    if is_prime(number):
        st.success(f"{number} is a Prime Number.")  # Display success if prime
    else:
        st.error(f"{number} is not a Prime Number.")  # Display error if not prime

# Button to calculate the factorial of the number
if st.button("Find Factorial"):
    # Call the factorial function (cached for optimization)
    result = factorial(number)
    st.info(f"The Factorial of {number} is {result}.")  # Display the result
