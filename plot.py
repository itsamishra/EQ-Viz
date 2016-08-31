import matplotlib, getUserChoice
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#
def plotEq(userChoice, data):
    # All x and y values that will be plotted
    xVal = []
    yVal = []

    # Adds x and y values to xVal and yVal that correspond to the variables that the user wants to plot
    xAnswer, yAnswer = getUserChoice.getXYAxis(userChoice)
    for i in data:
        if getattr(i, xAnswer) != None:
            xVal.append(getattr(i, xAnswer))
        else:
            xVal.append(0)
        if getattr(i, yAnswer) != None:
            yVal.append(getattr(i, yAnswer))
        else:
            yVal.append(0)

    #TODO add labels indicating what time period and magnitude range is being plotted (e.g. past hour/1.0+)
    #Plotting graph
    plt.plot(xVal, yVal, "r.")
    #Formatting graph
    plt.axis([-(1/20)*max(xVal), (21/20)*max(xVal), -(1/20)*max(yVal),(21/20)*max(yVal)])
    plt.xlabel(xAnswer[0].upper()+xAnswer[1:].lower())
    plt.ylabel(yAnswer[0].upper()+yAnswer[1:].lower())
    plt.title("Earthquake " + str(yAnswer[0].upper()+yAnswer[1:].lower()) + " vs " +
              str(xAnswer[0].upper()+xAnswer[1:].lower()))
    plt.grid()

    #Display the graph
    plt.show()

if __name__ == '__main__':
    import earthquakeData
    data = earthquakeData.getEqData("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    plotEq(data)