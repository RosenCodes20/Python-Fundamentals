people = {}

while True:
    entry = input()

    if "-" not in entry:
        break
    name,number = entry.split("-")

    people[name] = number

num = int(entry)

for search in range(num):
    current_name = input()

    if current_name in people.keys():
        print(f"{current_name} -> {people[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")