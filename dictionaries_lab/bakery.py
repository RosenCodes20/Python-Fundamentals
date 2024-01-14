foods = input().split()

stood = {}

for i in range(0,len(foods),2):

    keys = foods[i]

    values = int(foods[i+1])

    stood[keys] = values

print(stood)