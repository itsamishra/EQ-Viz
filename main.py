import earthquakeData, getUserSelection, getURL
#import plot

# TODO add Tkinter GUI functionality (allow user to select which data they want to get from USGS)
# Get relevent URL from: http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

userChoice = getUserSelection.getUserSelection()

url = getURL.getURL(userChoice)

print(url)

# Gets earthquake data from USGS
#eqData = earthquakeData.getEqData(url)

#plot.plotEq(eqData)