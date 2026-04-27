import random

def main():
    while True:
        print('\nChoose a number between 1 and 6 (or type "exit" to quit):')
        user_input = input()
        if user_input == "exit":
            break
        try:
            user_choice = int(user_input)
            if 1 <= user_choice <= 6:
                computer_choice = random.randint(1, 6)
                print(f"Computer rolled: {computer_choice}")
                if user_choice == computer_choice:
                    print("You guessed it right!")
                else:
                    print("Wrong guess. Try again!")
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")