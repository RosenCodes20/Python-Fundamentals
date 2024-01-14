number = int(input())
for cur_number in range(1, number + 1):
    num_int_str = str(cur_number)
    sum_of_the_numbers = 0
    for digits in num_int_str:
        sum_of_the_numbers += int(digits)
    is_special = False
    if sum_of_the_numbers == 5 or sum_of_the_numbers == 7 or sum_of_the_numbers == 11:
        is_special = True
    print(f"{cur_number} -> {is_special}")
