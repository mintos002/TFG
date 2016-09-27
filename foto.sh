#!/bin/bash

DATE=$(date +"%Y%m%d%H%M%S")
echo $DATE
raspistill -vf -hf -o /home/pi/camera/$DATE.jpg
