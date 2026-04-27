from models.account import Account

account = Account()

def display_balance():
    print(f"\nYour balance is {account.balance}")

def withdraw(amount):
    if amount > account.balance:
        print("\nInsufficient balance")
        return
    print("\nYou have withdrawn",amount)
    account.balance -= amount
    account.statement.append(("withdrawn", amount))

    print(f"Current balance is {account.balance}")

def deposit(amount):
    print("\nYou have deposited",amount) 
    account.balance += amount
    account.statement.append(("deposited", amount))
    print(f"Current balance is {account.balance}")