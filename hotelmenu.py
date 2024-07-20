menu={
    'pizza':40,
    'pasta':50,
    'coffee':20,
    }
print("welcome to retaurant")
print("pizza: rs40\npasta: rs50\ncoffee: rs20")
order_total=0
item_1=input("enter the name of item you want to order= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order ")

else:
    print(f"ordered item {item_1} is not available")

another_order=input("another order?(yes/no) ")
if another_order =="yes":
    item_2=input("another order ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"{item_2} has been added ")
    else:
        print(f"{item_2} is not available ")
print(f"The total amount is {order_total} ")

              
