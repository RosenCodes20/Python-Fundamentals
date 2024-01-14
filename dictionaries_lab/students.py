my_dict = {}
current_course = None
students = []
while True:

    courses = input()

    if ":" not in courses:
        current_course = courses
        break

    name,ID,course = courses.split(":")

    students.append({'name':name,'ID':ID,'course':course})

for student in students:
    if current_course.startswith(student['course'][0:6]):
        print(f"{student['name']} - {student['ID']}")