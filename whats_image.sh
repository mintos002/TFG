#!/bin/bash 
to=34687644952
msg=$1
yowpath=/home/pi/yowsup 
cd ${yowpath}
(sleep 1; echo -e "/L\n/image send $to $msg") | sudo ${yowpath}/yowsup-cli demos -c ${yowpath}/mydetails -y
PID=$!
sleep 10
sudo kill -INT $PID

