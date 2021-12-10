import matplotlib.pyplot as plt
from data import pull_table

def filt(expenses):
    lst = []
    for item in expenses:
        lst.append(item[0:2])
    return lst

def convert_dict(expenses):
    d = {}
    for item in expenses:
        if item[0] not in d:
            d[item[0]] = item[1]
        else:
            d[item[0]] += item[1]
    return d

def time_plot(expenses):
    dates = list(expenses.keys())           
    amount = list(expenses.values())        
    plt.plot_date(dates, amount, '-') 
    plt.show()
    plt.title('Expenses during the time')
    plt.xlabel('Time')
    plt.ylabel('Total expense ($)')
    plt.savefig("templates/output2.jpg")
    plt.close()


data = pull_table("expenses")
# print(data)
filtered_data = filt(data)
# print(filtered_data)
processed_data = convert_dict(filtered_data)
# print(processed_data)
time_plot(processed_data)

