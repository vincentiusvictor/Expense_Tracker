import matplotlib.pyplot as plt
from data import pull_table

def filt(expenses):
    """filter the amount and category from the expenses"""
    lst = []
    for item in expenses:
        lst.append(item[1:3])
    return lst

def convert_dict(expenses):
    """add up the amount under the same category and store it in a dictionary"""
    d = {}
    for item in expenses:
        if item[1] not in d:
            d[item[1]] = item[0]
        else:
            d[item[1]] += item[0]
    return d

def bar_graph(expenses):
    """make a bar graph based on the dictionary"""
    cat = list(expenses.keys())
    values = list(expenses.values())
    plt.bar(cat, values, color ='maroon', width = 0.4)
    plt.xlabel("Categories")
    plt.ylabel("Total amount in $")
    plt.title("Total Expenses per Category ")
    # plt.show()
    plt.savefig("static/output1.jpg")
    plt.close()

# data = pull_table("expenses")
# print(data)
# filtered_data = filt(data)
# # print(filtered_data)
# processed_data = convert_dict(filtered_data)
# # print(processed_data)
# bar_graph(processed_data)

