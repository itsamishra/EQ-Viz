import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def plotEq(data):
    # x and y coordinates of plot
    xVal = []
    yVal = []

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

    #TODO add labels indicating what time period and magnitude range is being plotted (e.g. past hour/1.0+)
    #Plotting graph
    plt.plot(xVal, yVal, "r.")
    #Formatting graph
    plt.axis([min(xVal)-0.1, max(xVal)+0.1, -(1/20)*max(yVal),(21/20)*max(yVal)])
    plt.xlabel("Earthquake Magnitude")
    plt.ylabel("Number of Felt Reports")
    plt.title("Earthquake Felt Reports and Magnitude")
    plt.grid()

    plt.show()

if __name__ == '__main__':
    import earthquakeData
    data = earthquakeData.getEqData("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    plotEq(data)