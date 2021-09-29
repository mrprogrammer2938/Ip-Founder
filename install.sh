#!/bin/sh

if [[ "$(id -u)" -ne 0 ]];
then
	echo "Please, Run This Program as Root!"
	exit
fi

function main() {
	printf '\033]2;Ip-Founder/Installing\a'
	clear
	echo "Installing Ip-Founder..."
	chmod +x ipfounder.py
	sleep 2
	apt install python
	apt install python3
	apt install python3-pip
	apt install --upgrade pip
	echo "

Finish...
Usage:
     python3 ipfounder.py
     "
    exit
}
main
