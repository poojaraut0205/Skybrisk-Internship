# Week 2: Data Structures and Functions

# Lists, Tuples, Sets, Dictionaries
numbers = [1, 2, 3, 4, 5, 2, 3]
unique_numbers = set(numbers)
print("Original List:", numbers)
print("Unique Numbers (Set):", unique_numbers)

student = {
    "name": "Vaishnavi",
    "age": 24,
    "course": "IT"
}
print("Student Dictionary:", student)

print("--------------")

# Functions: Sum of Squares
def sum_of_squares(nums):
    total = 0
    for n in nums:
        total += n * n
    return total

print("Sum of Squares:", sum_of_squares(numbers))

print("--------------")

# Lambda Function
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

print("--------------")

# List Comprehension
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)

print("--------------")

# Client Project: Data Cleaning Script
data = [10, 20, 20, 30, 40, 40, 50]
cleaned_data = list(set(data))

filtered_data = [x for x in cleaned_data if x > 25]

print("Original Data:", data)
print("Cleaned Data (Duplicates Removed):", cleaned_data)
print("Filtered Data (>25):", filtered_data)
