# python weight converter
Weight = float(input("Enter your weight : "))
unit  = input("Kilograms or pounds? (K or L): ")

if unit == "K":
    Weight = Weight * 2.205
    unit = "Lbs."
    print(f"Your weight is : {round(Weight,1)} {unit}")

elif unit == "L":
    Weight = Weight / 2.205
    unit = "Kgs."
    print(f"Your weight is : {round(Weight,1)} {unit}")

else:
    print(f"{unit} was not valid ")