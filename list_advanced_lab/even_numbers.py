numbers = list(map(int , input().split(", ")))

index = map(
    lambda x: x if numbers[x] % 2 == 0 else "don't",
    range(len(numbers))

)
indexes = list(filter(lambda b: b != "don't" , index))
print(indexes)