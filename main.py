# TODO: provide unlimited number of entries for bills paid
# TODO: calculate the finances and provide visual rep. using matplotlib
# TODO: give suggestion as to how the user can save their money
# TODO: try to implement different ttk themes

import matplotlib.pyplot as plt
from appJar import gui


def plotvalues(btn):
    values = app.getEntry("e1")
    new_list = list(map(int, values.split(",")))
    plt.plot(new_list)
    plt.ylabel('Payment Made')
    plt.show()


app = gui("Budget App", "378x265")
app.setBg("grey")

app.addEntry("e1")
app.addButton("Values", plotvalues)



app.go()