# tip calculator
bill = float(input("Enter the bill amount : ₹  "))
tip_percent = input("Enter the tip percentage(default 10% ) : ").strip()

if tip_percent == "":
    tip_percent = 10
else:
    tip_percent = float(tip_percent)

people = input("Enter the number of people (default 1 ) : ").strip()
if people == "":
    people = 1
else:
    people = int(people)

tip_amount = (tip_percent/100)*bill
total = bill + tip_amount
per_person = total / people

print("-------------- YOUR BILL --------------")
print(f"bill amount = ₹{bill:.2f}")
print(f"Tip {tip_percent} % : ₹{tip_amount:.2f}")
print(f"Total amount : ₹{total:.2f}")
if people > 1:
    print(f"Amount per person : ₹{per_person:.2f}")
    
print("---------THANK YOU FOR SHOPPING --------")