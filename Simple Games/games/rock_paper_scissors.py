import random

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def main():
    user_score, computer_score = 0, 0
    while True:
        user_input = input("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ")
        if user_input == 'quit':
            break
        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")

        if user_input == comp_choice:
            print("It's a tie!")
        elif (user_input == "rock" and comp_choice == "scissors") or \
            (user_input == "paper" and comp_choice == "rock") or \
            (user_input == "scissors" and comp_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nCurrent Scores - You: {user_score}, Computer: {computer_score}\n")