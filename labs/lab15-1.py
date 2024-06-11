def display_main_menu():
    print("Main Menu")
    print("1. Utility")
    print("2. Game")
    print("3. Multimedia")
    print("4. Exit")


def display_utility_menu():
    print("Utility Menu")
    print("1. Calculator")
    print("2. Email")
    print("3. Note")
    print("4. Main menu")


def display_game_menu():
    print("Game Menu")
    print("1. Poker")
    print("2. Blackjack")
    print("3. Main menu")


def display_multimedia_menu():
    print("Multimedia Menu")
    print("1. Music player")
    print("2. Camera")
    print("3. Download Youtube")
    print("4. Main menu")


while True:
    display_main_menu()
    user = input("Please input: ")

    if user == '4':
        print("Thank you! Bye!")
        break
    elif user == '1':
        while True:
            display_utility_menu()
            user = input("Please input: ")
            if user == '4':
                break
            else:
                print("I am sorry. It's not ready yet.")
    elif user == '2':
        while True:
            display_game_menu()
            user = input("Please input: ")
            if user == '3':
                break
            else:
                print("I am sorry. It's not ready yet.")
    elif user == '3':
        while True:
            display_multimedia_menu()
            user = input("Please input: ")
            if user == '4':
                break
            else:
                print("I am sorry. It's not ready yet.")
    else:
        print("I am sorry. Please input correctly.")
