
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print("Student Average Marks")
    print("-" * 40)

    for student in reader:
        name = student["Name"]

        marks = [
            float(student["Maths"]),
            float(student["Science"]),
            float(student["English"])
        ]

        average = sum(marks) / len(marks)

        print(f"Name: {name}, Average Marks: {average:.2f}")
