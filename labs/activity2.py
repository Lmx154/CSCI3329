cursor.execute("SELECT userid, fname, lname, email, position FROM carmax_employees")
rows = cursor.fetchall()
print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<15} {'Position':<10}")
print(f"{row[0]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<5}")

elif choice == '5':
    cursor = db.cursor()
    cursor.execute("""
        SELECT c.userid, c.fname, c.lname, c.email, GROUP_CONCAT(cc.vin SEPARATOR ', ') AS cart
        FROM carmax_customers c
        LEFT JOIN customer_cart cc ON c.userid = cc.customer_id
        GROUP BY c.userid, c.fname, c.lname, c.email
    """)
    rows = cursor.fetchall()
    print(f"{'ID':<10} {'F_Name':<10} {'L_Name':<10} {'Email':<20} {'Cart':<10}")
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<20} {row[4]:<10}")
