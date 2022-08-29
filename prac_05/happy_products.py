print("Menu:")
print("(I)nstructions")
print("(C)alculate")
print("(Q)uit")
choice = str(input("Choice: ").upper())
while choice != "Q":
    if choice == "I":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off! ")
print("Menu:")
print("(I)nstructions")
print("(C)alculate")
print("(Q)uit")
choice = str(input("Choice: ").upper())
elif choice == "C":
    products = int(input("Number of products: "))
    while products < 0:
        print("Invalid input")
        products = int(input("Number of products: "))
    price = float(input("Price: "))
    while price <= 0:
        print("Invalid input")
        price = float(input("Price: "))
    total = products * price
    if products > 5:
        total = total * 0.9
    print("{} x ${} products = ${}. format(products, price, cost")
else:
    print("Invalid choice")
    print("Menu:")
    print("(I)nstructions")
    print("(C)alculate")
    print("(Q)uit")
    choice = str(input("Choice: ").upper ())
print("Farewell")






