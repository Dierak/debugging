#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

def print_usage():
    print("Usage: ./script_name.py <number>")
    print("Calculate the factorial of a given number.")

if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments.")
    print_usage()
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Error: Invalid argument. Please provide a valid integer.")
    print_usage()
    sys.exit(1)

if number < 0:
    print("Error: Factorial is not defined for negative numbers.")
    sys.exit(1)

result = factorial(number)
print(result)

