from services.atmOperations import account

def show_statement():
    print("\nTransaction Statement:")
    for transaction in account.statement:
        print(f"{transaction[0]}: {transaction[1]}")