"""
Project: Task List Manager

What it needs: File I/O, lists, dictionaries, string methods

What it is: A tool that adds, removes, and lists tasks, saving them to a file.

"""

task = {}



while(True):
    print("""
        ------------------------------
        ------------------------------\n
        Welcome to Task List Manager\n
        ------------------------------
        ------------------------------""")

    option = input("""

        1. Add a task/s \n
        2. View task/s\n
        3. Complete a Task
        4. Show remaining task/s \n
        4. Exit\n

        Enter Option (e.g. 1 for Add a task.): """)

    print("\n\t------------------------------\n")
    match option :
        case "1":
            print("\tAdd a task Selected:")
            # add_expense()
        case "2":
            print("\tView tasks Selected:")
            # view_expenses()
        case "3":
            print("\tComplete a task Selected:")
        case "4":
            print("\tShow remaining task Selected:")
            # total_spending()
        case "5":
            print("\tThanks for using.")
            break
        case _:
            print ("\tError: Invalid Input")
