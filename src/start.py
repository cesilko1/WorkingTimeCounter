#!/usr/bin/python3

'''
start instance
'''

from datetime import datetime
from sys import argv
import json
import sys


jsonFileName = "counting.json"

startTime = datetime.now()

exists = False
instance_name = ""


def newData(instance, csvFileName, running):
	instance = str(instance)
	csvFileName = str(csvFileName)

	newString = '{"'+instance+'":{"start-time":"'+str(startTime)+'", "csv-path":"'+csvFileName+'", "running":"'+str(running)+'"} }'
	newJsonData = json.loads(newString)

	return newJsonData




with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		jsonData = newData(argv[1], argv[2], True)



for instance in jsonData:
	if instance == argv[1]:
		exists = True
		instance_name = instance
		break


if exists:
	if jsonData[instance_name]["running"] == "False":
		jsonData[instance_name]["start-time"] = str(startTime)
		jsonData[instance_name]["running"] = True
	else:
		pass

else:
	jsonData.update(newData(argv[1], argv[2], True))

with open(jsonFileName, "w") as f:
	newString = json.dumps(jsonData)
	f.write(newString)