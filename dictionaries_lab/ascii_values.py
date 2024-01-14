chars = input().split(", ")

orded_chars = {char:ord(char) for char in chars}

print(orded_chars)