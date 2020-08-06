import requests
import json
import calendar
import time
import datetime
import sys
import string

def calcTime(time,years,months, days, hours, minutes, seconds):
	years= time/(365.25*24*60*60)
	time=time-(years*(60*60*24*365))
	years=int(years)
	months=time/(29.53*24*60*60)
	months= int(months)
	time= time-(months*(29.53*24*60*60))
	time=int(time)
	days=time/(24*60*60)
	time=time-(days*(24*60*60))
	hours =time/(60*60)
	time=time-(hours*60*60)
	minutes=time/(60)
	time=time-(minutes*60)
	seconds=time
	return (years,months,days, hours, minutes,seconds)
	
quotes= ["Change your thoughts and you change your world. - Norman Vincent Peale",
		"It's a beautiful day to save lives -Derek Shepard",
		"I can't change the direction of the wind, but I can adjust my sails to always reach my destination. -Jimmy Dean"]
	
url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"lat":"44.969","lon":"-93.222","callback":"Minneapolis","units":"imperial","mode":""}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "c3a8bf4f4dmsh80a23d2f83e4ad1p13093fjsn898b5d24848b"
    }

rawData = requests.request("GET", url, headers=headers, params=querystring)
intData=rawData.content[12:-1]
tempData= json.loads(intData)
tempData=tempData['main']							#pressure in inHg= num/33.8436
print(tempData['temp'])


timeSinceEpoch=int(calendar.timegm(time.gmtime()))
epochToBigDay=1501711200
ourTime= timeSinceEpoch-epochToBigDay
if True:																#This is just so I can condense the code
	years=0
	months=0
	days=0
	hours=0
	minutes=0
	seconds=0
	timeList=calcTime(ourTime, years, months, days, hours, minutes, seconds)
	years=timeList[0]
	months=timeList[1]
	days=timeList[2]
	hours=timeList[3]
	minutes=timeList[4]
	seconds=timeList[5]
	#print('You\'ve been stuck with this nerd for about:' + '\n' + str(years)+' Years '+ str(months) +' Month(s) ' + str(days) + ' Day(s) '+str(hours) +' Hour(s) ' + str(minutes)+' Minute(s) '+ str(seconds) +' Second(s) ') 
	print("")




