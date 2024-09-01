import random

choices = ('scissors', 'rock', 'paper')

def determine_winner(computer, player):
    if computer == player:
        return "It's a tie"
    elif (player == "scissors" and computer == "paper") or (player == "rock" and computer =="scissors") or (player == "paper"  and computer =="rock"):
        return "You won"
    return "You lost"

while True:
    player_choice = input("Please chose rock, paper or scissors or quit to end the game: ").lower()
    if player_choice == "quit":
        break
    if player_choice not in choices:
        print("Invalid entry, please try again")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")

    result = determine_winner(computer_choice, player_choice)
    print(result)