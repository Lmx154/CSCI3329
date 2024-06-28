import mysql.connector as mc


def main_menu():  # main menu function
    print("1. Login \n2. Signup \n3. Exit")


def customer_menu(user_id):  # customer menu function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    while True:
        print("1. Display Inventory \n2. Sort Inventory \n3. Add to cart \n4. View cart \n5. Empty cart \n6. Log out")
        choice = input("Please input your choice: ")

        if choice == '1':  # Display Inventory
            display_inventory(only_available=True, show_is_available=False)

        elif choice == '2':  # Sort Inventory
            sort_inventory()

        elif choice == '3':  # Add to cart
            display_inventory(only_available=True, show_is_available=False)
            vin = input("Enter VIN of the car to add to cart: ")
            cursor = db.cursor()
            cursor.execute("SELECT model FROM cars WHERE vin = %s", (vin,))
            car_model = cursor.fetchone()
            if car_model:
                cursor.execute("INSERT INTO customer_cart (customer_id, vin) VALUES (%s, %s)", (user_id, vin))
                cursor.execute("UPDATE cars SET is_available = 0 WHERE vin = %s", (vin,))
                db.commit()
                print(f"{car_model[0]} has been added to your cart!")
            else:
                print("Car with that VIN not found.")

        elif choice == '4':  # View cart
            cursor = db.cursor()  # Grab cursor
            cursor.execute("""
                SELECT c.vin, c.type, c.brand, c.model, c.year, c.mileage, c.price, c.color, c.feature
                FROM cars c
                JOIN customer_cart cc ON c.vin = cc.vin
                WHERE cc.customer_id = %s
            """, (user_id,))  # get car info from columns in car table. Join cart table with car table using vin & filter to include only rows with customer id in cart table
            rows = cursor.fetchall()

            # Display cart with labels
            print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")
            for row in rows:
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")

        elif choice == '5':  # Empty cart
            cursor = db.cursor()
            cursor.execute("SELECT vin FROM customer_cart WHERE customer_id = %s", (user_id,))
            rows = cursor.fetchall()
            for row in rows:
                cursor.execute("UPDATE cars SET is_available = 1 WHERE vin = %s", (row[0],))
            cursor.execute("DELETE FROM customer_cart WHERE customer_id = %s", (user_id,))
            db.commit()
            print("Cart emptied, your car/s are no longer reserved.")

        elif choice == '6':  # Log out
            break

    db.close()


def sort_inventory():  # sort inventory function
    while True:
        print("Sort Menu \n1. Sort by VIN \n2. Sort by Brand \n3. Sort by Model \n4. Sort by Year")
        print("5. Sort by Mileage \n6. Sort by Price \n7. Sort by Color \n8. Exit Sort Menu")
        sort_choice = input("Please input your choice: ")

        sort_column = None
        if sort_choice == '1':
            sort_column = 'vin'
        elif sort_choice == '2':
            sort_column = 'brand'
        elif sort_choice == '3':
            sort_column = 'model'
        elif sort_choice == '4':
            sort_column = 'year'
        elif sort_choice == '5':
            sort_column = 'mileage'
        elif sort_choice == '6':
            sort_column = 'price'
        elif sort_choice == '7':
            sort_column = 'color'
        elif sort_choice == '8':
            break
        else:
            print("Invalid choice, please try again.")
            continue

        if sort_column:
            display_sorted_inventory(sort_column)


def display_sorted_inventory(sort_column):  # display sorted inventory function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    cursor = db.cursor()
    query = f"SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars WHERE is_available = 1 ORDER BY {sort_column}"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Display sorted inventory with labels
    print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")

    db.close()


def display_inventory(only_available, show_is_available):  # display inventory function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    cursor = db.cursor()

    if only_available:
        cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars WHERE is_available = 1")
    else:
        if show_is_available:
            cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature, is_available FROM cars")
        else:
            cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars")
    rows = cursor.fetchall()

    # Display inventory with labels
    if show_is_available:
        print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10} {'Availability':<12}")
    else:
        print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")

    for row in rows:
        if show_is_available:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10} {row[9]:<12}")
        else:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")

    db.close()


