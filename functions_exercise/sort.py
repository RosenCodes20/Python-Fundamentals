def sorted_list(number):
    sort=[]
    for num in number:
        sort.append(int(num))
    return sorted(sort)


nums=input().split()
print(sorted_list(nums))