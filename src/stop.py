#!/usr/bin/python3

from datetime import timedelta
from datetime import datetime
from dateutil.parser import parse
from sys import argv
import sys
import time
import json


jsonFileName = "counting.json"

stopTime = datetime.now()


def getWorkingTime(startString):
	return startString


with open(jsonFileName) as f:
	jsonString = f.read()

	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while loading json file")
		sys.exit()


try:
	if jsonData[argv[1]]["running"] == "True":

		startTime = datetime.strptime(jsonData[argv[1]]["start-time"], '%Y-%m-%d %H:%M:%S.%f')
		print(startTime.minute)

		with open(jsonData[argv[1]]["csv-path"], "a") as wf:
			pass

	else:
		print("this job is not running")
except:
	print("error: unstarted job")