"""
Project: CLI Expense Tracker
what it needs: File I/O (JSON), try/except, loops, functions
what it does: A tool that adds expenses, saves them to a JSON file, and shows the total.
"""


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

        Enter Option (e.g. 1 for Add an expense.)""")

    print("\n\t------------------------------\n")
    match option :
        case "1":
            print("\tAdd an Expense Selected:")
        case "2":
            print("\tView Expenses Selected:")
        case "3":
            print("\tShow total spending Selected:")
        case "4":
            print("\tThanks for using.")
            break
        case _:
            print ("\tError: Invalid Input")
