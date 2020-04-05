#!/bin/bash

if [ $(whoami) == "root" ];
then
	HOME_DIR=$(eval echo ~$SUDO_USER)

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