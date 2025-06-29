# Add a new expense: description, amount
# View all expenses
# Calculate total spent
# Exit the app

myExpense = {}
def add_Expenses():
    expenseName = input("Enter the ExpenseName: ")
    expenseAmount = float(input("Enter the Amount: "))
    myExpense.update({expenseName : expenseAmount})
    print("Expense Added Successfully")

def view_Expenses():
    if not myExpense:
        print("No Expenses are tracked")
    else:
        print("List of Expenses")
        print("----------------")
        for i in myExpense:
            print(f"{i} : ${myExpense[i]:.2f} ")

def totalExpenses():
    if not myExpense:
        print("Track Expenses to display")
    else:
        total = sum(myExpense[i] for i in myExpense)
        print(f"Total Expenses: ${total:.2f}")
            
def main():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            add_Expenses()
        elif choice == "2":
            view_Expenses()
        elif choice == "3":
            totalExpenses()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start the app
main()
