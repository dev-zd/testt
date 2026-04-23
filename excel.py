import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book1.csv")

print(df)

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Graph")

plt.show()