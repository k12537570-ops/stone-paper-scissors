import random

def stone_paper_scissors():
    choices = ['stone', 'paper', 'scissors']

    print("\n--- Stone Paper Scissors ---")
    print("Choose: stone, paper, or scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice!")
        return

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win")
    else:
        print("You lose")

stone_paper_scissors()
