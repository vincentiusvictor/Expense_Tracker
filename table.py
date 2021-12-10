from flask_table import Table, Col

class ItemTable(Table):
    date = Col('Date')
    amount = Col('Amount')
    category = Col('Category')
    description = Col('Description')

class Item(object):
    def __init__(self, date, amount, category, description, border=True):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

def create_items(data):
    lst = []
    for item in data:
        entry = Item(item[0], item[1], item[2], item[3])
        lst.append(entry)
    return lst

