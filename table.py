from flask_table import Table, Col

class ItemTable(Table):
    """Creates a class that contains all the data for the table.
    Contains: date, amount, category, description
    """
    date = Col('Date')
    amount = Col('Amount')
    category = Col('Category')
    description = Col('Description')

class Item(object):
    """Creates a class that contains one entry worht of data.
    """
    def __init__(self, date, amount, category, description, border=True):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

def create_items(data):
    """takes in raw data from SQL and coverts it into an Item object.
    """
    lst = []
    for item in data:
        entry = Item(item[0], item[1], item[2], item[3])
        lst.append(entry)
    return lst

