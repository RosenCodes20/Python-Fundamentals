def even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


nums = input().split()
lst = []
for num in nums:
    lst.append(int(num))
res=[]
for numbers in lst:
    if even_numbers(numbers):
        res.append(numbers)
final_res = list(filter(even_numbers,res))
print(final_res)
