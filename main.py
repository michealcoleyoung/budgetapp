# TODO: provide unlimited number of entries for bills paid
# TODO: calculate the finances and provide visual rep. using matplotlib
# TODO: give suggestion as to how the user can save their money
# TODO: try to implement different ttk themes

import matplotlib.pyplot as plt
from appJar import gui
plt.style.use('ggplot')


def plotvalues(btn):
    plt.xlabel("Months 1 - 4")
    plt.ylabel('Amounts Payed')
    plt.title("Billing Amounts Payed")
    x = ["month 1", "month 2", "month 3", "month 4"]
    values = app.getEntry("e1")
    new_list = list(map(float, values.split(",")))
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, new_list, color='green')
    plt.xticks(x_pos, x)
    app.setLabel("s1", new_list[3] - new_list[2])

    plt.show()

    # sets amount saved values


def clear(btn):
    app.clearAllEntries()
    app.clearLabel("s1")


app = gui("Budget App", "378x265")
app.setBg("grey")

app.addEntry("e1")
app.addLabel("Savings Month 1")
app.addLabel("s1", "")
app.addLabel("Savings Month 2")
app.addLabel("s2", "")
app.addLabel("Savings Month 3")
app.addLabel("s3", "")
app.addLabel("Savings Month 4")
app.addLabel("s4", "")
app.addButtons(["Values", "Clear"], [plotvalues, clear])


app.go()