menu = {
    'pizza' : 100,
    'pasta' : 60,
    'burger' : 50,
    'salad' : 30,
    'coffee' : 80,
}

print("Welcome to python restaurant")
print("pizza : 100rs\npasta : 60rs\nburger : 50rs\nsalad : 30rs\ncoffee : 80rs")

order_total = 0

item_1 = input("Enter the name of the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to order")

else:
    print(f"Ordered item {item_1} is not available")

another_order = input("Do you want to add another item? Yes/No")
if another_order == "Yes":
    item_2 = input("Enter the name of second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of items to pay {order_total} ")

    