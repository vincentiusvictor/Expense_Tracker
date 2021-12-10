from os import name
from flask import Flask, render_template, request

import sqlite3 as sql
from table import ItemTable, Item, create_items

conn = sql.connect("database.db")
c = conn.cursor()
check = c.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' ").fetchall()
if check[0][0] == 0:
    c.execute(f"CREATE TABLE expenses (date DATE, amount DECIMAL(30,2), category VARCHAR(25), description VARCHAR(100))")
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
        time = request.form["date"]
        amount = request.form["amount"]
        category = request.form["categories"]
        description = request.form["description"]
        
        if amount and category:
            with sql.connect("database.db") as conn:
                c = conn.cursor()
                c.execute(f"INSERT INTO expenses VALUES ('{time}', {amount}, '{category}', '{description}')")
                conn.commit()
                return render_template("entry_success.html")
        else:
            return render_template("entry_fail.html")
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
        items = create_items(data)
        return render_template("results.html", table = ItemTable(items))

if __name__ == '__main__': 
    app.run(debug=True)