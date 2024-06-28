import mysql.connector as mc


# Database class to manage the database connection and operations
class Database:
    def __init__(self):
        self.db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")

    def get_cursor(self):
        return self.db.cursor()

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()


# User class as a base class for Customer and Employee
class User:
    def __init__(self, user_id, fname, lname, email):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname
        self.email = email

    # Method to display inventory
    def display_inventory(self, db, only_available, show_is_available):
        cursor = db.get_cursor()

        # SQL query to fetch inventory based on availability and sorted by sort_order
        if only_available:
            cursor.execute( "SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars WHERE is_available = 1 ORDER BY sort_order")
        else:
            if show_is_available:
                cursor.execute( "SELECT vin, type, brand, model, year, mileage, price, color, feature, is_available FROM cars ORDER BY sort_order")
            else:
                cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars ORDER BY sort_order")
        rows = cursor.fetchall()

        # Display inventory
        if show_is_available:
            print(
                f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10} {'Availability':<12}")
        else:
            print(
                f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")

        for row in rows:
            if show_is_available:
                print(
                    f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10} {row[9]:<12}")
            else:
                print(
                    f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")

    # Method to sort inventory
    def sort_inventory(self, db, sort_column):
        cursor = db.get_cursor()
        # SQL query to fetch sorted inventory and update sort_order
        query = f"SELECT vin FROM cars WHERE is_available = 1 ORDER BY {sort_column}"
        cursor.execute(query)
        rows = cursor.fetchall()
        # Update the sort_order in the database
        for index, row in enumerate(rows):
            cursor.execute("UPDATE cars SET sort_order = %s WHERE vin = %s", (index, row[0]))
        db.commit()
        self.display_inventory(db, only_available=True, show_is_available=False)

    # Declared static since class info is not required
    @staticmethod
    def _print_inventory(rows):
        print(
            f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")
        for row in rows:
            print(
                f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")


# Customer class inheriting from User
class Customer(User):
    def __init__(self, user_id, fname, lname, email):
        super().__init__(user_id, fname, lname, email)

    # Customer menu
    def menu(self, db):
        while True:
            print("1. Display Inventory \n2. Sort Inventory \n3. Add to cart")
            print("4. View cart \n5. Empty cart \n6. Log out")
            choice = input("Please input your choice: ")

            if choice == '1':
                self.display_inventory(db, only_available=True, show_is_available=False)

            elif choice == '2':
                self.sort_inventory_menu(db)

            elif choice == '3':
                self.add_to_cart(db)

            elif choice == '4':
                self.view_cart(db)

            elif choice == '5':
                self.empty_cart(db)

            elif choice == '6':
                print("Bye~!")
                break

    # Method to add a car to the cart
    def add_to_cart(self, db):
        self.display_inventory(db, only_available=True, show_is_available=False)
        vin = input("Enter VIN of the car to add to cart: ")
        cursor = db.get_cursor()

        # SQL query to fetch the car model
        cursor.execute("SELECT model FROM cars WHERE vin = %s", (vin,))
        car_model = cursor.fetchone()
        if car_model:
            # SQL queries to add car to cart and update availability
            cursor.execute("INSERT INTO customer_cart (customer_id, vin) VALUES (%s, %s)", (self.user_id, vin))
            cursor.execute("UPDATE cars SET is_available = 0 WHERE vin = %s", (vin,))
            db.commit()
            print(f"{car_model[0]} has been added to your cart!")
        else:
            print("Car with that VIN not found.")

    # Method to view the cart
    def view_cart(self, db):
        cursor = db.get_cursor()
        # SQL query to fetch the cart details
        cursor.execute(""" SELECT c.vin, c.type, c.brand, c.model, c.year, c.mileage, c.price, c.color, c.feature FROM cars c JOIN customer_cart cc ON c.vin = cc.vin WHERE cc.customer_id = %s """, (self.user_id,))
        rows = cursor.fetchall()
        self._print_inventory(rows)

    # Method to empty the cart
    def empty_cart(self, db):
        cursor = db.get_cursor()
        # SQL query to fetch VINs of cars in the cart
        cursor.execute("SELECT vin FROM customer_cart WHERE customer_id = %s", (self.user_id,))
        rows = cursor.fetchall()
        for row in rows:
            # SQL query to update availability
            cursor.execute("UPDATE cars SET is_available = 1 WHERE vin = %s", (row[0],))
        # SQL query to delete cart entries
        cursor.execute("DELETE FROM customer_cart WHERE customer_id = %s", (self.user_id,))
        db.commit()
        print("Cart emptied, your car/s are no longer reserved.")

    # Menu to sort inventory
    def sort_inventory_menu(self, db):
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
                print("Going back to customer menu.")
                break
            else:
                print("Invalid choice, please try again.")
                continue
            if sort_column:
                self.sort_inventory(db, sort_column)


# Employee class inheriting from User
class Employee(User):
    def __init__(self, user_id, fname, lname, email, position):
        super().__init__(user_id, fname, lname, email)
        self.position = position

    # Employee menu
    def menu(self, db):
        while True:
            print("1. Display Inventory \n2. Add a Car \n3. Delete a Car \n4. Update a Car")
            print("5. Display Customers \n6. Display Employees \n7. Log out")
            choice = input("Please input your choice: ")
            if choice == '1':
                self.display_inventory(db, only_available=False, show_is_available=True)
            elif choice == '2':
                self.add_car(db)
            elif choice == '3':
                self.delete_car(db)
            elif choice == '4':
                self.update_car(db)
            elif choice == '5':
                self.display_customers(db)
            elif choice == '6':
                self.display_employees(db)
            elif choice == '7':
                print("Bye~!")
                break

    # Method to add a car to the inventory
    def add_car(self, db):
        self.display_inventory(db, only_available=False, show_is_available=True)
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
        cursor = db.get_cursor()
        # SQL query to insert a new car into the inventory
        cursor.execute( "INSERT INTO cars (vin, type, brand, model, year, mileage, price, color, feature, is_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",  (vin, car_type, brand, model, year, mileage, price, color, feature, is_available))
        db.commit()
        print("Car added successfully.")

    # Method to delete a car from the inventory
    def delete_car(self, db):
        self.display_inventory(db, only_available=False, show_is_available=True)
        vin = input("Enter VIN of the car to delete: ")
        cursor = db.get_cursor()
        # SQL query to delete a car from the inventory
        cursor.execute("DELETE FROM cars WHERE vin = %s", (vin,))
        db.commit()
        print("Car deleted successfully.")

    # Method to update a car's details in the inventory
    def update_car(self, db):
        self.display_inventory(db, only_available=False, show_is_available=True)
        vin = input("Enter VIN of the car to update: ")
        cursor = db.get_cursor()
        # SQL query to fetch details of a car
        cursor.execute("SELECT * FROM cars WHERE vin = %s", (vin,))
        car = cursor.fetchone()
        if not car:
            print("Car not found.")
            return
        while True:
            print("Update Menu \n1. Update Brand \n2. Update Model \n3. Update Year \n4. Update Mileage ")
            print("5. Update Price \n6. Update Color \n7. Update Feature \n8. Update Availability \n9. Exit Update Menu")
            update_choice = input("Please input your choice: ")

            # SQL queries to update the car details based on the chosen option
            if update_choice == '1':
                new_value = input(f"Enter new Brand (Current: {car[2]}): ")
                cursor.execute("UPDATE cars SET brand = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Brand updated successfully.")
            elif update_choice == '2':
                new_value = input(f"Enter new Model (Current: {car[3]}): ")
                cursor.execute("UPDATE cars SET model = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Model updated successfully.")
            elif update_choice == '3':
                new_value = input(f"Enter new Year (Current: {car[4]}): ")
                cursor.execute("UPDATE cars SET year = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Year updated successfully.")
            elif update_choice == '4':
                new_value = input(f"Enter new Mileage (Current: {car[5]}): ")
                cursor.execute("UPDATE cars SET mileage = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Mileage updated successfully.")
            elif update_choice == '5':
                new_value = input(f"Enter new Price (Current: {car[6]}): ")
                cursor.execute("UPDATE cars SET price = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Price updated successfully.")
            elif update_choice == '6':
                new_value = input(f"Enter new Color (Current: {car[7]}): ")
                cursor.execute("UPDATE cars SET color = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Color updated successfully.")
            elif update_choice == '7':
                new_value = input(f"Enter new Feature (Current: {car[8]}): ")
                cursor.execute("UPDATE cars SET feature = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Feature updated successfully.")
            elif update_choice == '8':
                new_value = input(f"Enter new availability (1 = available, 0 = unavailable) (Current: {car[9]}): ")
                cursor.execute("UPDATE cars SET is_available = %s WHERE vin = %s", (new_value, vin))
                db.commit()
                print("Availability updated successfully.")
            elif update_choice == '9':
                print("Going back to employee menu.")
                break
            else:
                print("Invalid choice, please try again.")
            cursor.execute("SELECT * FROM cars WHERE vin = %s", (vin,))
            car = cursor.fetchone()

    # Method to display customers and their carts
    def display_customers(self, db):
        cursor = db.get_cursor()
        # SQL query to fetch customer details and their carts
        cursor.execute(""" SELECT c.userid, c.fname, c.lname, c.email, GROUP_CONCAT(cc.vin SEPARATOR ', ') AS cart FROM carmax_customers c LEFT JOIN customer_cart cc ON c.userid = cc.customer_id GROUP BY c.userid, c.fname, c.lname, c.email """)
        rows = cursor.fetchall()
        print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Cart':<10}")
        for row in rows:
            row = [r if r is not None else '' for r in row]
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")

    # Method to display employees
    def display_employees(self, db):
        cursor = db.get_cursor()

        # SQL query to fetch employee details
        cursor.execute("SELECT userid, fname, lname, email, position FROM carmax_employees")
        rows = cursor.fetchall()
        print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Position':<10}")
        for row in rows:
            row = [r if r is not None else '' for r in row]
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")


# Login Function
def login():
    db = Database()
    while True:
        user_type = int(input("Login as: \n1. Employee \n2. Customer \nPlease input your choice: "))
        if user_type not in [1, 2]:
            print("Invalid choice. Please enter 2 for customer or 1 for employee.")
            continue
        username = input("Enter username: ")
        password = input("Enter password: ")
        cursor = db.get_cursor()
        if user_type == 2:
            # SQL query to verify customer credentials
            cursor.execute("SELECT * FROM carmax_customers WHERE userid = %s AND passwd = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Welcome {user[2]}!")
                customer = Customer(user[0], user[2], user[3], user[4])
                customer.menu(db)
                break
        elif user_type == 1:
            # SQL query to verify employee credentials
            cursor.execute("SELECT * FROM carmax_employees WHERE userid = %s AND passwd = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Welcome {user[2]}!")
                employee = Employee(user[0], user[2], user[3], user[4], user[5])
                employee.menu(db)
                break
        print("Invalid username or password. Please try again.")
    db.close()


# Signup Function
def signup():
    db = Database()
    while True:
        user_type = int(input("Sign up as: \n1. Employee \n2. Customer \nPlease input your choice: "))
        if user_type not in [1, 2]:
            print("Invalid choice. Please enter 2 for customer or 1 for employee.")
            continue
        if user_type == 2:
            userid = input("Enter username: ")
            password = input("Enter password: ")
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            email = input("Enter email: ")
            cursor = db.get_cursor()
            # SQL query to insert a new customer
            cursor.execute(
                "INSERT INTO carmax_customers (userid, passwd, fname, lname, email) VALUES (%s, %s, %s, %s, %s)",
                (userid, password, fname, lname, email))
        elif user_type == 1:
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
            cursor = db.get_cursor()
            # SQL query to insert a new employee
            cursor.execute("INSERT INTO carmax_employees (userid, passwd, fname, lname, email, position) VALUES (%s, %s, %s, %s, %s, %s)",(userid, password, fname, lname, email, position))
        db.commit()
        print("Signup successful. You can now login.")
        break
    db.close()


# Main application
print("Welcome to Carmax in Mission, Texas!")
while True:
    print("1. Login \n2. Signup \n3. Exit")
    choice = input("Please input your choice: ")
    if choice == "3":
        print("Thank you!")
        break
    elif choice == "1":
        login()
    elif choice == "2":
        signup()
    else:
        print("Invalid choice, please try again.")
        continue
