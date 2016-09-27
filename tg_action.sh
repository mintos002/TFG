#!/bin/bash
PATH=/home/pi/tg
${PATH}/bin/telegram-cli -k ${PATH}/tg-server.pub -W -s ${PATH}/action.lua &
