#!/bin/bash

#Script for running timepointer.
#
#Created by Vilém Raška 2020.
#This script is released under MIT License.
#==========================================


#set directory where to write to given csv file
csv_path=$PWD/$2

#go to timepointer working directory
cd ~/.timepointer


case $1 in
	start)
		#check number of flags
		if [ $# == 2 ];
		then
			#check if the csv file exists
			if [ ! -f $csv_path ];
			then
				#create new csv file
				touch $csv_path

				#write reader into csv file
				echo 'date,start,stop,note' >> $csv_path
			fi

			#run python script for setting timepoint vith given csv path
			python3 start.py $csv_path
		else
			echo "please specify csv file"
		fi
		;;

	stop)
		#check if the count of arguments ig higher than 1
		if [ $# > 1 ]
		then
			msg=""

			#put all arguments into string divided by space
			while test $# -gt 0
			do
				msg+=" $1"
				shift
			done
			
			python3 stop.py "${msg:6}"
		else
			python3 stop.py
		fi
		;;

	status)
		python3 status.py
		;;

	help)
		cat help.txt
		;;

	*)
		cat help.txt
		;;
esac