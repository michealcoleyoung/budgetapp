# TODO: provide unlimited number of entries for bills paid
# TODO: calculate the finances and provide visual rep. using matplotlib
# TODO: give suggestion as to how the user can save their money
# TODO: try to implement different ttk themes

import matplotlib.pyplot as plt
from appJar import gui
plt.style.use('ggplot')


def plotvalues(btn):
    plt.xlabel("Payment Made")
    plt.ylabel('Previous Months')
    plt.title("Billing Amounts Payed")
    x = ["month 1", "month 2", "month 3", "month 4"]
    values = app.getEntry("e1")
    new_list = list(map(int, values.split(",")))
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, new_list, color='green')
    plt.xticks(x_pos, x)
    plt.show()


app = gui("Budget App", "378x265")
app.setBg("grey")

app.addEntry("e1")
app.addButton("Values", plotvalues)



app.go()