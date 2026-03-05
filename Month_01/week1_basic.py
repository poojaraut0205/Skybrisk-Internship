# Week 1: Python Basics Programs

# Temperature Converter (Celsius to Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("--------------")

# Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("--------------")

# Client Project: Average Temperature Calculation
temperatures = [30, 32, 29, 31, 33]
average_temp = sum(temperatures) / len(temperatures)
print("Average Temperature:", average_temp)
