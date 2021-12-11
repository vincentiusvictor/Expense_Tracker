import matplotlib.pyplot as plt
from data import pull_table

def filt2(expenses):
    """filter the amount and date from the expenses"""
    lst = []
    for item in expenses:
        lst.append(item[0:2])
    return lst

def convert_dict2(expenses):
    """"add up the amount under the same date and store it in a dictionary"""
    d = {}
    for item in expenses:
        if item[0] not in d:
            d[item[0]] = item[1]
        else:
            d[item[0]] += item[1]
    return d

def time_plot(expenses):
    """make a line chart based on the dictionary"""
    dates = list(expenses.keys())           
    amount = list(expenses.values())        
    plt.plot_date(dates, amount, '-') 
    # plt.show()
    plt.title('Total Expenses Over Time')
    plt.xlabel('Time')
    plt.ylabel('Total expense ($)')
    plt.savefig("static/output2.jpg")
    plt.close()


# data = pull_table("expenses")
# print(data)
# filtered_data2 = filt2(data)
# print(filtered_data2)
# processed_data2 = convert_dict2(filtered_data)
# print(processed_data2)
# time_plot(processed_data2)

