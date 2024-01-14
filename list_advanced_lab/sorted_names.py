def names():
    names_list = [name for name in input().split(", ")]

    sorted_list = sorted(names_list, key=lambda x: (-len(x), x) )

    return sorted_list


print(names())
