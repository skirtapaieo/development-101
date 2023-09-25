import json
import os

# Initialize variables
subjects = ["math", "science", "history", "english", "geography"]
cumulative_subject_grades = {subject: 0 for subject in subjects}
subject_counts = {subject: 0 for subject in subjects}
student_averages = []
grade_level_totals = {i: [] for i in range(1, 9)}
num_students = 1000

# Process each student's report card
for i in range(num_students):
    with open(f"students/{i}.json", "r") as f:
        report_card = json.load(f)

    total_grade = 0
    for subject in subjects:
        grade = report_card[subject]
        total_grade += grade
        cumulative_subject_grades[subject] += grade
        subject_counts[subject] += 1

    average_grade = total_grade / len(subjects)
    student_averages.append((i, average_grade))  # (id, average)
    grade_level_totals[report_card['grade']].append(average_grade)

# Calculate and print required values
avg_student_grade = sum([avg for _, avg in student_averages]) / num_students
print(f'Average Student Grade: {avg_student_grade:.2f}')

subject_averages = {subject: cumulative_subject_grades[subject] / subject_counts[subject] for subject in subjects}
hardest_subject = min(subject_averages, key=subject_averages.get)
easiest_subject = max(subject_averages, key=subject_averages.get)
print(f'Hardest Subject: {hardest_subject}')
print(f'Easiest Subject: {easiest_subject}')

grade_level_averages = {grade: sum(grades) / len(grades) for grade, grades in grade_level_totals.items()}
best_performing_grade = max(grade_level_averages, key=grade_level_averages.get)
worst_performing_grade = min(grade_level_averages, key=grade_level_averages.get)
print(f'Best Performing Grade: {best_performing_grade}')
print(f'Worst Performing Grade: {worst_performing_grade}')

best_student_id, _ = max(student_averages, key=lambda x: x[1])
worst_student_id, _ = min(student_averages, key=lambda x: x[1])
print(f'Best Student ID: {best_student_id}')
print(f'Worst Student ID: {worst_student_id}')
