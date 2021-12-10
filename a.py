import sqlite3
from datetime import datetime

conn = sqlite3.connect("expense.db")
c = conn.cursor()

def check_table(table):
    """check if a table exists"""
    check = c.execute(f" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' ").fetchall()
    return check[0][0]

def delete_table(table):
    """delete a new table in the database
    """
    c.execute(f"DROP TABLE {table}")

def create_table(table): 
    """creates a new table in the database
    """
    c.execute(f"CREATE TABLE {table} (date DATETIME, amount DECIMAL(30,2), category VARCHAR(25), description VARCHAR(100))")

def pull_table(payments):
    """pulls data from a table
    """
    all = c.execute(f"SELECT * FROM {payments}").fetchall()
    return all

def insert_data(table, amount, category, description):
    """Inserts a new entry into a table
    """
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.execute(f"INSERT INTO {table} VALUES ('{time}', {amount}, '{category}' '{description}')")


def main():
    """"""
    # delete_table("payments")
    # create_table("payments")
    # print(check_table("payments"))

    insert_data("payments", 500, 'lunch')
    insert_data("payments", 200, 'dinner')
    
    print(
        pull_table("payments")
    )

if __name__ == "__main__":
    main()
