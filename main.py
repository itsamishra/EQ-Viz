# Name: Earthquake Visualization
# Description: An app that visualizes data from USGS using the matplotlib library
# Author: Ashutosh Mishra

import earthquakeData, getUserSelection, getUserChoice, plot

# Gets url that user requests
userChoice = getUserSelection.getUserSelection()

url = getUserChoice.getURL(userChoice)

# Gets earthquake data from USGS
eqData = earthquakeData.getEqData(url)

# Plots requested earthquake data
plot.plotEq(userChoice, eqData)