from os import name
from flask import Flask, render_template, request

from datetime import datetime
import sqlite3 as sql

conn = sql.connect("database.db")
c = conn.cursor()
check = c.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' ").fetchall()
if check[0][0] == 0:
    c.execute(f"CREATE TABLE expenses (date DATETIME, amount DECIMAL(30,2), category VARCHAR(25), description VARCHAR(100))")
conn.commit()
conn.close()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/new_entry/", methods=["GET", "POST"])
def new_entry():
    """add a new expense. redirect to previous and next page
    """
    if request.method == "POST":
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        amount = request.form["amount"]
        category = request.form["categories"]
        description = request.form["description"]
        
        with sql.connect("database.db") as conn:
            c = conn.cursor()
            c.execute(f"INSERT INTO expenses VALUES ('{time}', {amount}, '{category}', '{description}')")
            conn.commit()
            return render_template("entry_success.html")
    else:
        return render_template("new_entry_form.html", error = True)


@app.route("/show_all")
def show_all():
    """show all of the expenses. redirect to new entry and main page 
    """
    with sql.connect("database.db") as conn:
        c = conn.cursor()
        data = c.execute("SELECT * FROM expenses").fetchall()
        conn.commit()
        return render_template("results.html", data = data)

if __name__ == '__main__': 
    app.run(debug=True)