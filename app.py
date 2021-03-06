from flask import Flask, render_template, request
import sqlite3 as sql
from table import ItemTable, create_items
from bar_chart import filt, convert_dict, bar_graph
from line_chart import filt2, convert_dict2, time_plot

def create_db():
    """Creates the databse with a table named 'expenses'.
    """
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
    """Creates the home page of the web application.
    """
    return render_template("main_page.html")

@app.route("/new_entry/", methods=["GET", "POST"])
def new_entry():
    """Page to add a new expense. If successful show entry_success, If fail show entry_fail. 
    Link to redirect to show data and show graphs.
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
    """Page that showw all of the expenses. Link to redirect to home page.
    """
    with sql.connect("database.db") as conn:
        c = conn.cursor()
        data = c.execute("SELECT * FROM expenses").fetchall()
        conn.commit()
        items = create_items(data)
        return render_template("results.html", table = ItemTable(items))

@app.route("/delete", methods=["GET", "POST"])
def delete():
    """Page to authorize data erasure. Has a yes or no option.
    """
    if request.method == "POST":
        try:
            with sql.connect("database.db") as conn:
                c = conn.cursor()
                c.execute("DROP TABLE expenses")
                c.execute("CREATE TABLE expenses (date DATE, amount DECIMAL(30,2), category VARCHAR(25), description VARCHAR(100))")
                conn.commit()
        finally:
            return render_template("main_page.html")
    else:
        return render_template("delete.html")

@app.route("/graph")
def graph():
    """Page that shows all the graphs based on data. Link to redirect to home page.
    """ 
    with sql.connect("database.db") as conn:
        c = conn.cursor()
        data = c.execute(f"SELECT * FROM expenses").fetchall()
    filtered_data = filt(data)
    processed_data = convert_dict(filtered_data)
    filtered_data_2 = filt2(data)
    processed_data_2 = convert_dict2(filtered_data_2)
    bar_graph(processed_data)
    time_plot(processed_data_2)
    return render_template("graph.html")

def start_app():
    create_db()
    app.run(debug=True)

def main():
    start_app()

if __name__ == '__main__': 
    main()