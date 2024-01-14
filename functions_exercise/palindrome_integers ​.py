def palindrome_numbers(numbers):
    return numbers == (numbers[::-1])


nums = input().split(", ")
for nums in nums:
    print(palindrome_numbers(nums))

