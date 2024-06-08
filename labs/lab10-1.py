import random

keep_playing = 'y'
while keep_playing == 'y':
    print("Start Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    throw = int(input("What do you want to throw? "))
    npc = random.randint(1, 3)

    player_choice = ""
    computer_choice = ""

    if throw == 1:
        player_choice = "Rock"
    elif throw == 2:
        player_choice = "Paper"
    elif throw == 3:
        player_choice = "Scissors"

    if npc == 1:
        computer_choice = "Rock"
    elif npc == 2:
        computer_choice = "Paper"
    elif npc == 3:
        computer_choice = "Scissors"

    print("Computer:", computer_choice, " vs You:", player_choice)

    if throw == npc:
        print("It's a tie!")
    elif (throw == 1 and npc == 3) or (throw == 2 and npc == 1) or (throw == 3 and npc == 2):
        print("You win!!!")
    else:
        print("You lose.")

    keep_playing = input("Do you want to play again? (y/n): ").lower()

print("Thanks you!!!")
