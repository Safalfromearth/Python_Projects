from games.rock_paper_scissors import main as rps_main
from games.dice_roll import main as dice_main

while True:
    print("\n\n1. Play Rock, Paper, Scissors\n2. Play Dice Roll\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        rps_main()
    elif choice == 2:
        dice_main()
    elif choice == 3:
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please try again.")