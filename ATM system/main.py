from services.atmOperations import deposit, withdraw, display_balance
from services.statement import show_statement

while True:
    print("\n\n1. Display Balance\n2. Withdraw Money\n3. Deposit Money\n4. Print Bank Statement\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_balance()
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
    elif choice == 3:
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
    elif choice == 4:
        show_statement()
    elif choice == 5:
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")