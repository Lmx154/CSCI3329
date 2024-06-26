import mysql.connector as mc


def main_menu():
    print("1. Login")
    print("2. Signup")
    print("3. Exit")


def customer_menu():
    print("1. Display Inventory")
    print("2. Sort Inventory")
    print("3. Add to cart")
    print("4. View cart")
    print("5. Empty cart")
    print("6. Log out")


def display_inventory():
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cars WHERE is_available = 1")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()


def employee_menu():
    db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")

    while True:
        print("1. Display Inventory")
        print("2. Add a Car")
        print("3. Delete a Car")
        print("4. Update a Car")
        print("5. Display Customers")
        print("6. Display Employees")
        print("7. Log out")
        choice = input("Please input your choice: ")

        if choice == '1':
            display_inventory()

        elif choice == '2':
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
            cursor.execute("INSERT INTO cars (vin, type, brand, model, year, mileage, price, color, feature, is_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (vin, car_type, brand, model, year, mileage, price, color, feature, is_available))
            db.commit()
            print("Car added successfully.")

        elif choice == '3':
            vin = input("Enter VIN of the car to delete: ")
            cursor = db.cursor()
            cursor.execute("DELETE FROM cars WHERE vin = %s", (vin,))
            db.commit()
            print("Car deleted successfully.")

        elif choice == '4':
            vin = input("Enter VIN of the car to update: ")

            # Fetch current values
            cursor = db.cursor()
            cursor.execute("SELECT * FROM cars WHERE vin = %s", (vin,))
            car = cursor.fetchone()
            if not car:
                print("Car not found.")
                continue

            # Update fields
            car_type = input(f"Enter Type ({car[1]}): ") or car[1]
            brand = input(f"Enter Brand ({car[2]}): ") or car[2]
            model = input(f"Enter Model ({car[3]}): ") or car[3]
            year = input(f"Enter Year ({car[4]}): ") or car[4]
            mileage = input(f"Enter Mileage ({car[5]}): ") or car[5]
            price = input(f"Enter Price ({car[6]}): ") or car[6]
            color = input(f"Enter Color ({car[7]}): ") or car[7]
            feature = input(f"Enter Feature ({car[8]}): ") or car[8]
            is_available = input(f"Is Available ({car[9]}) (1 for Yes, 0 for No): ") or car[9]

            cursor.execute("UPDATE cars SET type=%s, brand=%s, model=%s, year=%s, mileage=%s, price=%s, color=%s, feature=%s, is_available=%s WHERE vin=%s",
                           (car_type, brand, model, year, mileage, price, color, feature, is_available, vin))
            db.commit()
            print("Car updated successfully.")

        elif choice == '5':
            cursor = db.cursor()
            cursor.execute("SELECT * FROM customers")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif choice == '6':
            cursor = db.cursor()
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif choice == '7':
            break

        else:
            print("Invalid choice, please try again.")

    db.close()


while True:
    main_menu()
    ch = input("Please input your choice: ")
    if ch == "3":
        break
    elif ch == "1":
        # This is a simplified login check for demonstration purposes
        user_type = 'e'  # Assume the user is an employee for demonstration
        if user_type == 'c':
            while True:
                customer_menu()
                ch = input("Please input your choice: ")
                if ch == '6':
                    break
                elif ch == '1':
                    display_inventory()
        elif user_type == 'e':
            employee_menu()
