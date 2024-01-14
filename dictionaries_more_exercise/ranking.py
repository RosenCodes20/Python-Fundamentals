contest_pass_succes = {}
points = {}
while True:
    courses = input()

    if courses == "end of contests":
        break

    course, password = courses.split(":")

    if course not in contest_pass_succes:
        contest_pass_succes[course] = password

while True:
    point = input()

    if point == "end of submissions":
        break

    contest, passwords, username, pointes = point.split("=>")
    pointes = int(pointes)

    if contest in contest_pass_succes.keys() and contest_pass_succes[contest] == passwords:
        if username not in points.keys():
            points[username] = {}
        if contest not in points[username] or pointes > points[username][contest]:
            points[username][contest] = pointes

total_points = {user: sum(pointas.values()) for user, pointas in points.items()}

best_person = max(total_points, key=total_points.get)

print(f"Best candidate is {best_person} with total {total_points[best_person]} points.")
print("Ranking:")

sorted_users = sorted(points.keys())
for users in sorted_users:
    print(users)
    for contests, pointus in sorted(points[users].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contests} -> {pointus}")
