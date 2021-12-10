import matplotlib.pyplot as plt
from data import pull_table

def time_plot(expenses):
    time = []
    for item in expenses:
        time.append(item[0])
    values = []
    for item in expenses:
        values.append(item[1])
    print(time)
    plt.plot(time,values)
    plt.title('Expenses during the time')
    plt.xlabel('Time')
    plt.ylabel('Total expense ($)')
    # plt.show()
    plt.savefig("templates/output2.jpg")

data = pull_table("expenses")
time_plot(data)