from tkinter import *
from tkinter import ttk

# Closes tkinter box
def quit(root):
    root.destroy()

# If user presses button
def pressAcceptButton():
    if (combobox1.get() in ("Past Hour", "Past Day", "Past 7 Days", "Past 30 Days") and
                combobox2.get() in ("1.0+", "2.5+", "4.5+")):
        userSelection.append(combobox1.get())
        userSelection.append(combobox2.get())
        quit(root)
    else:
        print("Please select one of the presented options")

def getUserSelection():
    global root, combobox1, combobox2, userSelection
    userSelection = []
    root = Tk()

    #Labels
    chooseOption = ttk.Label(root, text="Please choose an option from the list below, then click accept.")
    chooseOption.grid(row=0, column=0, sticky=W)
    choiceDescription1 = ttk.Label(root, text="Display earthquake data from:")
    choiceDescription1.grid(row=1, column=0, sticky=W)
    choiceDescription2 = ttk.Label(root, text="Display earthquakes with magnitudes:")
    choiceDescription2.grid(row=2, column=0, sticky=W)
    description1 = StringVar()
    # Comboboxes
    combobox1 = ttk.Combobox(root, textvariable=description1)
    combobox1.config(values=("Past Hour", "Past Day", "Past 7 Days", "Past 30 Days"))
    combobox1.grid(row=1, column=1)
    description2 = StringVar()
    combobox2 = ttk.Combobox(root, textvariable=description2)
    combobox2.config(values=("1.0+", "2.5+", "4.5+"))
    combobox2.grid(row=2, column=1)
    # Button
    acceptButton = ttk.Button(root, text="Accept", command=pressAcceptButton)
    acceptButton.grid(row=3, column=1, sticky=E)

    #Launch GUI
    root.mainloop()
    return userSelection

if __name__ == '__main__':
    print(getUserSelection())