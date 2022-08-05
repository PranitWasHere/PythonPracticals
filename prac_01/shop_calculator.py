total_price = 0
number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price = (total_price+price)
print(f"Total price for {number_of_items} items is ${total_price}")


