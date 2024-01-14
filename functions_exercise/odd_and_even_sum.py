def odd_and_even_sum(number: str):
    odd_sum = 0
    even_sum = 0
    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)

        elif int(num) % 2 != 0:
            odd_sum += int(num)
    return even_sum, odd_sum


nums = input()
even_sums, odd_sums = odd_and_even_sum(nums)
print(f"Odd sum = {odd_sums}, Even sum = {even_sums}")
