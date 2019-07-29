products = {}
while True:
    print("1.Add Product 2.Display Products 3:Search Product 4.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        product_id = input("Enter the ID:")
        product_name = input("Enter the Name:")
        products[product_id] = product_name

    elif ch == 2:
        if len(products) == 0:
            print("No products to be displayed")
        else:
            for k,v in products.items():
                print(f"{k}:{v}")


    elif ch == 3:
        search = input("Enter the product Id to be searches:")
        if products.get(search):
            print(f"Product id:{search} value:{products.get(product_id)}")
        else:
            print("Product ID is not present")

    else:
        break