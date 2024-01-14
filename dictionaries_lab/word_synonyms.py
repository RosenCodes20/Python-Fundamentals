n = int(input())
my_dict = {}

for lines in range(n):
    word = input()
    synonym = input()

    if word in my_dict:
        my_dict[word].append(synonym)
    else:
        my_dict[word] = [synonym]

for k,v in my_dict.items():

    splitted_value = ", ".join(v)
    print(f"{k} - {splitted_value}")
