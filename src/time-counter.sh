#!/bin/bash

#cd ~/.working-time-counter

case $1 in
	start)
		python3 start.py $2 $3
		echo "starting counting time for $2"
		;;
	stop)
		echo "stopping counting time for $2"
		python3 stop.py $2
		;;
	help)
		cat ../help.txt
		;;
	*)
		cat ../help.txt
		;;
esac