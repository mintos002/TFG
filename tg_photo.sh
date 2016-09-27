#!/bin/bash
to=$1
msg=$2
tgpath=/home/pi/tg
cd ${tgpath}
(sleep 1; echo "contact_list"; sleep 1; echo "safe_quit") | ${tgpath}/bin/telegram-cli -W -k tg-server.pub -e "send_photo $to $msg"
