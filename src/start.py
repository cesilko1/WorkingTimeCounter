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


def newData(instance, csvFileName):
	instance = str(instance)
	csvFileName = str(csvFileName)

	newString = '{"'+instance+'":{"start-time":"'+str(startTime)+'", "csv-path":"'+csvFileName+'"} }'
	newJsonData = json.loads(newString)

	return newJsonData





with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while loading json")
		jsonData = newData(argv[1], argv[2])



for instance in jsonData:
	
	if instance == argv[1]:
		#json instance exists
		print("this job is already running!")
		sys.exit()

	else:
		print("adding new instance")
		jsonData.update(newData(argv[1], argv[2]))



with open(jsonFileName, "w") as f:
	print("saving json")
	newString = json.dumps(jsonData)
	f.write(newString)


