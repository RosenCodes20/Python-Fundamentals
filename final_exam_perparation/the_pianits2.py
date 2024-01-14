n = int(input())
pieces_dict = {}
for _ in range(n):
    piece, composer, key = input().split("|")

    if piece not in pieces_dict:
        pieces_dict[piece] = {"Composer": composer, "Key": key}

command = input()
while command != "Stop":
    current_command = command.split("|")
    if current_command[0] == "Add":
        piece, composer, key = current_command[1], current_command[2], current_command[3]
        if piece in pieces_dict:
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif current_command[0] == "Remove":
        piece = current_command[1]
        if piece in pieces_dict:
            pieces_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif current_command[0] == "ChangeKey":
        piece, new_key = current_command[1], current_command[2]
        if piece in pieces_dict:
            pieces_dict[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for pieces, composer_key in pieces_dict.items():
    print(f"{pieces} -> Composer: {composer_key['Composer']}, Key: {composer_key['Key']}")