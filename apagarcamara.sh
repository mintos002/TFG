#!/bin/bash
# -*- coding: utf-8 -*-
msg="Cámara apagada"

sudo pkill -f motion                                                                # Cerrar motion
sleep 1.5                                                                           # Esperar 1.5 segundos
sudo pkill -f mjpg_streamer                                                         # Cerrar mmjpg_streamer

/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje 

