#!/bin/bash

if [ -f /usr/bin/timepointer ];
then
echo "uninstalling working timepointer"

echo "removing command file"
sudo rm -fv /usr/bin/timepointer

echo "clearing working directory"
rm -rfv ~/.timepointer

echo "timepointer has been uninstalled"
else
echo "timepointer is not installed yet"
fi