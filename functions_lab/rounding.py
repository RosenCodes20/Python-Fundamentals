def rounding(number):
    return round(number)


num = input().split()
lst=[]
for nums in num:
    lst.append(rounding(round(float(nums))))
print(lst)
