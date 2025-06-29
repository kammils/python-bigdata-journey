# expense_tracker.py

expenses = []

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    expenses.append({"description": description, "amount": amount})
    print("✅ Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n📋 Expense List:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spent: ${total:.2f}\n")

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
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start the app
main()
