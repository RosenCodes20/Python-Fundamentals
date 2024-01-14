people_dict = {}
number_people = 0
users = {}
names_list = []
points_list = []
while True:

    lines = input()
    if lines == "no more time":
        break

    username, contest, points = lines.split(" -> ")

    if contest not in people_dict:
        people_dict[contest] = {}
    if username not in people_dict[contest]:
        people_dict[contest][username] = 0
    if people_dict[contest][username] < int(points):
        people_dict[contest][username] = int(points)


for contests in people_dict.keys():
    print(f"{contests}: {len(people_dict[contests].keys())} participants")
    for i, (username, points) in enumerate(sorted(people_dict[contests].items(),key=lambda x: (-x[1], x[0])),1):
        if username not in users:
            users[username] = 0
        users[username] += int(points)

        print(f"{i}. {username} <::> {int(points)}")
print(f"Individual standings:")
for i, (key, value) in enumerate(sorted(users.items(), key=lambda x: (-x[1], x[0])), 1):
     print(f"{i}. {key} -> {value}")