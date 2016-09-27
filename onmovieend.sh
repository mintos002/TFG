#!/bin/bash
wn=34687644952                 #Numero telefono
tu="Alex_Juan"                 #Nombre usuario de telegram
img=$1                         #Path del video
msg="Subiendo video a dropbox" #Mensaje
yowpath=/home/pi/yowsup        #Path to yowsup

dropbox_uploader.sh -s upload $img rpicamara &   #Subir imagen a la carpeta rpicamara en dropbox

/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje al usuario


