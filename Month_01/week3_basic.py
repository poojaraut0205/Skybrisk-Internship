# Week 3: NumPy and Pandas for Data Manipulation

import numpy as np
import pandas as pd

# NumPy Array Operations
numbers = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", numbers)
print("Mean:", np.mean(numbers))
print("Sum:", np.sum(numbers))

print("--------------")

# Pandas DataFrame
data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [85, 90, None, 78, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("--------------")

# Client Project: Data Cleaning
# Remove missing values
cleaned_df = df.dropna()
print("DataFrame after removing missing values:")
print(cleaned_df)

print("--------------")

# Aggregation: Calculate average marks
average_marks = cleaned_df["Marks"].mean()
print("Average Marks:", average_marks)
