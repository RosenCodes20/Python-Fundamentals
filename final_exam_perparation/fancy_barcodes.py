import re

n = int(input())

for i in range(n):
    barcodes = input()
    valid_barcodes = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    match = re.findall(valid_barcodes, barcodes)
    if match:
        found_nums = r"\d+"
        another_match = re.findall(found_nums, barcodes)
        if not another_match:
            print("Product group: 00")
        else:
            merge_nums = "".join(another_match)
            print(f"Product group: {merge_nums}")
    else:
        print("Invalid barcode")
