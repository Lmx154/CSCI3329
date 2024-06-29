from flask import Flask, render_template
import mysql.connector as mc

db = mc.connect(
    host="34.170.66.255",
    user="root",
    passwd="password",
    database="carmax"
)
cursor = db.cursor()
cursor.execute("SELECT vin, make, model, mileage, year, price, color FROM cars")
rows = cursor.fetchall()
app = Flask(__name__)


@app.route('/Lab')
def result():
    return render_template('inventory.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
