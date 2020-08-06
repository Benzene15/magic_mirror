import requests
import json
import calendar
import time
from math import floor
import geocoder

def calc_days():
    '''Takes the number of seconds that we have 
       had together and calculates it to days'''
    timeSinceEpoch=int(calendar.timegm(time.gmtime()))
    epochToBigDay=1501711200
    ourTime= timeSinceEpoch-epochToBigDay
    return floor(ourTime/86400)

quotes= ["Change your thoughts and you change your world. - Norman Vincent Peale",
		"It's a beautiful day to save lives -Derek Shepard",
		"I can't change the direction of the wind, but I can adjust my sails to always reach my destination. -Jimmy Dean"]

#The url for the api request	
url = "https://community-open-weather-map.p.rapidapi.com/weather"

#lat and lon coords to call with api
lat,lon = geocoder.ip('me').latlng

#make and set our query init to (0,0) if coords can't be found
querystring = {"lat":"0","lon":"0","units":"imperial"}
querystring["lat"]=str(lat)
querystring["lon"]=str(lon)

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "c3a8bf4f4dmsh80a23d2f83e4ad1p13093fjsn898b5d24848b"
    }

temp_data = requests.request("GET", url, headers=headers, params=querystring)
temp_data=json.loads(temp_data.content)
#1 hPa -> 0.029529983071445 inHg


print(temp_data)
print(calc_days())