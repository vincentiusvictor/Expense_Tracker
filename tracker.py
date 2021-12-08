import sqlite3 as sql

def create_new_table(name):
    """creates a new table entry in the database, 
    if the table exists delete it and create a new one"""
    if sql.check_table(name) == 1:
        sql.delete_table(name)
    else:
        sql.create_table(name)
        

def add_entry(name, amount, description):
    sql.insert_data(name, amount, description)


