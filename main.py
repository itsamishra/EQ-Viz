# Name: Earthquake Visualization
# Description: An app that visualizes data from USGS using the matplotlib library
# Author: Ashutosh Mishra

import earthquakeData, getUserSelection, getURL
#import plot

# Get relevent URL from: http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

userChoice = getUserSelection.getUserSelection()

url = getURL.getURL(userChoice)
print(url)

# Gets earthquake data from USGS
eqData = earthquakeData.getEqData(url)
print(eqData)


#plot.plotEq(eqData)