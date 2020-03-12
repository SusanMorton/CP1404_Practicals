"""
program calculates total price for shopping cart items
if raw total over $100, 10% discount is applied
"""
item_price_total = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item " +str(i+1) + ": "))
    item_price_total = item_price_total + item_price

if item_price_total > 100:
    item_price_discount = item_price_total - (item_price_total * 0.10)
    print("Total price for " + str(number_of_items) + " items is: ${:.2f}".format(item_price_discount))
else:
    print("Total price for " + str(number_of_items) + " items is: ${:.2f}".format(item_price_total))

