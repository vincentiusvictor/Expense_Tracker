from os import name
from flask import Flask, render_template, request

from postgresql import insert_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/new_entry/", methods=["GET", "POST"])
def new_entry():
    """add a new expense. redirect to previous and next page
    """
    if request.method == "POST":
        number = request.form["amount"]
        cat = request.form["category"]
        new_expense = insert_data(name, number, cat)
        return render_template("new_entry_form.html", new_expense)
    else:
        return render_template("new_entry_form.html", error = True)


@app.route("/show_all")
def show_all():
    """show all of the expenses. redirect to new entry and main page 
    """
    pass

if __name__ == '__main__': 
    app.run(debug=True)