from flask import Flask, render_template, url_for, redirect, request
import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user='root',
                                     password='', database='sys')

cursor = connection.cursor()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Coś poszło nie tak. Spróbuj ponownie'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route("/index")
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


@app.route("/champ")
def Championy():
    cursor.execute('SELECT * FROM `championy`')
    value = cursor.fetchall()
    return render_template("champ.html", data=value)


@app.route("/dodr", methods=['GET', 'POST'])
def dodr():
    if request.method == "POST":
        rasa = request.form["rasa"]
        waga = request.form["waga"]
        wzrost = request.form["wzrost"]

        cursor.execute('INSERT INTO `users`(`user`, `password`, `iq`) '
                       'VALUES ("%s","%s","%s")'
                       % (rasa, waga, wzrost))
        connection.commit()
    return render_template("dodr.html")









if __name__ == "__main__":
    app.run(debug=True)
