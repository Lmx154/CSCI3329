from pandastable import Table, TableModel
import tkinter as tk
import pandas as pd
import mysql.connector as mc

# connect database
db = mc.connect(host="34.170.66.255", user="root", passwd="password", database="carmax")
cursor = db.cursor()
cursor.execute("SELECT vin, make, model, mileage, year, price, color FROM cars")
rows = cursor.fetchall()
# get data
columns = ['VIN', 'Make', 'Model', 'Mileage', 'Year', 'Price', 'Color']
df = pd.DataFrame(rows, columns=columns)
# tkinter window
root = tk.Tk()
root.geometry("650x300")
frame = tk.Frame(root)
frame.pack(fill='x', expand=True)
# window
pt = Table(frame)
pt.updateModel(TableModel(df))
pt.show()

root.mainloop()
