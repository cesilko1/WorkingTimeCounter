#!/usr/bin/python3

import json


jsonFileName = "counting.json"

with open(jsonFileName) as file:
	jsonString = file.read()

	try:
		jsonData = json.loads(jsonString)
		print("Status of timepointer: "+jsonData["status"])
		print("csv file: "+jsonData["csv-path"])

	except:
		print("Error while reading json file")
