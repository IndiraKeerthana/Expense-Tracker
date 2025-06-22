# A list to store all the expenses
expenses = []

# Add a new expense
def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (e.g., Food, Travel): ")
    amount = input("Amount: ")
    note = input("Note (optional): ")

    expense = {
        "date": date,
        "category": category,
        "amount": float(amount),
        "note": note
    }
    expenses.append(expense)
    print("✅ Expense added!")

# Show all expenses
def view_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        print("\n🧾 All Expenses:")
        for exp in expenses:
            print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']:.2f} | {exp['note']}")

# Show totals by category and month
def summarize_expenses():
    if not expenses:
        print("No data to summarize.")
        return

    total = 0
    categories = {}
    months = {}

    for exp in expenses:
        amount = exp['amount']
        category = exp['category']
        date = exp['date']

        total += amount
        categories[category] = categories.get(category, 0) + amount
        month = date[:7]  # Gets 'YYYY-MM'
        months[month] = months.get(month, 0) + amount

    print(f"\n💰 Total Spent: ₹{total:.2f}")
    print("\n📂 By Category:")
    for cat, amt in categories.items():
        print(f"  {cat}: ₹{amt:.2f}")
    print("\n🗓️ By Month:")
    for m, amt in months.items():
        print(f"  {m}: ₹{amt:.2f}")

# Main menu loop
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All")
        print("3. Show Totals")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses()
        elif choice == '4':
            print("👋 Bye! (your data will be lost when this closes)")
            break
        else:
            print("❌ Invalid option. Try again!")

if __name__ == "__main__":
    main()
