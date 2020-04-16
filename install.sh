#!/bin/bash

#Script for installing timepointer into Ubuntu based system.
#
#Created by Vilém Raška 2020.
#This script is released under MIT License.
#==========================================

#check if the script has root privileges
if [ $(whoami) == "root" ];
then
	#set home directory for installation
	HOME_DIR=$(eval echo ~$SUDO_USER)

	#check if the timepointer is already installed
	if [ -f /usr/bin/timepointer ];
	then
		echo "timepointer is aleready installed"

	else
		echo "installing timepointer"

		echo "creating working dir"
		mkdir $HOME_DIR/.timepointer

		echo "copying files"
		cp -v timepointer/*.py $HOME_DIR/.timepointer/
		cp -v timepointer/timepointer.sh $HOME_DIR/.timepointer/
		cp -v help.txt $HOME_DIR/.timepointer/

		echo "creating json file"
		touch $HOME_DIR/.timepointer/timepointer.json

		echo "writing data to json file"
		echo '{ "start-time": "", "csv-path": "", "status": "free" }' >> $HOME_DIR/.timepointer/timepointer.json

		echo "creating symlink"
		ln -sv $HOME_DIR/.timepointer/timepointer.sh /usr/bin/timepointer

		echo "setting permissions"
		chown -Rv $SUDO_USER $HOME_DIR/.timepointer

		#check if the timepointer is installed successfully
		if [ -f /usr/bin/timepointer ];
		then
			echo
			echo "timepointer has been installed successfully"
			echo "for more information type: timepointer --help"
		fi
	fi
else
	echo "please run this script with sudo"
fi