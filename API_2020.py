import requests
import json
import calendar
import time
from math import floor
import geocoder
#import urllib

def calc_days():
    '''Takes the number of seconds that we have 
       had together and calculates it to days'''
    timeSinceEpoch=int(calendar.timegm(time.gmtime()))
    epochToBigDay=1501711200
    ourTime= timeSinceEpoch-epochToBigDay
    return floor(ourTime/86400)

def main():
    quotes= ["Change your thoughts and you change your world. - Norman Vincent Peale",
            "It's a beautiful day to save lives -Derek Shepard",
            "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. -Jimmy Dean"]

    #The url for the api request	
    weather_url = "https://community-open-weather-map.p.rapidapi.com/weather"

    #lat and lon coords to call with api
    lat,lon = geocoder.ip('me').latlng

    UWM_coords=(43.076070,-87.882350)

    #make and set our query init to (0,0) if coords can't be found
    querystring = {"lat":"0","lon":"0","units":"imperial"}
    querystring["lat"]=str(lat)
    querystring["lon"]=str(lon)

    headers = {
        'x-rapidapi-key': "c3a8bf4f4dmsh80a23d2f83e4ad1p13093fjsn898b5d24848b"
        }

    temp_data = requests.request("GET", weather_url, headers=headers, params=querystring)
    temp_data=json.loads(temp_data.content)
    #1 hPa -> 0.029529983071445 inHg

    ''' Probably have to pay for this, so heck
    orig_coord = lat, lon
    dest_coord = UWM_coords[0], UWM_coords[1]
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
    drive=requests.request("GET", url)
    drive=json.loads(drive.content)
    print(drive)
    '''

    print(temp_data)
    print(calc_days())

if __name__ == "__main__":
    main()