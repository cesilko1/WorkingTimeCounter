#!/bin/bash

cd ~/.timepointer/src

case $1 in
	--start)
		touch $2
		python3 start.py $2
		;;
	--stop)
		python3 stop.py
		;;
	--help)
		cat ../help.txt
		;;
	*)
		cat ../help.txt
		;;
esac