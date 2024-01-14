strings = input().split()
palindrome_in_strings = input()
found_palindrome = 0
palindromes_list = []

for words in strings:
    if words == words[::-1]:
        palindromes_list.append(words)


print(palindromes_list)
print(f"Found palindrome {palindromes_list.count(palindrome_in_strings)} times")
