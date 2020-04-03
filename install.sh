#!/bin/bash

if [ -f /usr/bin/timepointer ]
then
echo "timepointer is aleready installed"

else
echo "installing timepointer"

echo "creating working dir"
mkdir ~/.timepointer

echo "copying files"
cp -rv src/ ~/.timepointer/
cp -v help.txt ~/.timepointer/

echo "creating link to command"
sudo ln -sv ~/.timepointer/src/timepointer.sh /usr/bin/timepointer

echo "timepointer has been installed sucessfully"
echo
echo "for more information type: timepointer --help"
fi