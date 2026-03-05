# Week 4: Data Visualization with Matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# Sample Dataset
data = {
    "Age": [20, 21, 22, 23, 24, 25, 26],
    "Marks": [65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.figure()
plt.scatter(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()

# Line Plot (Dashboard-style visualization)
plt.figure()
plt.plot(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks Line Plot")
plt.show()
