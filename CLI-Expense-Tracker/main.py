"""
Project: CLI Expense Tracker
what it needs: File I/O (JSON), try/except, loops, functions
what it does: A tool that adds expenses, saves them to a JSON file, and shows the total.
"""

expenses = {}
def add_expense():
    print("\t------------------------------")
    expense_name = input("\tEnter the name of expense: ")

    try:
        amount = int(input("\tEnter the amount: "))
        expenses[expense_name] = amount
        print(f"\t{expense_name} added Successfully.")
    except ValueError:
        print("\n\tError!! : Input is not a Number. ")

def view_expenses():
    print(f"\n\t {expenses}")


def total_spending():
    total = 0

    for i in expenses.values():
        total += i

    print(f"\n\t {total} is Total Spending till now.")


while(True):
    print("""
        ------------------------------
        ------------------------------\n
        Welcome to CLI Expense Tracker\n
        ------------------------------
        ------------------------------""")

    option = input("""

        1. Add an expense\n
        2. View expenses\n
        3. Show total spending\n
        4. Exit\n

        Enter Option (e.g. 1 for Add an expense.): """)

    print("\n\t------------------------------\n")
    match option :
        case "1":
            print("\tAdd an Expense Selected:")
            add_expense()
        case "2":
            print("\tView Expenses Selected:")
            view_expenses()
        case "3":
            print("\tShow total spending Selected:")
            total_spending()
        case "4":
            print("\tThanks for using.")
            break
        case _:
            print ("\tError: Invalid Input")
