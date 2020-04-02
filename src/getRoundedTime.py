#!/usr/bin/python3

from datetime import datetime
from datetime import timedelta

def getRoundedTime(dt, delta):
	return dt + (datetime.min - dt) % delta