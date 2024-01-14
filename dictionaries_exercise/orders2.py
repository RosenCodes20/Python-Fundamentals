products_dict = {}

while True:

    current_product = input()
    if current_product == "buy":
        break

    product, price, quantity = current_product.split()

    if product not in products_dict:
        products_dict[product] = 0
    else:
        products_dict[product] += int(quantity)
        products_dict[product] += int(quantity) * float(price)
for products, quantities in products_dict.items():
    print(f"{products} -> {quantities:.2f}")
