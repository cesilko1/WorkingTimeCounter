#!/usr/bin/python3

'''
start instance
'''

from datetime import datetime
from sys import argv
import json


jsonFileName = "counting.json"

startTime = datetime.now()

with open(jsonFileName) as f:
	jsonString = f.read()
	jsonData = json.loads(jsonString)


for instance in jsonData:
	if instance == argv[1]:
		if jsonData[instance]["running"] == True:
			return