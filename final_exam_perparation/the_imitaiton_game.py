encrypted_message = input()
command = input()

while command != "Decode":
    current_command = command.split("|")
    if current_command[0] == "Move":
        number_letters = int(current_command[1])
        encrypted_message = f"{encrypted_message[number_letters:]}{encrypted_message[:number_letters]}"
    elif current_command[0] == "Insert":
        index, value = int(current_command[1]), current_command[2]
        encrypted_message = f"{encrypted_message[:index]}{value}{encrypted_message[index:]}"
    elif current_command[0] == "ChangeAll":
        substring, replacement = current_command[1], current_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")