import matplotlib.pyplot as plt
import pandas as pd
from data import insert_data, pull_table

def filter(expenses):
    lst = []
    for item in expenses:
        lst.append(item[1:3])
    return lst

def convert_dict(expenses):
    d = {}
    for item in expenses:
        if item[1] not in d:
            d[item[1]] = item[0]
        else:
            d[item[1]] += item[0]
    return d

def bar_graph(expenses):
    cat = list(expenses.keys())
    values = list(expenses.values())
    plt.bar(cat, values, color ='maroon', width = 0.4)
    plt.xlabel("Expenses Category")
    plt.ylabel("Total amount in $")
    plt.title("Total amount of $ of expense per category ")
    plt.show()

def filter_2(expenses):
    lst = []
    for item in expenses:
        lst.append(item[0:2])
    return lst

def convert_dict_2(expenses):
    d = {}
    for item in expenses:
        if item[0] not in d:
            d[item[0]] = item[1]
        else:
            d[item[0]] += item[1]
    return d

def time_plot(expenses):
    time = []
    for item in expenses:
        time.append(item[0])
    values = []
    for item in expenses:
        time.append(item[2])
    return values




data = pull_table("expenses")
print(data)
filtered_data = filter(data)
# print(filtered_data)
processed_data = convert_dict(filtered_data)
# print(processed_data)
# bar_graph(processed_data)
filtered_data_2 = filter_2(data)
# print(filtered_data_2)
processed_data_2 = convert_dict_2(filtered_data_2)
# print(processed_data_2)
print(time_plot(data))
