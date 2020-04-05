#!/usr/bin/python3

'''
start counting time
'''

from datetime import datetime
from sys import argv
import json
import sys


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


if jsonData["status"] == "running":
	print("this job is already running!")
	sys.exit()
elif jsonData["status"] == "stopped":
	jsonData["start-time"] = startTime
	jsonData["csv-path"] = csvPath
	jsonData["status"] = "running"
	print("start timepoint")


with open(jsonFileName, "w") as f:
	newString = json.dumps(jsonData)
	f.write(newString)