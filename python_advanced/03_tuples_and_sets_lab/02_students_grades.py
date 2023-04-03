# https://judge.softuni.org/Contests/Practice/Index/1832#1

students_grades = {}
for _ in range(int(input())):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grades in students_grades.items():
    avg = sum(grades) / len(grades) if grades else 0
    marks = ' '.join([f"{mark:.2f}" for mark in grades])
    print(f"{student} -> {marks} (avg: {avg:.2f})")
