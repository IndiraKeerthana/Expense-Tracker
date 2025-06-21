import csv
from datetime import datetime
from collections import defaultdict

FILENAME = 'expenses.csv'

# 📁 Create the CSV file if it's missing
def init_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])
    except FileExistsError:
        pass  # Already exists, no need to touch it

# ➕ Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    amount = input("Enter amount: ")
    note = input("Add a short note (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("✅ Expense recorded!")

# 📃 Display all recorded expenses with aligned table format
def view_expenses():
    print("\n📜 All Expenses:")
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    print(f"{row[0]:<12} | {row[1]:<10} | {row[2]:<8} | {row[3]}")
                    print("-" * 50)
                else:
                    print(f"{row[0]:<12} | {row[1]:<10} | ₹{float(row[2]):<7.2f} | {row[3]}")
    except FileNotFoundError:
        print("⚠️ No expenses file found yet.")

# 📊 Summarize spending by category and by month
def summarize_expenses():
    total = 0.0
    category_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            print("\n📋 Stored Expenses:")
            print(f"{headers[0]:<12} | {headers[1]:<10} | {headers[2]:<8} | {headers[3]}")
            print("-" * 50)

            for date_str, category, amount, note in reader:
                try:
                    amount = float(amount)
                    total += amount
                    category_totals[category] += amount

                    month = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m')
                    monthly_totals[month] += amount

                    print(f"{date_str:<12} | {category:<10} | ₹{amount:<7.2f} | {note}")
                except ValueError:
                    print(f"⚠️ Skipping malformed entry: {date_str}, {category}, {amount}, {note}")

        print(f"\n💰 Total Spent: ₹{total:.2f}")

        print("\n📂 Spending by Category:")
        for category, amt in category_totals.items():
            print(f"  - {category}: ₹{amt:.2f}")

        print("\n🗓️ Spending by Month:")
        for month, amt in sorted(monthly_totals.items()):
            print(f"  - {month}: ₹{amt:.2f}")

    except FileNotFoundError:
        print("⚠️ No expenses file found yet.")

# 🎮 Main user interface loop
def main():
    init_file()
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1️⃣  Add Expense")
        print("2️⃣  View Expenses")
        print("3️⃣  Summarize Expenses")
        print("4️⃣  Exit")
        choice = input("Pick an option (1–4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses()
        elif choice == '4':
            print("👋 Thanks for using the expense tracker. Happy saving!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
