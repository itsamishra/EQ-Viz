import requests
# TODO replace list with an Earthquake Data class
def getEqData(url):
    a = requests.get(url).json()

    # Relevent earthquake info
    eqLocs = []
    eqMags = []
    eqFelt = []

    # Gathering earthquake info
    for i in a["features"]:
        eqMags.append(i["properties"]["mag"])
        eqLocs.append(i["properties"]["place"])
        eqFelt.append(i["properties"]["felt"])

    # Putting all data in single list
    eqData = []
    for i in range(len(eqLocs)):
        eqData.append([eqLocs[i], eqMags[i], eqFelt[i]])

    return eqData