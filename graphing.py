import numpy as np
import matplotlib.pyplot as plt

def bar_graph(expenses):
    cat = list(expenses.keys())
    values = list(expenses.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(cat, values, color ='maroon', width = 0.4)
    plt.xlabel("Expenses Category")
    plt.ylabel("Total amount in $")
    plt.title("Total amount of $ of expense per category ")
    plt.show()



data = {"Home & Utilities":100, "Transportation":200}
bar_graph(data)
