import os


def display_main_menu():
    print("Main Menu")
    print("1. Utility")
    print("2. Game")
    print("3. Multimedia")
    print("4. Log out")


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


def display_login_menu():
    print("Login/Signup Menu")
    print("1. Log in")
    print("2. Sign up")
    print("3. Exit")


def signup():
    username = input("Please input an ID: ")
    password = input("Please input a password: ")

    id_file = open("id.txt", "a")
    id_file.write(username + "\n")
    id_file.close()

    pass_file = open("pass.txt", "a")
    pass_file.write(password + "\n")
    pass_file.close()

    print("Signup successful! Please log in to continue.")


def login():
    username = input("Please input your ID: ")
    password = input("Please input your password: ")

    ids = []
    id_file = open("id.txt", "r")
    for line in id_file:
        ids.append(line.strip())
    id_file.close()

    passwords = []
    pass_file = open("pass.txt", "r")
    for line in pass_file:
        passwords.append(line.strip())
    pass_file.close()

    if username in ids and passwords[ids.index(username)] == password:
        print("Welcome back, {}!".format(username))
        return True
    else:
        print("ID or Password is incorrect!")
        return False


# Start of the script execution
while True:
    display_login_menu()
    choice = input("Please input: ")

    if choice == '3':
        print("Thank you! Bye~")
        break
    elif choice == '2':
        signup()
    elif choice == '1':
        if login():
            while True:
                display_main_menu()
                user = input("Please input: ")

                if user == '4':
                    print("You are logged out!")
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
        else:
            continue
