# python concession stand program
menu = {
    "samosa": 20,
    "vada pav": 30,
    "chole bhature": 80,
    "masala dosa": 50,
    "dal makhani": 200,
    "paneer tikka": 180,
    "gulab jamun": 15,
    "halwa": 40,
    "dhokla": 30 }

cart = []
total = 0

print("------MENU------")
for key, value in menu.items():
    print(f"{key.title():15} : ₹ {value:.2f}")
print("----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Item not on menu. Try again.")

print("------YOUR ORDER ------")
for item in cart:
    total += menu[item]
    print(item.title(), end=" ")

print()
print(f"Total is : ₹ {total:.2f}")
