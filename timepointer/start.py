#!/usr/bin/python3

'''
This short script saves current time and given path to csv into json.

Created by Vilém Raška 2020.
Released under MIT License.
===========================
'''

from datetime import datetime
from sys import argv
import sys
import json



def roundMinute(time):
	roundedMinutes = round(time.minute / 15) * 15

	if roundedMinutes == 60:
		roundedMinutes = 0
		returnTime = datetime(time.year, time.month, time.day, time.hour+1, roundedMinutes)
	else:
		returnTime = datetime(time.year, time.month, time.day, time.hour, roundedMinutes)	

	return returnTime



#name of file where to save datetime and csv path.
jsonFileName = "timepointer.json"

startTime = datetime.now()

csvPath = argv[1]




with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while reading json file!")
		sys.exit()


if jsonData["status"] == "pointed":
	print("timepointer is already pointed!")
	sys.exit()

elif jsonData["status"] == "free":
	jsonData["start-time"] = str(startTime)
	jsonData["csv-path"] = csvPath
	jsonData["status"] = "pointed"
	print("start timepoint for: "+str(roundMinute(startTime).hour)+":"+str(roundMinute(startTime).minute))


with open(jsonFileName, "w") as f:
	newString = json.dumps(jsonData)
	f.write(newString)