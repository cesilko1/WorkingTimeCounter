#!/usr/bin/python3

'''
This short script saves current time and given path to csv into json.

Created by Vilém Raška.
Released under MIT License.
'''

from datetime import datetime
from sys import argv
import json
import sys

#name of file where to save datetime and csv path.
jsonFileName = "timepointer.json"

startTime = str(datetime.now())

csvPath = argv[1]




with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while reading json file!")
		sys.exit()


if jsonData["status"] == "pointed":
	print("this job is already running!")
	sys.exit()

elif jsonData["status"] == "free":
	jsonData["start-time"] = startTime
	jsonData["csv-path"] = csvPath
	jsonData["status"] = "pointed"
	print("start timepoint")


with open(jsonFileName, "w") as f:
	newString = json.dumps(jsonData)
	f.write(newString)