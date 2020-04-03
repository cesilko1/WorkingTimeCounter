#!/usr/bin/python3

'''
stops the counting time
'''


from datetime import timedelta
from datetime import datetime
from dateutil.parser import parse
from sys import argv
import sys
import time
import json


jsonFileName = "counting.json"

stopTime = datetime.now()


with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while loading json file!")
		sys.exit()


startTime = datetime.now()

with open(jsonData["csv-path"], "a") as csv:
	csv.write(str(stopTime.day)+". "+str(stopTime.month)+". "+str(stopTime.year)+",")
	csv.write(str(startTime.hour)+":"+str(startTime.minute)+",")
	csv.write(str(stopTime.hour)+":"+str(stopTime.minute)+"\n")
	print("stop timepoint")

with open(jsonFileName, "w") as f:
	jsonData["status"] = "stopped"
	newJsonString = json.dumps(jsonData)
	f.write(newJsonString)