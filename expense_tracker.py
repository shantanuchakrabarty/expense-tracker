import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, Bills, etc.): ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n=== All Expenses ===")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']} | ₹{expense['amount']} | {expense['description']}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    
    try:
        choice = int(input("\nEnter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Deleted: {removed['description']} (₹{removed['amount']})")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "4":
            pass  # We'll add this in the next phase
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()