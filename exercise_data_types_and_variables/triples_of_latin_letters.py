n=int(input())
for first_letter in range(n):
    for second_letter in range(n):
        for third_letter in range(n):
            print(f"{chr(first_letter+97)+chr(second_letter+97)+chr(third_letter+97)}")