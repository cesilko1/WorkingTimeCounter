#!/bin/bash

csv_path=$PWD/$2

cd ~/.timepointer/src

case $1 in
	--start)
		touch $csv_path
		python3 start.py $csv_path
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