def data_types(string,number):
    if string=="int":
        return f"{float(number) * 2:.0f}"
    elif string=="real":
        return f"{float(number) * 1.50:.2f}"
    else:
        return f"${number}$"


some_string=input()
num=input()
print(data_types(some_string,num))