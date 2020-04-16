#!/bin/bash

#Script for uninstalling timepointer from your Debian based system.
#
#Created by Vilém Raška 2020.
#This script is released under MIT License.
#==========================================


#check if the script has root privileges
if [ $(whoami) == "root" ];
then
	#set home directory where should be timepointer installed
	HOME_DIR=$(eval echo ~$SUDO_USER)

	#check if the timepointer is installed in this system
	if [ -f /usr/bin/timepointer ];
	then
		echo "uninstalling working timepointer"

		echo "removing command file"
		rm -fv /usr/bin/timepointer

		echo "clearing working directory"
		rm -rfv $HOME_DIR/.timepointer

		echo "timepointer has been uninstalled"
	else
		echo "timepointer is not installed yet"
	fi
else
	echo "please run this script with sudo"
fi