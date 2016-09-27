#!/bin/bash
# -*- coding: utf-8 -*-
msg="Cámara encendida"

mjpg_streamer -b -i "input_uvc.so -y -r 640x480 -f 30" -o "output_http.so -w /usr/www"    # Ejecutar mmjpg_streamer
sleep 1                                                                                   # Esperar 1.5 segundos
motion &                                                                                  # Ejecutar motion
sleep 1                                                                                   # Esperar 1.5 segundos

/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje
