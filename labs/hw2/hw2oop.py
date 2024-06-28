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


# Customer class inheriting from User
class Customer(User):
    def __init__(self, user_id, fname, lname, email):
        super().__init__(user_id, fname, lname, email)

    def display_inventory(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars WHERE is_available = 1")
            rows = cursor.fetchall()
            self._print_inventory(rows)

    def sort_inventory(self, sort_column):
        with Database() as db:
            cursor = db.get_cursor()
            query = f"SELECT vin, type, brand, model, year, mileage, price, color, feature FROM cars WHERE is_available = 1 ORDER BY {sort_column}"
            cursor.execute(query)
            rows = cursor.fetchall()
            self._print_inventory(rows)

    def add_to_cart(self, vin):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("SELECT model FROM cars WHERE vin = %s", (vin,))
            car_model = cursor.fetchone()
            if car_model:
                cursor.execute("INSERT INTO customer_cart (customer_id, vin) VALUES (%s, %s)", (self.user_id, vin))
                cursor.execute("UPDATE cars SET is_available = 0 WHERE vin = %s", (vin,))
                db.commit()
                print(f"{car_model[0]} has been added to your cart!")
            else:
                print("Car with that VIN not found.")

    def view_cart(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("""
                SELECT c.vin, c.type, c.brand, c.model, c.year, c.mileage, c.price, c.color, c.feature
                FROM cars c
                JOIN customer_cart cc ON c.vin = cc.vin
                WHERE cc.customer_id = %s
            """, (self.user_id,))  # Fetch car info from columns in car table joined with cart table filtered by customer id
            rows = cursor.fetchall()
            self._print_inventory(rows)

    def empty_cart(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("SELECT vin FROM customer_cart WHERE customer_id = %s", (self.user_id,))
            rows = cursor.fetchall()
            for row in rows:
                cursor.execute("UPDATE cars SET is_available = 1 WHERE vin = %s", (row[0],))
            cursor.execute("DELETE FROM customer_cart WHERE customer_id = %s", (self.user_id,))
            db.commit()
            print("Cart emptied, your car/s are no longer reserved.")

    @staticmethod
    def _print_inventory(rows):
        print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")
        for row in rows:
            print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")


# Employee class inheriting from User
class Employee(User):
    def __init__(self, user_id, fname, lname, email, position):
        super().__init__(user_id, fname, lname, email)
        self.position = position

    def display_inventory(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("SELECT vin, type, brand, model, year, mileage, price, color, feature, is_available FROM cars")
            rows = cursor.fetchall()
            self._print_inventory(rows, show_is_available=True)

    def add_car(self, vin, car_type, brand, model, year, mileage, price, color, feature, is_available):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute(
                "INSERT INTO cars (vin, type, brand, model, year, mileage, price, color, feature, is_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (vin, car_type, brand, model, year, mileage, price, color, feature, is_available))
            db.commit()
            print("Car added successfully.")

    def delete_car(self, vin):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("DELETE FROM cars WHERE vin = %s", (vin,))
            db.commit()
            print("Car deleted successfully.")

    def update_car(self, vin, update_choice, new_value):
        columns = ["brand", "model", "year", "mileage", "price", "color", "feature", "is_available"]
        column_name = columns[update_choice - 1]
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute(f"UPDATE cars SET {column_name} = %s WHERE vin = %s", (new_value, vin))
            db.commit()
            print(f"{column_name.capitalize()} updated successfully.")

    def display_customers(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("""
                SELECT c.userid, c.fname, c.lname, c.email, GROUP_CONCAT(cc.vin SEPARATOR ', ') AS cart
                FROM carmax_customers c
                LEFT JOIN customer_cart cc ON c.userid = cc.customer_id
                GROUP BY c.userid, c.fname, c.lname, c.email
            """)  # Fetch customer info and their cart details
            rows = cursor.fetchall()
            print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Cart':<10}")
            for row in rows:
                row = [r if r is not None else '' for r in row]
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")

    def display_employees(self):
        with Database() as db:
            cursor = db.get_cursor()
            cursor.execute("SELECT userid, fname, lname, email, position FROM carmax_employees")
            rows = cursor.fetchall()
            print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Position':<10}")
            for row in rows:
                row = [r if r is not None else '' for r in row]
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")

    @staticmethod
    def _print_inventory(rows, show_is_available=False):
        if show_is_available:
            print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10} {'Availability':<12}")
        else:
            print(f"{'VIN':<10} {'Type':<10} {'Brand':<10} {'Model':<10} {'Year':<5} {'Mileage':<8} {'Price':<7} {'Color':<7} {'Feature':<10}")
        for row in rows:
            if show_is_available:
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10} {row[9]:<12}")
            else:
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<10}")


# CarmaxApp class to handle the main application flow
class CarmaxApp:
    @staticmethod
    def main_menu():
        print("1. Login \n2. Signup \n3. Exit")

    @staticmethod
    def login():
        db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
        while True:
            user_type = int(input("Login as: \n1. Employee \n2. Customer \nPlease input your choice: "))
            if user_type not in [1, 2]:
                print("Invalid choice. Please enter 2 for customer or 1 for employee.")
                continue

            username = input("Enter username: ")
            password = input("Enter password: ")

            cursor = db.get_cursor()
            if user_type == 2:
                cursor.execute("SELECT * FROM carmax_customers WHERE userid = %s AND passwd = %s", (username, password))
                user = cursor.fetchone()
                if user:
                    print(f"Welcome {user[2]}!")
                    customer = Customer(user[0], user[2], user[3], user[4])
                    CarmaxApp.customer_menu(customer)
                    break
            elif user_type == 1:
                cursor.execute("SELECT * FROM carmax_employees WHERE userid = %s AND passwd = %s", (username, password))
                user = cursor.fetchone()
                if user:
                    print(f"Welcome {user[2]}!")
                    employee = Employee(user[0], user[2], user[3], user[4], user[5])
                    CarmaxApp.employee_menu(employee)
                    break

            print("Invalid username or password. Please try again.")
        db.close()

    @staticmethod
    def signup():
        db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")
        while True:
            user_type = int(input("Sign up as: \n1. Employee \n2. Customer \nPlease input your choice: "))
            if user_type not in [1, 2]:
                print("Invalid choice. Please enter 2 for customer or 1 for employee.")
                continue

            userid = input("Enter username: ")
            password = input("Enter password: ")
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            email = input("Enter email: ")

            cursor = db.get_cursor()
            if user_type == 2:
                cursor.execute("INSERT INTO carmax_customers (userid, passwd, fname, lname, email) VALUES (%s, %s, %s, %s, %s)",
                               (userid, password, fname, lname, email))
            elif user_type == 1:
                manager_key = input("Enter manager key: ")
                if manager_key != '1234':
                    print("Invalid manager key. Sign up failed.")
                    continue
                position = input("Enter position: ")
                cursor.execute("INSERT INTO carmax_employees (userid, passwd, fname, lname, email, position) VALUES (%s, %s, %s, %s, %s, %s)",
                               (userid, password, fname, lname, email, position))

            db.commit()
            print("Signup successful. You can now login.")
            break
        db.close()

    @staticmethod
    def customer_menu(customer):
        while True:
            print("1. Display Inventory \n2. Sort Inventory \n3. Add to cart \n4. View cart \n5. Empty cart \n6. Log out")
            choice = input("Please input your choice: ")

            if choice == '1':
                customer.display_inventory()

            elif choice == '2':
                CarmaxApp.sort_inventory(customer)

            elif choice == '3':
                vin = input("Enter VIN of the car to add to cart: ")
                customer.add_to_cart(vin)

            elif choice == '4':
                customer.view_cart()

            elif choice == '5':
                customer.empty_cart()

            elif choice == '6':
                break

    @staticmethod
    def sort_inventory(customer):
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
                customer.sort_inventory(sort_column)

    @staticmethod
    def employee_menu(employee):
        while True:
            print("1. Display Inventory \n2. Add a Car \n3. Delete a Car \n4. Update a Car")
            print("5. Display Customers \n6. Display Employees \n7. Log out")
            choice = input("Please input your choice: ")

            if choice == '1':
                employee.display_inventory()

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
                employee.add_car(vin, car_type, brand, model, year, mileage, price, color, feature, is_available)

            elif choice == '3':
                vin = input("Enter VIN of the car to delete: ")
                employee.delete_car(vin)

            elif choice == '4':
                vin = input("Enter VIN of the car to update: ")
                while True:
                    print("Update Menu \n1. Update Brand \n2. Update Model \n3. Update Year \n4. Update Mileage ")
                    print("5. Update Price \n6. Update Color \n7. Update Feature \n8. Update Availability \n9. Exit Update Menu")
                    update_choice = int(input("Please input your choice: "))
                    if 1 <= update_choice <= 8:
                        new_value = input(f"Enter new value: ")
                        employee.update_car(vin, update_choice, new_value)
                    elif update_choice == 9:
                        break
                    else:
                        print("Invalid choice, please try again.")

            elif choice == '5':
                employee.display_customers()

            elif choice == '6':
                employee.display_employees()

            elif choice == '7':
                break


if __name__ == "__main__":
    while True:
        CarmaxApp.main_menu()
        ch = input("Please input your choice: ")
        if ch == "3":
            break
        elif ch == "1":
            CarmaxApp.login()
        elif ch == "2":
            CarmaxApp.signup()
        else:
            print("Invalid choice, please try again.")
