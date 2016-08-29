import matplotlib.pyplot as plt

def plotEq(data):
    #x and y coordinates of plot
    xVal = []
    yVal = []

    #xAnswer = input()
    #yAnswer = input()
    xAnswer = "magnitude"
    yAnswer = "feltReports"
    for i in range(len(data)):
        if getattr(data[i], xAnswer) != None:
            xVal.append(getattr(data[i], xAnswer))
        else:
            xVal.append(0)
        if getattr(data[i], yAnswer) != None:
            yVal.append(getattr(data[i], yAnswer))
        else:
            yVal.append(0)

    for i in range(len(xVal)):
        print(xVal[i],yVal[i])

    '''
    for i in data:
        if i[1] != None:
            xVal.append(i[1])
        else:   #If i[1] == None
            xVal.append(0)
        if i[2] != None:
            yVal.append(i[2])
        else:   #If i[2] == None
            yVal.append(0)
    '''

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
    plt.savefig("assets/plot")


if __name__ == '__main__':
    import earthquakeData
    data = earthquakeData.getEqData("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    plotEq(data)