def employee_menu():  # employee menu function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")

    while True:
        print("1. Display Inventory \n2. Add a Car \n3. Delete a Car \n4. Update a Car")
        print("5. Display Customers \n6. Display Employees \n7. Log out")
        choice = input("Please input your choice: ")

        if choice == '1':  # Display Inventory
            display_inventory(only_available=False, show_is_available=True)

        elif choice == '2':  # Add a Car
            display_inventory(only_available=False, show_is_available=True)
            vin = input("Enter VIN: ")
            car_type = input("Enter Type: ")
            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            year = input("Enter Year: ")
            mileage = input("Enter Mileage: ")
            price = input("Enter Price: ")
            color = input("Enter Color: ")
            feature = input("Enter Feature: ")
            is_available = input("Is Available (1 for Yes, 0 for No): ")

            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO cars (vin, type, brand, model, year, mileage, price, color, feature, is_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (vin, car_type, brand, model, year, mileage, price, color, feature, is_available))
            db.commit()
            print("Car added successfully.")

        elif choice == '3':  # Delete a Car
            display_inventory(only_available=False, show_is_available=True)
            vin = input("Enter VIN of the car to delete: ")
            cursor = db.cursor()
            cursor.execute("DELETE FROM cars WHERE vin = %s", (vin,))
            db.commit()
            print("Car deleted successfully.")

        elif choice == '4':  # Update a Car
            display_inventory(only_available=False, show_is_available=True)
            vin = input("Enter VIN of the car to update: ")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM cars WHERE vin = %s", (vin,))
            car = cursor.fetchone()
            if not car:
                print("Car not found.")
                continue

            while True:
                print("Update Menu \n1. Update Brand \n2. Update Model \n3. Update Year \n4. Update Mileage ")
                print("5. Update Price \n6. Update Color \n7. Update Feature \n8. Update Availability \n9. Exit Update Menu")
                update_choice = input("Please input your choice: ")

                if update_choice == '1':  # Update Brand
                    new_value = input(f"Enter new Brand (Current: {car[2]}): ")
                    cursor.execute("UPDATE cars SET brand = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Brand updated successfully.")
                elif update_choice == '2':  # Update Model
                    new_value = input(f"Enter new Model (Current: {car[3]}): ")
                    cursor.execute("UPDATE cars SET model = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Model updated successfully.")
                elif update_choice == '3':  # Update Year
                    new_value = input(f"Enter new Year (Current: {car[4]}): ")
                    cursor.execute("UPDATE cars SET year = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Year updated successfully.")
                elif update_choice == '4':  # Update Mileage
                    new_value = input(f"Enter new Mileage (Current: {car[5]}): ")
                    cursor.execute("UPDATE cars SET mileage = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Mileage updated successfully.")
                elif update_choice == '5':  # Update Price
                    new_value = input(f"Enter new Price (Current: {car[6]}): ")
                    cursor.execute("UPDATE cars SET price = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Price updated successfully.")
                elif update_choice == '6':  # Update Color
                    new_value = input(f"Enter new Color (Current: {car[7]}): ")
                    cursor.execute("UPDATE cars SET color = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Color updated successfully.")
                elif update_choice == '7':  # Update Feature
                    new_value = input(f"Enter new Feature (Current: {car[8]}): ")
                    cursor.execute("UPDATE cars SET feature = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Feature updated successfully.")
                elif update_choice == '8':  # Update Availability
                    new_value = input(f"Enter new availability (1 = available, 0 = unavailable) (Current: {car[9]}): ")
                    cursor.execute("UPDATE cars SET is_available = %s WHERE vin = %s", (new_value, vin))
                    db.commit()
                    print("Availability updated successfully.")
                elif update_choice == '9':  # Exit Update Menu
                    break
                else:
                    print("Invalid choice, please try again.")

                cursor.execute("SELECT * FROM cars WHERE vin = %s", (vin,))
                car = cursor.fetchone()

        elif choice == '5':  # Display Customers
            cursor = db.cursor()
            cursor.execute("""
                SELECT c.userid, c.fname, c.lname, c.email, GROUP_CONCAT(cc.vin SEPARATOR ', ') AS cart
                FROM carmax_customers c
                LEFT JOIN customer_cart cc ON c.userid = cc.customer_id
                GROUP BY c.userid, c.fname, c.lname, c.email
            """)  # Get customer details and their cart contents
            rows = cursor.fetchall()
            print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Cart':<10}")
            for row in rows:
                row = [r if r is not None else '' for r in row]  # Replace None with empty string
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")

        elif choice == '6':  # Display Employees
            cursor = db.cursor()
            cursor.execute("SELECT userid, fname, lname, email, position FROM carmax_employees")
            rows = cursor.fetchall()
            print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Position':<10}")
            for row in rows:
                row = [r if r is not None else '' for r in row]  # Replace None with empty string
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")

        elif choice == '7':  # Log out
            break

        else:
            print("Invalid choice, please try again.")

    db.close()


def login():  # login function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    while True:
        user_type = int(input("Login as: \n1. Employee \n2. Customer \nPlease input your choice: "))
        if user_type not in [1, 2]:
            print("Invalid choice. Please enter 2 for customer or 1 for employee.")
            continue

        username = input("Enter username: ")
        password = input("Enter password: ")

        cursor = db.cursor()
        if user_type == 2:
            cursor.execute("SELECT * FROM carmax_customers WHERE userid = %s AND passwd = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Welcome {user[2]}!")
                customer_menu(user[0])
                break
        elif user_type == 1:
            cursor.execute("SELECT * FROM carmax_employees WHERE userid = %s AND passwd = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Welcome {user[2]}!")
                employee_menu()
                break

        print("Invalid username or password. Please try again.")

    db.close()


def signup():  # signup function
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    while True:
        user_type = int(input("Sign up as: \n1. Employee \n2. Customer \nPlease input your choice: "))
        if user_type not in [1, 2]:
            print("Invalid choice. Please enter 2 for customer or 1 for employee.")
            continue

        if user_type == 2:  # Sign up as Customer
            userid = input("Enter username: ")
            password = input("Enter password: ")
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            email = input("Enter email: ")
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO carmax_customers (userid, passwd, fname, lname, email) VALUES (%s, %s, %s, %s, %s)",
                (userid, password, fname, lname, email))
        elif user_type == 1:  # Sign up as Employee
            manager_key = input("Enter manager key: ")
            if manager_key != '1234':
                print("Invalid manager key. Sign up failed.")
                continue
            userid = input("Enter username: ")
            password = input("Enter password: ")
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            email = input("Enter email: ")
            position = input("Enter position: ")
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO carmax_employees (userid, passwd, fname, lname, email, position) VALUES (%s, %s, %s, %s, %s, %s)",
                (userid, password, fname, lname, email, position))

        db.commit()
        print("Signup successful. You can now login.")
        break

    db.close()


# Main loop to display main menu and handle user choice
while True:
    main_menu()
    ch = input("Please input your choice: ")
    if ch == "3":
        break
    elif ch == "1":
        login()
    elif ch == "2":
        signup()
    else:
        print("Invalid choice, please try again.")
