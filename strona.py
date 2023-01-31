from flask import Flask, render_template
import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user='root',
                                     password='', database='sys')

cursor = connection.cursor()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hodowle")
def hodowle():
    cursor.execute("select * from hodowle")
    value = cursor.fetchall()
    return render_template("hodowle.html", data=value)


@app.route("/rasypsow")
def rasypsow():
    cursor.execute('SELECT * FROM `rasy psow`')
    value = cursor.fetchall()
    return render_template("rasypsow.html", data=value)


if __name__ == "__main__":
    app.run(debug=True)
