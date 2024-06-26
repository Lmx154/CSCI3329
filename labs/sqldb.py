import mysql.connector as mc

db = mc.connect(host="", user="root", password="")
print(db)
cursor = db.cursor()
sql = "SELECT * FROM cars;"
cursor.execute(s)