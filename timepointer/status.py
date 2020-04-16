#!/usr/bin/python3

'''
Script for showing status of timepointer.

Created by Vilém Raška.
Released under MIT License.
'''

import json


jsonFileName = "timepointer.json"

with open(jsonFileName) as file:
	jsonString = file.read()

	try:
		jsonData = json.loads(jsonString)
		print("Status of timepointer: "+jsonData["status"])
		print("csv file: "+jsonData["csv-path"])

	except:
		print("Error while reading json file")
