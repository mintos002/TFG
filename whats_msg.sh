#!/bin/bash
to=$1
msg=$2
yowpath=/home/pi/yowsup
cd ${yowpath}
(echo -e "/L\n/message send $to $msg"; sleep 5; echo "sudo kill %1") | sudo yowsup-cli demos -c mydetails -y &
