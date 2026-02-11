# python expense tracker program
class Expense:
    def __init__(self,amount,category,date):
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker :
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)

    def show_expenses(self):
        for expense in self.expenses:
            print(f"{expense.amount} | {expense.category} | {expense.date}")
            print("-------------------")

    def total_spent(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"total spent : {total}")

tracker = ExpenseTracker()
while True:
    print("1. add expense : ")
    print("2. show expenses : ")
    print("3. total spent : ")
    print("4. exit : ")

    choice = input("choose option : ")

    if choice == '1':
     amount = float(input("enter your amount : "))
     category = input("enter category : ")
     date = input("enter date :")

     expense_obj = Expense(amount,category,date)
     tracker.add_expense(expense_obj)

    elif choice == "2":
     tracker.show_expenses()

    elif choice == "3":
     tracker.total_spent()

    elif choice == "4":
     break
    