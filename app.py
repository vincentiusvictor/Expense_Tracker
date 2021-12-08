from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    print("Hello")

@app.route("/new_entry")
def new_entry():
    """
    """

@app.route("/show_all")
def show_all():
    """
    """