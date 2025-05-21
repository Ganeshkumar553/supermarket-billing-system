from datetime import datetime

print(25 * "*", "Welcome to the Supermarket", 25 * "*")
name = input("Enter your name: ")

print("\nThe list of items in the supermarket:")
item_list = '''
Rice    Rs  20/kg
Sugar   Rs  30/kg
Salt    Rs  20/kg
Oil     Rs  80/litre
Paneer  Rs  110/kg
Maggi   Rs  50/kg
Boost   Rs  90/each
Colgate Rs  85/each
'''
print(item_list)

items = {
    'Rice': 20,
    'Sugar': 30,
    'Salt': 20,
    'Oil': 80,
    'Paneer': 110,
    'Maggi': 50,
    'Boost': 90,
    'Colgate': 85
}

ilist = []  
qlist = []  
plist = []  

while True:
    option = input("Press 1 to buy an item or 2 to exit: ")
    if option == '1':
        item = input("Enter the item name: ").capitalize()
        if item in items:
            try:
                quantity = float(input("Enter the quantity: "))
                if quantity <= 0:
                    print("Please enter a valid positive quantity.")
                    continue
                price = quantity * items[item]
                print(f"Price for {quantity} {item}(s): Rs {price}")
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            except ValueError:
                print("Invalid quantity entered. Please enter a number.")
        else:
            print("Sorry, we don't have that item.")
    elif option == '2':
        break
    else:
        print("Invalid option, please press 1 or 2.")

inp = input("Do you want to generate the bill? (yes/no): ").lower()
if inp == 'yes':
    print("\n" + 30 * "=")
    print(f"Bill for {name}")
    print("Date & Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(30 * "=")
    print(f"{'Item':10} {'Quantity':10} {'Price':10}")
    print(30 * "-")
    total_price = 0
    for i in range(len(ilist)):
        print(f"{ilist[i]:10} {qlist[i]:<10} Rs {plist[i]:<10.2f}")
        total_price += plist[i]
    print(30 * "-")
    print(f"{'Total':20} Rs {total_price:.2f}")
    print(30 * "=")
    print("Thank you for shopping with us!")
else:
    print("Thank you! Visit again.")

