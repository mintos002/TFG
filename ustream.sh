#!/bin/bash
# -*- coding: utf-8 -*-
wn=34687644952
tn="Alex_Juan"
msg="Ustream activado, mira lo que está pasando en: http://www.ustream.tv/channel/dqEMu9XW2pz"

RTMP_URL=rtmp://1.22604875.fme.ustream.tv/ustreamVideo/22604875
STREAM_KEY=r4PjKu3xBQYzeLxrPRRSannJ5KEwCeWE

#RTMP_URL=rtmp://1.22707727.fme.ustream.tv/ustreamVideo/22707727
#STREAM_KEY=jZEPa4AKR8AEDJ74RrChPtGgtGQTwNHN

avconv -f mjpeg -r 1 -i "http://localhost:8081/" -f flv $RTMP_URL/$STREAM_KEY &

/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje al usuario



