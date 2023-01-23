import random
while True:
    user = input('Choose from {rock, paper, scissors}')
    pc = random.choice(['rock', 'paper', 'scissors'])
    print(f"\nYou chose {user}, computer chose {pc}.\n")

    if user == pc:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if pc == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if pc == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if pc == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
