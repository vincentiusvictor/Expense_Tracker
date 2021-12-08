import database as d

def create_new_table(name):
    """creates a new table entry in the database, 
    if the table exists delete it and create a new one"""
    if d.check_table(name) == 1:
        d.delete_table(name)
    else:
        d.create_table(name)
        

def add_entry(name, amount, description):
    d.insert_data(name, amount, description)
    

