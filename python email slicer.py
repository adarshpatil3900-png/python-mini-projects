# python Email slicer program
email=input("Enter your email : ")

Index=email.index("@")

username=email[:Index]

domain=email[Index:]

print(f"Your username is {username} and domain is {domain}")