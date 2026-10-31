print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")
print(" ")

menu = ("""Taco Palace menu:
1. Taco ($2.50)
2. Burrito ($2.50)
3. Nachos ($3.00)
4. Soft Drink ($2.00)
5. Quit""")

print(menu)
print(" ")

totalPrice = 0.00
selection = 0

while selection != 5:
    selection = int(input("Enter a number: "))
    if selection == 1:
        print("You selected a Taco")
        totalPrice = totalPrice + 2.50
        print(" ")
        print(menu)
    if selection == 2:
        print("You selected a Burrito")
        totalPrice = totalPrice + 2.50
        print(" ")
        print(menu)
    if selection == 3:
        print("You selected Nachos")
        totalPrice = totalPrice + 3.00
        print(" ")
        print(menu)
    if selection == 4:
        print("You selected a Soft Drink")
        totalPrice = totalPrice + 2.00
        print(" ")
        print(menu)
    if selection > 5:
        print("That is not a valid selection. Please try again.")
    if selection < 1:
        print("That is not a valid selection. Please try again.")

if selection == 5:
    print(" ")
    print("Your total is $%.2f" % totalPrice)

