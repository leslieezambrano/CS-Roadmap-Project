def display_intro():
print("Hello! Welcome to the Travel Expense Planner.")
print("This planner will help you track travel expenses and compare them to
your budget for your next travel visit!\n")
def get_budget():
while True:
budget = float(input("Please enter your budget: "))
if budget <= 0:
print("Error: Please enter a valid budget!")
else:
break
return budget
def get_category():
while True:
print("Please pick from the following categories:")
print("1. Transportation")
print("2. Accommodation")
print("3. Food")
print("4. Activities")
print("5. Miscellaneous")
choice = int(input("Your choice (1-5): "))
if choice >= 1 and choice <= 5:
break
else:
print("\nError: Please enter a valid category! (Accepts integer values
only)\n")
if choice == 1:
return "Transportation"
elif choice == 2:
return "Accommodation"
elif choice == 3:
return "Food"
elif choice == 4:
return "Activities"
return "Miscellaneous"
def get_expense_amount():
amount = 0
while True:
amount = float(input("Please enter your expense amount:"))
if amount <= 0:
print("\nError: Please enter a valid amount!\n")
else:
break
return amount
def add_expense():
categories = []
expenses = []
print("We will now collect your expenses categorized.\n")
restart = 'y'
while restart == 'y':
categories.append(get_category())
expenses.append(get_expense_amount())
restart = input("Would you like to add another expense? (y/n): ")
return categories, expenses
def calculate_total(amounts):
total = 0
for i in amounts:
total += i

