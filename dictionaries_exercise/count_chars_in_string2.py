words = [char for char in input() if char != " "]

symbols = {}

for word in words:
    if word not in symbols:
        symbols[word] = 0
    symbols[word] += 1

for char,occurenses in symbols.items():
    print(f"{char} -> {occurenses}")