#!/bin/bash

if [ -f /usr/bin/timepointer ]
then
	echo "timepointer is aleready installed"

else
	echo "installing timepointer"

	echo "creating working dir"
	mkdir ~/.timepointer
	mkdir ~/.timepointer/src

	echo "copying files"
	cp -v src/*.py ~/.timepointer/src/
	cp -v src/timepointer.sh ~/.timepointer/src/
	cp -v help.txt ~/.timepointer/

	echo "creating json file"
	touch ~/.timepointer/src/counting.json

	echo "writing data to json file"
	echo '{ "start-time": "", "csv-path": "", "status": "stopped" }' >> ~/.timepointer/src/counting.json

	echo "creating symlink"
	sudo ln -sv ~/.timepointer/src/timepointer.sh /usr/bin/timepointer

	if [ -f /usr/bin/timepointer ]
	then
		echo
		echo "timepointer has been installed sucessfully"
		echo "for more information type: timepointer --help"
	fi
fi