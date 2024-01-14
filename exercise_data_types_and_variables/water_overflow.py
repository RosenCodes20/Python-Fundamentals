number_of_lines = int(input())
capacity = 255
sum_litres = 0
for lines in range(number_of_lines):
    litres_of_water = int(input())
    if capacity - litres_of_water < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litres_of_water
    sum_litres += litres_of_water
print(sum_litres)
