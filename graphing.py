# import matplotlib.pyplot as plt
# import pandas as pd
from data import insert_data, pull_table

# def bar_graph(expenses):
#     cat = list(expenses.keys())
#     values = list(expenses.values())
#     fig = plt.figure(figsize = (10, 5))
#     plt.bar(cat, values, color ='maroon', width = 0.4)
#     plt.xlabel("Expenses Category")
#     plt.ylabel("Total amount in $")
#     plt.title("Total amount of $ of expense per category ")
#     plt.show()

# data = {"Home & Utilities":100, "Transportation":200}
# # bar_graph(data)

# insert_data("payments", 500, 'lunch')
# insert_data("payments", 200, 'dinner')


# print(a)

# def Convert(lst):
#     res_dct = {lst[i+1]: lst[i] for i in range(0, len(lst), 2)}
#     return res_dct



def filter(expenses):
    lst = []
    for item in expenses:
        lst.append(item[1:3])
    return lst


def convert_dict(expenses):
    d = {}
    for item in expenses:
        if item[1] not in d:
            d[item] = item[0]
        else:
            d[item] += item[0]
    return d


data = pull_table("expenses")
new_data = filter(data)
print(new_data)
processed_data = convert_dict(new_data)
# print(processed_data)


# for item in a:
#     a, b =list(item[1:3])
# print(a)
# print(b)
# for item in a:
#     print(item[1:3].split('\n'))

# def one_list(b):
#     list_of_lists = []
#     for line in b:
#         stripped_line = line.strip()
#         line_list = stripped_line.split()
#         list_of_lists.append(line_list)
#         b.close()
#         print(list_of_lists)

# for item in a:
#     print(one_list(item[1:3]))



# print(Convert(pull_table("payments")))

# dates = ['2015-12-20','2015-09-12']  
# PM_25 = [80, 55]
# data = pd.DataFrame({'dates':pd.to_datetime(dates),'PM_25':PM_25})
# data.plot(x='dates',y='PM_25',marker='o',linestyle='none',color='red',ms=3)
