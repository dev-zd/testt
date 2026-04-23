import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 70, 90, 60]
}

df = pd.DataFrame(data)

# 1️⃣ Find average marks
average = df["Marks"].mean()
print("Average Marks:", average)

# 2️⃣ Print students with marks > 80
high_marks = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:")
print(high_marks)