import matplotlib.pyplot as plt

def plotEq(data):
    #x and y coordinates of plot
    xVal = []
    yVal = []

    for i in data:
        if i[1] != None:
            xVal.append(i[1])
        else:   #If i[1] == None
            xVal.append(0)
        if i[2] != None:
            yVal.append(i[2])
        else:   #If i[2] == None
            yVal.append(0)

    #TODO add labels indicating what time period and magnitude range is being plotted (e.g. past hour/1.0+)
    #Plotting graph
    plt.plot(xVal, yVal, "r.")
    #Formatting graph
    plt.axis([min(xVal)-0.1, max(xVal)+0.1, -(1/20)*max(yVal),(21/20)*max(yVal)])
    print(min(xVal))
    print(max(xVal))
    plt.xlabel("Earthquake Magnitude")
    plt.ylabel("Number of Felt Reports")
    plt.title("Earthquake Felt Reports and Magnitude")
    plt.grid()

    #plt.show()
    plt.savefig("plot")


if __name__ == '__main__':
    plotEq([['57km SSE of Chignik Lake, Alaska', 5, None], ['Southwest Indian Ridge', 4.8, None], ['86km S of Unalaska, Alaska', 4.5, None], ['49km NNE of Visokoi Island, South Georgia and the South Sandwich Islands', 5.4, None], ['Owen Fracture Zone region', 4.9, None], ['9km W of Sarahan, India', 4.6, 3], ['7km S of Sanchez, Dominican Republic', 4.5, 51]])