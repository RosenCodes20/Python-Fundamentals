text = input()

sorted_text = [char for char in text if char.lower() not in ("a", "o", "u", "i", "e")]

print("".join(sorted_text))
