import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Initialize an empty DataFrame to store expenses
columns = ["Date", "Category", "Description", "Amount"]
expenses = pd.DataFrame(columns=columns)

def add_expense(date, category, description, amount):
    """Adds a new expense to the DataFrame."""
    global expenses
    new_expense = pd.DataFrame(
        [[date, category, description, amount]],
        columns=["Date", "Category", "Description", "Amount"]
    )
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    messagebox.showinfo("Success", "Expense added successfully!")

def view_expenses():
    """Displays all logged expenses."""
    if expenses.empty:
        messagebox.showwarning("No Expenses", "No expenses logged yet.")
    else:
        expenses_window = tk.Toplevel(root)
        expenses_window.title("Logged Expenses")
        expenses_window.geometry("600x400")

        text_widget = tk.Text(expenses_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        text_widget.insert(tk.END, expenses.to_string(index=False))

def generate_report():
    """Generates a summary report of expenses by category and month."""
    if expenses.empty:
        messagebox.showwarning("No Expenses", "No expenses to generate a report.")
        return

    # Convert Date column to datetime for easier analysis
    expenses["Date"] = pd.to_datetime(expenses["Date"])

    # Group by category and calculate total expenses
    category_report = expenses.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    # Group by month and calculate total expenses
    expenses["Month"] = expenses["Date"].dt.to_period("M")
    monthly_report = expenses.groupby("Month")["Amount"].sum()

    report_window = tk.Toplevel(root)
    report_window.title("Expense Report")
    report_window.geometry("600x400")

    text_widget = tk.Text(report_window, wrap=tk.WORD)
    text_widget.pack(expand=True, fill=tk.BOTH)

    text_widget.insert(tk.END, "Expense Report by Category:\n")
    text_widget.insert(tk.END, category_report.to_string())
    text_widget.insert(tk.END, "\n\nExpense Report by Month:\n")
    text_widget.insert(tk.END, monthly_report.to_string())

def add_expense_gui():
    #nHandles the Add Expense button click event."""
    try:
        date = date_entry.get()
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        category = category_entry.get()
        description = description_entry.get()
        amount = float(amount_entry.get())
        add_expense(date, category, description, amount)
        clear_entries()
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Invalid input: {e}. Please try again.")

def clear_entries():
    #Clears all entry fields
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 24, "bold"), bg="#3b7bbf", fg="white", pady=20)
title_label.pack(fill="both")

# Date input
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="#f0f0f0")
date_label.pack(pady=5)
date_entry = tk.Entry(root, font=("Arial", 12))
date_entry.pack(pady=5)

# Category input
category_label = tk.Label(root, text="Category (e.g., Food, Rent):", font=("Arial", 12), bg="#f0f0f0")
category_label.pack(pady=5)
category_entry = tk.Entry(root, font=("Arial", 12))
category_entry.pack(pady=5)

# Description input
description_label = tk.Label(root, text="Description of Expense:", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=5)
description_entry = tk.Entry(root, font=("Arial", 12))
description_entry.pack(pady=5)

# Amount input
amount_label = tk.Label(root, text="Amount Spent:", font=("Arial", 12), bg="#f0f0f0")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=5)

# Add Expense Button
add_button = tk.Button(root, text="Add Expense", font=("Arial", 14), bg="#4CAF50", fg="white", command=add_expense_gui)
add_button.pack(pady=20)

# View Expenses Button
view_button = tk.Button(root, text="View Expenses", font=("Arial", 14), bg="#2196F3", fg="white", command=view_expenses)
view_button.pack(pady=10)

# Generate Report Button
report_button = tk.Button(root, text="Generate Report", font=("Arial", 14), bg="#FF9800", fg="white", command=generate_report)
report_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
