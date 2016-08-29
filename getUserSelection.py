from tkinter import *
from tkinter import ttk

# Closes tkinter box
def quit(root):
    root.destroy()

# If user presses button
def pressAcceptButton():
    if (combobox1.get() in ("Past Hour", "Past Day", "Past 7 Days", "Past 30 Days") and
                combobox2.get() in ("1.0+", "2.5+", "4.5+","--ALL--") and
                combobox3.get() in ("Magnitude", "Depth", "Time", "Time Zone", "Felt Reports", "Max reported intensity",
                             "Max instrumental intensity", "Epicenter to station distance",
                             "Root mean squared travel time", "Gap between closest stations") and
                combobox4.get() in ("Magnitude", "Depth", "Time", "Time Zone", "Felt Reports", "Max reported intensity",
                             "Max instrumental intensity", "Epicenter to station distance",
                             "Root mean squared travel time", "Gap between closest stations")):
        if combobox3.get() != combobox4.get():
            userSelection.append(combobox1.get())
            userSelection.append(combobox2.get())
            userSelection.append(combobox3.get())
            userSelection.append(combobox4.get())
            quit(root)
        else:
            # TODO convert this into a popup box
            print("Please select 2 different variables for x and y")
    else:
        # TODO convert this into a popup box
        print("Please select one of the presented options")

# GUI
def getUserSelection():
    global root, combobox1, combobox2, combobox3, combobox4, userSelection
    userSelection = []
    root = Tk()

    # TODO ask user what they want to plot
    # Opt: magnitude, depth, time, time zone, felt reports, cdi (max reported intensity), mmi (max estimated instrumental
    # intensity), dmin (horizontal distance from the epicenter to the nearest station), rms (root mean squared travel
    # time), gap (largest azimuthal gap between azimuthally adjacent stations),
    #Labels
    chooseOption = ttk.Label(root, text="Please choose an option from the list below, then click accept.")
    chooseOption.grid(row=0, column=0, sticky=W)
    choiceDescription1 = ttk.Label(root, text="Display earthquake data from:")
    choiceDescription1.grid(row=1, column=0, sticky=W)
    choiceDescription2 = ttk.Label(root, text="Display earthquakes with magnitudes:")
    choiceDescription2.grid(row=2, column=0, sticky=W)
    choiceDescription3 = ttk.Label(root, text="What would you like to plot on the x-axis?")
    choiceDescription3.grid(row=3, column=0, sticky=W)
    choiceDescription4 = ttk.Label(root, text="What would you like to plot on the y-axis?")
    choiceDescription4.grid(row=4, column=0, sticky=W)
    # Comboboxes
    description1 = StringVar()
    combobox1 = ttk.Combobox(root, textvariable=description1)
    combobox1.config(values=("Past Hour", "Past Day", "Past 7 Days", "Past 30 Days"))
    combobox1.grid(row=1, column=1)
    description2 = StringVar()
    combobox2 = ttk.Combobox(root, textvariable=description2)
    combobox2.config(values=("1.0+", "2.5+", "4.5+","--ALL--"))
    combobox2.grid(row=2, column=1)
    description3 = StringVar()
    combobox3 = ttk.Combobox(root, textvariable=description3)
    combobox3.config(values=("Magnitude", "Depth", "Time", "Time Zone", "Felt Reports", "Max reported intensity",
                             "Max instrumental intensity", "Epicenter to station distance",
                             "Root mean squared travel time", "Gap between closest stations"))
    combobox3.grid(row=3, column=1)
    description4 = StringVar()
    combobox4 = ttk.Combobox(root, textvariable=description4)
    combobox4.config(values=("Magnitude", "Depth", "Time", "Time Zone", "Felt Reports", "Max reported intensity",
                             "Max instrumental intensity", "Epicenter to station distance",
                             "Root mean squared travel time", "Gap between closest stations"))
    combobox4.grid(row=4, column=1)
    # Button
    acceptButton = ttk.Button(root, text="Accept", command=pressAcceptButton)
    acceptButton.grid(row=5, column=1, sticky=E)

    #Launch GUI
    root.mainloop()
    return userSelection

if __name__ == '__main__':
    print(getUserSelection())