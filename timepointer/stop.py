#!/usr/bin/python3

'''

'''

from datetime import datetime
import json


def roundMinute(time):
	roundedMinutes = round(time.minute / 15) * 15

	if roundedMinutes == 60:
		roundedMinutes = 0
		returnTime = datetime(time.year, time.month, time.day, time.hour+1, roundedMinutes)
	else:
		returnTime = datetime(time.year, time.month, time.day, time.hour, roundedMinutes)	

	return returnTime



jsonFileName = "timepointer.json"

stopTime = datetime(2020, 4, 6, 10, 56)


with open(jsonFileName) as f:
	jsonString = f.read()
	try:
		jsonData = json.loads(jsonString)
	except:
		print("error while loading json file!")
		sys.exit()


startTime = datetime.strptime(jsonData["start-time"], '%Y-%m-%d %H:%M:%S.%f')

with open(jsonData["csv-path"], "a") as csv:
	csv.write(str(stopTime.day)+". "+str(stopTime.month)+". "+str(stopTime.year)+",")
	csv.write(str(roundMinute(startTime).hour)+":"+str(roundMinute(startTime).minute)+",")
	csv.write(str(roundMinute(stopTime).hour)+":"+str(roundMinute(stopTime).minute)+"\n")
	print("stopped: "+str(roundMinute(stopTime).hour)+":"+str(roundMinute(stopTime).minute))

with open(jsonFileName, "w") as f:
	jsonData["status"] = "stopped"
	newJsonString = json.dumps(jsonData)
	f.write(newJsonString)