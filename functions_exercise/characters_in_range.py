def ascii_table(string1, string2):
    chars = []
    for char in range(ord(string1) + 1, ord(string2)):
        chars.append(chr(char))
    return chars


str1 = input()
str2 = input()
print(" ".join(ascii_table(str1, str2)))
