import json
from datetime import datetime

# File to store the expense data
DATA_FILE = 'expenses.json'

# Function to load expenses from the JSON file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist yet

# Function to save expenses to the JSON file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

# Function to add a new expense
def add_expense(expenses):
    amount = float(input("Enter the amount in ₹: "))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date_input = input("Enter the date (YYYY-MM-DD) or press Enter to use today's date: ")
    
    if date_input:
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # Add the expense as a dictionary to the list
    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense of ₹{amount} under {category} on {date}.")

# Function to display total spending by category
def view_category_summary(expenses):
    category = input("Enter the category to view spending summary: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total spending on {category}: ₹{total:.2f}")

# Function to display total overall spending
def view_total_spending(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total overall spending: ₹{total:.2f}")

# Function to view spending over time (daily or monthly summaries)
def view_spending_over_time(expenses):
    summary_type = input("Enter summary type (daily/monthly): ").lower()
    if summary_type not in ['daily', 'monthly']:
        print("Invalid choice! Choose 'daily' or 'monthly'.")
        return
    
    spending_summary = {}
    
    for exp in expenses:
        if summary_type == 'daily':
            key = exp['date']  # Daily summary by date
        elif summary_type == 'monthly':
            key = exp['date'][:7]  # Monthly summary (YYYY-MM)
        
        if key not in spending_summary:
            spending_summary[key] = 0
        spending_summary[key] += exp['amount']
    
    print(f"Spending {summary_type} summary:")
    for date, total in spending_summary.items():
        print(f"{date}: ₹{total:.2f}")

# Main function to handle user interaction and the menu
def main():
    expenses = load_expenses()  # Load existing expenses (if any)

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View total spending by category")
        print("3. View total overall spending")
        print("4. View spending over time (daily/monthly)")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_category_summary(expenses)
        elif choice == '3':
            view_total_spending(expenses)
        elif choice == '4':
            view_spending_over_time(expenses)
        elif choice == '5':
            save_expenses(expenses)  # Save expenses before exiting
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
