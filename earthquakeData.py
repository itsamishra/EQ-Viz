import requests

class Earthquake:
    def __init__(self):
        self.id = ""
        self.location = []
        self.magnitude = 0
        self.feltReports = 0
        self.place = ""

    #def addEq(self):
    def addEq(self, JSONData, eqNum):
        # Setting id
        self.id = JSONData["features"][eqNum]["id"]
        # Setting location (format: longitude,latitude, depth)
        for i in JSONData["features"][eqNum]["geometry"]["coordinates"]:
            self.location.append(i)
        # Add from "properties" portion of JSON
        print(JSONData["features"][eqNum]["properties"])
        self.magnitude = JSONData["features"][eqNum]["properties"]["mag"]
        if JSONData["features"][eqNum]["properties"]["felt"] != None:   #If it is none, feltReports remains zero
            self.feltReports = JSONData["features"][eqNum]["properties"]["felt"]
        self.place = JSONData["features"][eqNum]["properties"]["place"]



        print("_____")


# TODO replace list with an Earthquake Data class
def getEqData(url):
    eqData = []
    eqJSON = requests.get(url).json()
    numberOfEq = eqJSON["metadata"]["count"]

    # Properties
    #for j in range(len(eqJSON["features"])):
    #    for i in eqJSON["features"][j]["properties"]:
    #        print(eqJSON["features"][0]["properties"][i])

    for i in range(numberOfEq):
        earthquake = Earthquake()
        earthquake.addEq(eqJSON, i)
        eqData.append(earthquake)

    for i in eqData:
        print(i.id,i.location,i.magnitude,i.feltReports)

#    sampleEq.addEq(eqJSON, numberOfEq)

    return None



if __name__ == '__main__':
    getEqData("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")


'''
    # Relevent earthquake info
    eqLocs = []
    eqMags = []
    eqFelt = []

    # Gathering earthquake info
    for i in eqJSON["features"]:
        eqMags.append(i["properties"]["mag"])
        eqLocs.append(i["properties"]["place"])
        eqFelt.append(i["properties"]["felt"])

    # Putting all data in single list
    eqData = []
    for i in range(len(eqLocs)):
        eqData.append([eqLocs[i], eqMags[i], eqFelt[i]])

    return eqData
    '''