import csv
import random

# Fictional Student Dataset Generator - CUL-CYB 371
NUM_STUDENTS = 30
DEPARTMENTS = [
    "Cybersecurity",
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Data Science",
]
LEVELS = [100, 200, 300, 400]

# Updated dataset headers
headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

data = []

for i in range(1, NUM_STUDENTS + 1):
    # Student ID format tailored to Cyber/CS department (e.g., CYB2026001)
    student_id = f"SEN2026{i:03d}"

    department = random.choice(DEPARTMENTS)
    level = random.choice(LEVELS)

    # Realistic attendance (70% - 98%) and exam scores (50% - 95%)
    attendance = round(random.uniform(70.0, 98.0), 2)
    avg_exam_score = round(random.uniform(50.0, 95.0), 2)

    data.append([student_id, department, level, attendance, avg_exam_score])

# Write data directly to CSV
filename = "fictional_student_dataset.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Dataset successfully created and saved as '{filename}' with {NUM_STUDENTS} student records!")