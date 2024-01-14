def perfect_numbers(number):
    num_sum = 0
    for num in range(1, number):
        if number % num == 0:
            num_sum += num
    if number == num_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


nums = int(input())
print(perfect_numbers(nums))
