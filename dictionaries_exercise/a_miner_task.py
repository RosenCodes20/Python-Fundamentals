resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())

    if current_resource not in resources.keys():
        resources[current_resource] = 0

    resources[current_resource] += quantity

for resource, quantities in resources.items():

    print(f"{resource} -> {quantities}")