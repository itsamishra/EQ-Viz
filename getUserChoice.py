def getURL(userChoice):
    url = ""
    if userChoice[0] == "Past Hour":
        if userChoice[1] == "1.0+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
        elif userChoice[1] == "2.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
        elif userChoice[1] == "4.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"
        elif userChoice[1] == "--ALL--":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    elif userChoice[0] == "Past Day":
        if userChoice[1] == "1.0+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"
        elif userChoice[1] == "2.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
        elif userChoice[1] == "4.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
        elif userChoice[1] == "--ALL--":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    elif userChoice[0] == "Past 7 Days":
        if userChoice[1] == "1.0+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson"
        elif userChoice[1] == "2.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"
        elif userChoice[1] == "4.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
        elif userChoice[1] == "--ALL--":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    elif userChoice[0] == "Past 30 Days":
        if userChoice[1] == "1.0+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
        elif userChoice[1] == "2.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
        elif userChoice[1] == "4.5+":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
        elif userChoice[1] == "--ALL--":
            url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    return url

def getXYAxis(userChoice):
    x = ""
    y = ""
    if userChoice[2] == "Magnitude":
        x = "magnitude"
    elif userChoice[2] == "Depth":
        x = "depth"
    elif userChoice[2] == "Time":
        x = "time"
    elif userChoice[2] == "Time Zone":
        x = "timezone"
    elif userChoice[2] == "Felt Reports":
        x = "feltReports"
    elif userChoice[2] == "Max reported intensity":
        x = "cdi"
    elif userChoice[2] == "Max instrumental intensity":
        x = "mmi"
    elif userChoice[2] == "Epicenter to station distance":
        x = "dmin"
    elif userChoice[2] == "Root mean squared travel time":
        x = "rms"
    elif userChoice[2] == "Gap between closest stations":
        x = "gap"

    if userChoice[3] == "Magnitude":
        y = "magnitude"
    elif userChoice[3] == "Depth":
        y = "depth"
    elif userChoice[3] == "Time":
        y = "time"
    elif userChoice[3] == "Time Zone":
        y = "timezone"
    elif userChoice[3] == "Felt Reports":
        y = "feltReports"
    elif userChoice[3] == "Max reported intensity":
        y = "cdi"
    elif userChoice[3] == "Max instrumental intensity":
        y = "mmi"
    elif userChoice[3] == "Epicenter to station distance":
        y = "dmin"
    elif userChoice[3] == "Root mean squared travel time":
        y = "rms"
    elif userChoice[3] == "Gap between closest stations":
        y = "gap"

    return x,y

if __name__ == '__main__':
    print(getURL(["Past Hour", "1.0+"]))