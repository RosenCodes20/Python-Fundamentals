def min_number(numbers: list):
    min_list = []
    for num in numbers:
        min_list.append(int(num))
    return min(min_list)


def max_number(nums: list):
    max_list = []
    for num in nums:
        max_list.append(int(num))
    return max(max_list)


def sum_numbers(num: list):
    sum_list = []
    for nums in num:
        sum_list.append(int(nums))
    return sum(sum_list)


number = input().split()
minimum_number = min_number(number)

maximum_number = max_number(number)

sum_number = sum_numbers(number)

print(f"The minimum number is {minimum_number}")

print(f"The maximum number is {maximum_number}")

print(f"The sum number is: {sum_number}")