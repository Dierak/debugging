#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer recursively.

    Parameters:
    - n (int): The integer for which the factorial is calculated.

    Returns:
    - int: The factorial of the given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate factorial of the integer provided as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)

