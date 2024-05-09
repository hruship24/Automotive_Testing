'''
Date : 24th April 2024
Desc :Task 4: You are tasked with creating a temperature converter program in Python
called temperature_converter.py. The program should take two command-line arguments:
the temperature value and the unit of measurement (Celsius or Fahrenheit).
It should convert the temperature to the other unit of measurement and print the converted value.
The program should handle cases where the user provides invalid input
(e.g., non-numeric temperature value or invalid unit). If the input is valid,
the program should perform the conversion and display the result. Write the Python program
to fulfill these requirements.
'''

import sys

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    if len(sys.argv) != 3:
        print("Usage: python temperature_converter.py <temperature_value> <unit>")
        return

    value = sys.argv[1]
    unit = sys.argv[2]

    try:
        value = float(value)
    except ValueError:
        print("Error: Invalid input. Please provide a numeric temperature value.")
        return

    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        print(f"{value} Celsius is equivalent to {fahrenheit} Fahrenheit.")
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        print(f"{value} Fahrenheit is equivalent to {celsius} Celsius.")
    else:
        print("Error: Invalid unit. Please specify either 'Celsius' or 'Fahrenheit'.")

temperature_converter()