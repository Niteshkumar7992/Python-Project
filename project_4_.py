menu = {
    "Pizza":   40,
    "Pasta":   50,
    "Burger":  60,
    "Salad":   70,
    "Coffee":  80,

}
# gread
print("Welcome to Python Restaurant")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger:Rs 60\nSalad: Rs 70\nCoffee: Rs 80")

order_total  = 0
# 80 + 70= 150
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]  #0 + 50
    print("Your item {item_1} has been added to tour order")


else:
    print(f"Ordered item {item_1} is not avialable yet!")

another_order  = input("Do you want to add another item ?(Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu :
        order_total += menu[item_2] 
        print("Item {item_2} has been added to order ")
    else:
        print(f"Ordered item  {item_2} is not avaialable! ")
        
    item_3 = input("Enter the name of third item = ")
    if item_3 in menu :
        order_total += menu[item_3] 
        print("Item {item_3} has been added to order ")
    else:
        print(f"Ordered item  {item_3} is not avaialable! ")
print(f"The total amount of item to pay is  {order_total}")

 








