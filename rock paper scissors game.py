import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    if player == computer:
        print("Computer: "+ computer)
        print("Player: "+ player)
        print("Tie!!!")
    elif player == "rock":
        if computer == "scissors":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You Win!! ")
        elif computer == "paper":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You lose!!")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You Win!! ")
        elif computer == "rock":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You lose!!")
    elif player == "paper":
        if computer == "rock":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You Win!! ")
        elif computer == "scissors":
            print("Computer: "+ computer)
            print("Player: "+ player)
            print("You lose!!")
    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!! Thank you for playing with me.")
