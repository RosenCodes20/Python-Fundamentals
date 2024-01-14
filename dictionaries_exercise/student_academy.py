num = int(input())
students = {}
for i in range(num):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

for student,grades in students.items():

    if sum(grades) / len(grades) >= 4.50:
        print(f"{student} -> {sum(grades) / len(grades):.2f}")