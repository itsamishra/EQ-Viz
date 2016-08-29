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

if __name__ == '__main__':
    print(getURL(["Past Hour", "1.0+"]))