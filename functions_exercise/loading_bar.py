def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    num_division=number//10
    return f"{number}% [{num_division*'%'}{(10-num_division)*'.'}]\nStill loading..."


num=int(input())
print(loading_bar(num))
