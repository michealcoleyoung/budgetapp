# TODO: provide unlimited number of entries for bills paid
# TODO: calculate the finances and provide visual rep. using matplotlib
# TODO: give suggestion as to how the user can save their money
# TODO: try to implement different ttk themes

import matplotlib.pyplot as plt
from appJar import gui


def plotfinances(btn):
    plt.plot([int(app.getEntry("e1")), int(app.getEntry("e2")), int(app.getEntry("e3"))])
    plt.ylabel('some numbers')
    plt.show()





app = gui("Budget App", "378x265")
app.setBg("grey")


app.startTabbedFrame("TabbedFrame")  # tab frame start

app.startTab("Expenses")
app.addEntry("e1")
app.addEntry("e2")
app.addEntry("e3")
app.addEntry("e4")
app.addEntry("e5")
app.addEntry("e6")
app.addEntry("e7")
app.addEntry("e8")
app.addEntry("e9")
app.addEntry("e10")
app.addButton("PLOT", plotfinances)



app.stopTab()

app.startTab("Graph")
# This will include the graph with all expenses
app.stopTab()

app.stopTabbedFrame()  # tab frame end


app.go()