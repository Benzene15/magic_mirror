import requests
import json
import calendar
import time
import datetime
from math import floor
import geocoder
import random
import csv


def calc_days():
    '''Takes the number of seconds that we have 
       had together and calculates it to days'''
    timeSinceEpoch=int(calendar.timegm(time.gmtime()))
    epochToBigDay=1501711200
    ourTime= timeSinceEpoch-epochToBigDay
    return floor(ourTime/86400)

def random_quote():
    f=open("Quotes.csv")

    num=random.randint(0,75965)
    csv_reader=csv.reader(f,delimiter=';')
    quote=""

    #skip first line
    for row in csv_reader:
        break
    i=1
    for row in csv_reader:
        quote=(row[0]+" -"+row[1])
        if i==num:
            f.close()
            return quote
        else:
            i+=1

def weather():
    #The url for the api request	
    weather_url = "https://community-open-weather-map.p.rapidapi.com/weather"

    #lat and lon coords to call with api
    lat,lon = geocoder.ip('me').latlng
    #UWM_coords=(43.076070,-87.882350)

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
    return temp_data

def date_time():
    t = time.localtime()
    print(t)
    year=str(t[0])
    month=str(t[1])
    day=str(t[2])
    hour=t[3]
    if(hour==0):
        hour="00"
    else:
        hour=str(hour)
    minute=t[4]
    if(minute<10):
        minute='0'+str(minute)
    elif(minute==0):
        minute="00"
    else:
        minute=str(minute)
    second=str(t[5])
    
    return year,month,day,hour,minute,second

def main():
    date_time()
    print(date_time()[4])
    print(weather()['weather'])

def oldmain():
    #quotes= ["Change your thoughts and you change your world; Norman Vincent Peale",
    #        "It's a beautiful day to save lives;Derek Shepard",
    #        "I can't change the direction of the wind, but I can adjust my sails to always reach my destination;Jimmy Dean"]
    
    #find minute and hour for when to call funcs
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hour=int(current_time[:2])
    minute=int(current_time[3:5])
    second=int(current_time[7:9])
    print(second)

    rand_int=random.randint(0,75965)
    rand_quote=random_quote(rand_int)

    #Every five run this
    if(minute%5==0):
        #The url for the api request	
        weather_url = "https://community-open-weather-map.p.rapidapi.com/weather"

        #lat and lon coords to call with api
        lat,lon = geocoder.ip('me').latlng

        #UWM_coords=(43.076070,-87.882350)

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

    
    #Probably have to pay for this, so heck
    orig_coord = lat, lon
    dest_coord = UWM_coords[0], UWM_coords[1]
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
    drive=requests.request("GET", url)
    drive=json.loads(drive.content)
    print(drive)
    
    #use the csv to grab a random quote
    rand_int=random.randint(0,75965)
    rand_quote=random_quote(rand_int)

    return temp_data,calc_days(),rand_quote


if __name__ == "__main__":
    main()