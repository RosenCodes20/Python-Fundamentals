words = input().replace(" ","")

word_dict = {}

for word in words:
    word_dict[word] = word_dict.get(word,0) + 1
for k,v in word_dict.items():
    print(f"{k} -> {v}")