def numbers(num):
    return abs(num)


number = input().split()
lst = []
for nam in number:
    lst.append(abs(numbers(float(nam))))
print(lst)
