import matplotlib.pyplot as plt

# Data
students = ["Arun", "Bina", "Chetan", "Divya", "Esha"]
marks = [75, 85, 90, 70, 95]

# 🔹 LINE GRAPH
plt.figure(figsize=(8,5))
plt.plot(students, marks, marker='o', linestyle='-', color='blue', label="Marks")

plt.title("Student Marks - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()


# 🔹 BAR CHART
plt.figure(figsize=(8,5))
plt.bar(students, marks, color='green')

plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


# 🔹 PIE CHART
plt.figure(figsize=(6,6))
plt.pie(marks, labels=students, autopct='%1.1f%%', startangle=90)

plt.title("Student Marks Distribution - Pie Chart")

plt.show()