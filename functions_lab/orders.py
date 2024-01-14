products = input()
multiply = int(input())


def orders(product):
    if product == "coffee":
        return f"{1.5 * multiply:.2f}"
    elif product == "water":
        return f"{1 * multiply:.2f}"
    elif product == "coke":
        return f"{1.4 * multiply:.2f}"
    elif product == "snacks":
        return f"{2 * multiply:.2f}"


print(orders(products))
