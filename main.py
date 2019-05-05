# TODO: provide unlimited number of entries for bills paid
# TODO: calculate the finances and provide visual rep. using matplotlib
# TODO: give suggestion as to how the user can save their money
# TODO: try to implement different ttk themes

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from appJar import gui



def plotfinances(btn):


app = gui("Budget App", "378x265")



app.addEntry("Payments")
app.setEntryDefault("Payments", "Enter payment amounts here")



app.go()