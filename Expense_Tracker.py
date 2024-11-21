import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store expenses
columns = ["Date", "Category", "Description", "Amount"]
expenses = pd.DataFrame(columns=columns)

def add_expense(date, category, description, amount):
    """
    Adds a new expense to the DataFrame.

    :param date: Date of the expense (YYYY-MM-DD format).
    :param category: Expense category (e.g., Food, Rent, Travel).
    :param description: Short description of the expense.
    :param amount: Amount spent.
    """
    global expenses
    new_expense = pd.DataFrame(
        [[date, category, description, amount]],
        columns=["Date", "Category", "Description", "Amount"]
    )
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    print("Expense added successfully!")

def view_expenses():
    """Displays all logged expenses."""
    if expenses.empty:
        print("No expenses logged yet.")
    else:
        print("\nLogged Expenses:")
        print(expenses.to_string(index=False))

def generate_report():
    """Generates a summary report of expenses by category and month."""
    if expenses.empty:
        print("No expenses to generate a report.")
        return

    # Convert Date column to datetime for easier analysis
    expenses["Date"] = pd.to_datetime(expenses["Date"])

    # Group by category and calculate total expenses
    category_report = expenses.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    # Group by month and calculate total expenses
    expenses["Month"] = expenses["Date"].dt.to_period("M")
    monthly_report = expenses.groupby("Month")["Amount"].sum()

    print("\nExpense Report by Category:")
    print(category_report.to_string())

    print("\nExpense Report by Month:")
    print(monthly_report.to_string())

if __name__ == "__main__":
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                date = input("Enter the date (YYYY-MM-DD): ").strip()
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                category = input("Enter the category (e.g., Food, Rent): ").strip()
                description = input("Enter a description of the expense: ").strip()
                amount = float(input("Enter the amount spent: ").strip())
                add_expense(date, category, description, amount)
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            generate_report()

        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
