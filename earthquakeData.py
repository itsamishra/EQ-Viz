import requests

class Earthquake:
    def __init__(self):
        self.id = ""
        self.location = []
        self.magnitude = 0
        self.feltReports = 0
        self.place = ""
        self.time = 0
        self.updated = 0.0
        self.timezone = 0
        self.url = ""
        self.detail = ""
        self.cdi = 0.0
        self.mmi = 0.0
        self.alert = ""
        self.status= ""
        self.tsunami = ""
        self.sig = 0
        self.net = ""
        self.code = ""
        self.ids = ""
        self.sources = ""
        self.type = ""
        self.nst = 0
        self.dmin = 0.0
        self.rms = 0.0
        self.gap = 0.0
        self.mag = ""
        self.type = ""

    def addEq(self, JSONData, eqNum):
        # Setting id
        self.id = JSONData["features"][eqNum]["id"]
        # Setting location (format: longitude,latitude, depth)
        for i in JSONData["features"][eqNum]["geometry"]["coordinates"]:
            self.location.append(i)
        # Add from "properties" portion of JSON
        self.magnitude = JSONData["features"][eqNum]["properties"]["mag"]
        self.feltReports = JSONData["features"][eqNum]["properties"]["felt"]
        self.place = JSONData["features"][eqNum]["properties"]["place"]
        self.time = JSONData["features"][eqNum]["properties"]["time"]
        self.updated = JSONData["features"][eqNum]["properties"]["updated"]
        self.timezone = JSONData["features"][eqNum]["properties"]["tz"]
        self.url = JSONData["features"][eqNum]["properties"]["url"]
        self.detail = JSONData["features"][eqNum]["properties"]["detail"]
        self.cdi = JSONData["features"][eqNum]["properties"]["cdi"]
        self.mmi = JSONData["features"][eqNum]["properties"]["mmi"]
        self.alert = JSONData["features"][eqNum]["properties"]["alert"]
        self.status = JSONData["features"][eqNum]["properties"]["status"]
        self.tsunami = JSONData["features"][eqNum]["properties"]["tsunami"]
        self.sig = JSONData["features"][eqNum]["properties"]["sig"]
        self.net = JSONData["features"][eqNum]["properties"]["net"]
        self.code = JSONData["features"][eqNum]["properties"]["code"]
        self.ids = JSONData["features"][eqNum]["properties"]["ids"]
        self.sources = JSONData["features"][eqNum]["properties"]["sources"]
        self.type = JSONData["features"][eqNum]["properties"]["type"]
        self.nst = JSONData["features"][eqNum]["properties"]["nst"]
        self.dmin = JSONData["features"][eqNum]["properties"]["dmin"]
        self.rms = JSONData["features"][eqNum]["properties"]["rms"]
        self.gap = JSONData["features"][eqNum]["properties"]["gap"]
        self.type = JSONData["features"][eqNum]["properties"]["type"]

def getEqData(url):
    eqData = []
    eqJSON = requests.get(url).json()
    numberOfEq = eqJSON["metadata"]["count"]

    for i in range(numberOfEq):
        earthquake = Earthquake()
        earthquake.addEq(eqJSON, i)
        eqData.append(earthquake)

    return eqData



if __name__ == '__main__':
    data = getEqData("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
    for i in data:
        print(i.id, i.location, i.magnitude, i.feltReports, i.place, i.time, i.updated, i.timezone,
              i.url, i.detail, i.cdi, i.mmi, i.alert, i.status, i.tsunami, i.sig, i.net,
              i.code,
              i.ids, i.sources, i.type, i.nst, i.dmin, i.rms, i.gap, i.mag, i.type)