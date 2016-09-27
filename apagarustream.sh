#!/bin/bash
msg="Streaming en Ustream apagado"

#sudo pkill -f ustream.sh
sudo pkill -f "avconv -f mjpeg" # Cerrar el proceso de streaming

/home/pi/enviarmensaje.sh TEW "$msg" # Enviar mensaje


