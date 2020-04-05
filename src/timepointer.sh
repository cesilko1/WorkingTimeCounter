#!/bin/bash


csv_path=$PWD/$2

cd ~/.timepointer/src

case $1 in
	--start)
		if [ $# == 2 ];
		then
			if [ -f $csv_path ];
			then
				python3 start.py $csv_path
			else
				touch $csv_path
				echo 'date,start,stop' >> $csv_path
				python3 start.py $csv_path
			fi
		else
			echo "please specify csv file"
		fi
		;;
	--stop)
		python3 stop.py
		;;
	--status)
		python3 status.py
		;;
	--help)
		cat ../help.txt
		;;
	*)
		cat ../help.txt
		;;
esac