import matplotlib.pyplot as plt

def plotEq(data):
    #x and y coordinates of plot
    xVal = []
    yVal = []

    for i in data:
        if i[1] != None:
            xVal.append(i[1])
        else:
            xVal.append(0)
        if i[2] != None:
            yVal.append(i[2])
        else:
            yVal.append(0)

    #TODO label x/y axis and make graph look cleaner
    #TODO allow user to interact with plot of earthquakes by clicking on data points (is this possible??)
    #Formatting grapth
    plt.plot(xVal, yVal, "r.")
    plt.axis([int(min(xVal)), int(max(xVal))+1, 0, int(max(yVal))+1])
    print(int(max(yVal))+1)
    plt.xlabel("Earthquake Magnitude")
    plt.ylabel("Number of Felt Reports")
    plt.title("Earthquake Felt Reports and Magnitude")

    plt.show()