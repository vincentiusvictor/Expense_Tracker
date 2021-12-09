from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/new_entry")
def new_entry():
    """add a new expesne. redirect to previous and necct page
    """
    pass
###Post and get

@app.route("/show_all")
def show_all():
    """ redirect to new entry and main page 
    """
    pass

if __name__ == '__main__':
    app.run(debug=True)