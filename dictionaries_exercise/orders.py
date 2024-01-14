products_dict = {}

while True:
    product = input()

    if product == "buy":
        break

    name, price, quantity = product.split()

    if name not in products_dict.keys():
        products_dict[name] = {'price':float(price),'quantity':int(quantity)}
    else:
        products_dict[name]['quantity'] += int(quantity)
        products_dict[name]['price'] = float(price)

for products, quantities in products_dict.items():
    final_price = quantities['price'] * quantities['quantity']
    print(f"{products} -> {final_price :.2f}")
