courses = {}

while True:
    course = input()

    if course == "end":
        break

    softuni_course, name = course.split(" : ")

    if softuni_course not in courses:
        courses[softuni_course] = []

    courses[softuni_course].append(name)

for course_name, student in courses.items():
    print(f"{course_name}: {len(student)}")
    for students in student:
        print(f"-- {students}")
