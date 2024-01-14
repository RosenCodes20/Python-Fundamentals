secret_message = input().split()
words,numbers = [],[]
for message in secret_message:
    number , letters = "",""
    for symbol in message:
        if symbol.isdigit():
            number+=symbol
        else:
            letters+=symbol
    numbers.append(int(number))
    if len(letters) != 1:
        letters = f"{letters[-1]}{letters[1:-1]}{letters[0]}"
    words.append(letters)
for s,x in zip(numbers,words):
    print(f"{chr(s)}{x}",end=" ")