import sqlite3

conn = sqlite3.connect("expense.db")
c = conn.cursor()

def check_table(table):
    check = c.execute(f" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' ").fetchall()
    return check[0][0]

def delete_table(table):
    c.execute(f"DROP TABLE {table}")

def create_table(table): 
    c.execute(f"CREATE TABLE {table} (amount DECIMAL(30,2), description VARCHAR(100))")

def pull_table(payments):
    all = c.execute(f"SELECT * FROM {payments}").fetchall()
    return all

def insert_data(table, amount, description):
    c.execute(f"INSERT INTO {table} VALUES ({amount}, '{description}')")


def main():
    """"""
    delete_table("payments")
    create_table("payments")
    # print(check_table("payments"))

    insert_data("payments", 500, 'lunch')
    insert_data("payments", 200, 'dinner')
    
    print(
        pull_table("payments")
    )

if __name__ == "__main__":
    main()
