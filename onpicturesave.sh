#!/bin/bash
wn=34687644952                   #Numero telefono
tu="Alex_Juan"                     #Nombre usuario de telegram
img=$1                           #Path de la imagen
msg="Subiendo imagen a dropbox"  #Mensaje
yowpath=/home/pi/yowsup          #Path to yowsup

dropbox_uploader.sh -s upload $img rpicamara &   #Subir imagen a la carpeta rpicamara en dropbox
#sudo ${yowpath}/yowsup-cli demos -c ${yowpath}/mydetails -s "$wn" "$msg" &  #Avisar de la subida a dropbox
#/home/pi/tg_msg.sh $tu "$msg" & #Avisar de la subida a dropbox
#/home/pi/tg_photo.sh $tu $img & #Enviar foto por telegram
/home/pi/enviarmensaje.sh TEW "$msg" & #Enviar mensaje al usuario
sleep 3
/home/pi/enviarmensaje.sh te "$img" & # Envia la imagen al usuario
#python /home/pi/sendemail.py "$msg" $img&  #Enviar email

