import mysql.connector as mc

db = mc.connect(host="34.170.66.255", user="root", passwd="password", database="carmax")
cursor = db.cursor()
cursor.execute("SELECT vin, make, model, mileage, year, price, color FROM cars")
rows = cursor.fetchall()
print(f"{'VIN':<10} {'Make':<10} {'Model':<10} {'Mileage':<10} {'Year':<5} {'Price':<7} {'Color':<7}")
for row in rows:
    print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<5} {row[5]:<8} {row[6]:<7}")

