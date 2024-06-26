import mysql.connector as mc


def main_menu():
    print("1. login")
    print("2. signup")
    print("3. exit")


def customer_menu():
    print("Display Inventory")
    print("Sort Inventory")
    print("Add to cart")
    print("View cart")
    print("Empty cart")
    print("Log out")


def display_inventory():
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    print("show the database")
    # create an extra column that will show reserved
    # don't show reserved cars in inventory.


while True:
    main_menu()
    ch = input("Please input your choice: ")
    if ch == "3":
        break
    elif ch == "1":
        if True:
            user_type = 'c'
            if user_type == 'c':
                while True:
                    customer_menu()
                    ch = input("Please input your choice: ")
                    if ch == '6':
                        break
                    elif ch == '1':
                        display_inventory()